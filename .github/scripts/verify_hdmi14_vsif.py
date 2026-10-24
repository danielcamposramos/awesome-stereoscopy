#!/usr/bin/env python3
"""Check HDMI 1.4 Vendor-Specific InfoFrame arithmetic and frame-packing rasters.

Packs and unpacks the HDMI 1.4 VSIF (OUI 0x000C03) in plain Python, following the
layout Linux implements in drivers/video/hdmi.c, and checks the numbers quoted in
docs/frame-packing-and-hdmi-timings.md. The HDMI Forum VSIF (OUI 0xC45DD8) is a
later generation and is deliberately rejected here, not decoded.

Requires Python 3 only. It checks arithmetic, not how any sink behaves.
"""

from pathlib import Path
import re
import unittest


VENDOR_INFOFRAME = 0x81
VERSION = 1
HEADER = 4  # HB0, HB1, HB2 and the PB0 checksum, as HDMI_INFOFRAME_HEADER_SIZE.
HDMI14_OUI = 0x000C03
HDMI_FORUM_OUI = 0xC45DD8
NO_FORMAT, EXTENDED_RESOLUTION, FORMAT_3D = 0, 1, 2  # HDMI_Video_Format, PB4 [7:5]
SIDE_BY_SIDE_HALF = 8
STRUCTURES = {
    0: "frame packing",
    1: "field alternative",
    2: "line alternative",
    3: "side-by-side full",
    4: "L + depth",
    5: "L + depth + graphics + graphics-depth",
    6: "top-and-bottom",
    8: "side-by-side half",
}  # Codes 7 and 9-15 are reserved.
GUIDE = Path(__file__).resolve().parents[2] / "docs" / "frame-packing-and-hdmi-timings.md"


def checksum(packet):
    """PB0 makes every byte of header and payload sum to zero, modulo 256."""
    return (256 - sum(packet)) % 256


def payload_length(structure=None, vic=None):
    """HB2: 3D_Ext_Data adds a byte only for structures 8 and above."""
    if structure is not None and structure >= SIDE_BY_SIDE_HALF:
        return 6
    if structure is not None or vic is not None:
        return 5
    return 4


def pack(structure=None, ext_data=0, vic=None):
    if structure is not None and vic is not None:
        raise ValueError("HDMI_VIC and 3D_Structure are alternatives, not both")
    if structure is not None and structure not in STRUCTURES:
        raise ValueError(f"3D_Structure {structure} is reserved")
    if not 0 <= ext_data <= 15:
        raise ValueError("3D_Ext_Data is four bits")
    if vic is not None and not 1 <= vic <= 255:
        raise ValueError("HDMI_VIC is one non-zero byte")
    length = payload_length(structure, vic)
    packet = bytearray(HEADER + length)
    packet[0:4] = (VENDOR_INFOFRAME, VERSION, length, 0)
    packet[4:7] = HDMI14_OUI.to_bytes(3, "little")
    if structure is not None:
        packet[7] = FORMAT_3D << 5
        packet[8] = structure << 4
        if structure >= SIDE_BY_SIDE_HALF:
            packet[9] = ext_data << 4
    elif vic is not None:
        packet[7] = EXTENDED_RESOLUTION << 5
        packet[8] = vic
    packet[3] = checksum(packet)
    return bytes(packet)


def unpack(packet):
    """Return the fields of an HDMI 1.4 VSIF, or raise ValueError."""
    if len(packet) < HEADER or packet[0] != VENDOR_INFOFRAME or packet[1] != VERSION:
        raise ValueError("not a version 1 vendor-specific InfoFrame")
    length = packet[2]
    if length not in (4, 5, 6) or len(packet) < HEADER + length:
        raise ValueError(f"payload length {length} does not fit an HDMI 1.4 VSIF")
    if sum(packet[:HEADER + length]) % 256:
        raise ValueError("checksum does not bring the packet to zero")
    oui = int.from_bytes(packet[4:7], "little")
    if oui == HDMI_FORUM_OUI:
        raise ValueError("HDMI Forum VSIF: a different generation, not HDMI 1.4")
    if oui != HDMI14_OUI:
        raise ValueError(f"OUI 0x{oui:06X} is not HDMI 1.4's 0x{HDMI14_OUI:06X}")
    video_format = packet[7] >> 5
    if video_format in (FORMAT_3D, EXTENDED_RESOLUTION) and length < 5:
        raise ValueError(f"HDMI_Video_Format {video_format} needs PB5, payload length {length}")
    fields = {"structure": None, "ext_data": 0, "vic": None}
    if video_format == FORMAT_3D:
        fields["structure"] = packet[8] >> 4
        if fields["structure"] not in STRUCTURES:
            raise ValueError(f"3D_Structure {fields['structure']} is reserved")
        if fields["structure"] >= SIDE_BY_SIDE_HALF:
            fields["ext_data"] = packet[9] >> 4 if length == 6 else None
    elif video_format == EXTENDED_RESOLUTION:
        fields["vic"] = packet[8]
    elif video_format != NO_FORMAT:
        raise ValueError(f"HDMI_Video_Format {video_format} is reserved")
    if length != payload_length(fields["structure"], fields["vic"]):
        raise ValueError(f"payload length {length} does not match its contents")
    return fields


def frame_packed(hactive, vactive, htotal, vtotal, clock_khz):
    """Frame packing as drm_mode_set_crtcinfo() doubles a 2D timing."""
    return {"active": (hactive, vactive + vtotal), "vtotal": 2 * vtotal,
            "gap": vtotal - vactive, "clock_khz": 2 * clock_khz,
            "htotal": htotal}


# 2D timings from the CTA-861 table in Linux drivers/gpu/drm/drm_edid.c:
# (name, hactive, vactive, htotal, vtotal, refresh, pixel clock in kHz).
CTA_TIMINGS = (
    ("1080p24 (VIC 32)", 1920, 1080, 2750, 1125, 24, 74250),
    ("720p60 (VIC 4)", 1280, 720, 1650, 750, 60, 74250),
    ("720p50 (VIC 19)", 1280, 720, 1980, 750, 50, 74250),
)


class Hdmi14VsifTests(unittest.TestCase):
    def test_hand_computed_packets(self):
        """Packets worked out by hand, not by pack(): the independent oracle."""
        golden = {
            "frame packing": (dict(structure=0), "81 01 05 2A 03 0C 00 40 00"),
            "top-and-bottom": (dict(structure=6), "81 01 05 CA 03 0C 00 40 60"),
            "side-by-side half": (dict(structure=8), "81 01 06 A9 03 0C 00 40 80 00"),
            "HDMI_VIC 1": (dict(vic=1), "81 01 05 49 03 0C 00 20 01"),
            "no format": (dict(), "81 01 04 6B 03 0C 00 00"),
        }
        for name, (fields, hex_bytes) in golden.items():
            with self.subTest(packet=name):
                self.assertEqual(pack(**fields).hex(" ").upper(), hex_bytes)
                self.assertEqual(sum(bytes.fromhex(hex_bytes)) % 256, 0)

    def test_every_structure_round_trips(self):
        """All eight structures, and all sixteen 3D_Ext_Data values for code 8."""
        for structure in STRUCTURES:
            for ext_data in (range(16) if structure >= SIDE_BY_SIDE_HALF else (0,)):
                with self.subTest(structure=STRUCTURES[structure], ext_data=ext_data):
                    packet = pack(structure, ext_data)
                    self.assertEqual(len(packet), HEADER + packet[2])
                    self.assertEqual(packet[2], 6 if structure >= SIDE_BY_SIDE_HALF else 5)
                    self.assertEqual(sum(packet) % 256, 0)
                    self.assertEqual(packet[4:7], b"\x03\x0c\x00")
                    self.assertEqual(packet[7], 0x40)
                    self.assertEqual(packet[8], structure << 4)
                    self.assertEqual(unpack(packet), {"structure": structure,
                                                      "ext_data": ext_data, "vic": None})

    def test_every_vic_round_trips(self):
        for vic in range(1, 256):
            with self.subTest(vic=vic):
                packet = pack(vic=vic)
                self.assertEqual((packet[2], packet[7], packet[8]), (5, 0x20, vic))
                self.assertEqual(unpack(packet), {"structure": None, "ext_data": 0, "vic": vic})

    def test_any_single_byte_change_breaks_the_checksum(self):
        for structure in (0, 6, 8):
            packet = pack(structure)
            for index in range(len(packet)):
                with self.subTest(structure=structure, byte=index):
                    damaged = bytearray(packet)
                    damaged[index] ^= 0x01
                    with self.assertRaises(ValueError):
                        unpack(bytes(damaged))

    def test_lengths_that_do_not_match_contents_are_rejected(self):
        """Side-by-side half without 3D_Ext_Data, and frame packing with a spare byte."""
        def relength(packet, length):
            body = bytearray(packet[:HEADER + min(length, packet[2])])
            body.extend(bytes(HEADER + length - len(body)))
            body[2], body[3] = length, 0
            body[3] = checksum(body)
            return bytes(body)

        for structure, length in ((8, 5), (0, 6), (6, 4)):
            with self.subTest(structure=STRUCTURES[structure], length=length):
                with self.assertRaises(ValueError):
                    unpack(relength(pack(structure), length))

    def test_reserved_and_conflicting_fields_are_refused(self):
        for structure in (7, *range(9, 16)):
            with self.subTest(reserved=structure):
                with self.assertRaises(ValueError):
                    pack(structure)
        with self.assertRaises(ValueError):
            pack(structure=0, vic=1)

    def test_hdmi_forum_vsif_is_a_separate_generation(self):
        """Same InfoFrame type, different OUI: never read one as the other."""
        self.assertNotEqual(HDMI14_OUI, HDMI_FORUM_OUI)
        forum = bytearray(pack(0))
        forum[4:7] = HDMI_FORUM_OUI.to_bytes(3, "little")
        forum[3] = 0
        forum[3] = checksum(forum)
        self.assertEqual(sum(forum) % 256, 0, "control must fail on the OUI, not the checksum")
        with self.assertRaisesRegex(ValueError, "HDMI Forum"):
            unpack(bytes(forum))

    def test_frame_packing_rasters(self):
        """Two frames plus one 2D vertical blanking, at twice the pixel clock."""
        expected = {
            "1080p24 (VIC 32)": ((1920, 2205), 2250, 45),
            "720p60 (VIC 4)": ((1280, 1470), 1500, 30),
            "720p50 (VIC 19)": ((1280, 1470), 1500, 30),
        }
        for name, h, v, htotal, vtotal, refresh, clock in CTA_TIMINGS:
            with self.subTest(timing=name):
                self.assertEqual(htotal * vtotal * refresh, clock * 1000)
                packed = frame_packed(h, v, htotal, vtotal, clock)
                self.assertEqual((packed["active"], packed["vtotal"], packed["gap"]),
                                 expected[name])
                self.assertEqual(packed["active"][1], 2 * v + packed["gap"])
                self.assertEqual(htotal * packed["vtotal"] * refresh,
                                 packed["clock_khz"] * 1000)
                self.assertEqual(packed["clock_khz"], 148500)

    def test_guide_matches_the_arithmetic(self):
        if not GUIDE.exists():
            self.skipTest(f"{GUIDE} not found")
        guide = GUIDE.read_text(encoding="utf-8")
        self.assertIn("PB4 = 0x40", guide)
        for structure in (0, 6, 8):
            with self.subTest(structure=STRUCTURES[structure]):
                quoted = re.search(rf"\b{structure} {re.escape(STRUCTURES[structure])}\s*"
                                   r"\(PB5 = 0x([0-9A-F]{2})\)", guide)
                self.assertIsNotNone(quoted, "PB5 value not found in the guide")
                self.assertEqual(int(quoted.group(1), 16), structure << 4)
        for name, h, v, htotal, vtotal, refresh, clock in CTA_TIMINGS:
            packed = frame_packed(h, v, htotal, vtotal, clock)
            width, height = packed["active"]
            with self.subTest(timing=name):
                self.assertIn(f"{width} x {height}", guide)
                self.assertIn(f"VTOTAL {packed['vtotal']}", guide)
                self.assertIn(f"{packed['gap']} lines gap", guide)
        worked = re.findall(r"^[^:\n|]+:\s+((?:[0-9A-F]{2} ){7,9}[0-9A-F]{2})\s*$", guide, re.M)
        self.assertGreaterEqual(len(worked), 4, "worked packets missing from the guide")
        for row in worked:
            with self.subTest(worked_packet=row):
                packet = bytes.fromhex(row)
                self.assertEqual(sum(packet) % 256, 0)
                fields = unpack(packet)
                self.assertEqual(pack(**fields), packet)


if __name__ == "__main__":
    unittest.main(verbosity=2)
