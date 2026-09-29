# Stereo Camera Geometry, Parallax Budget, and Rigging Mathematics

This reference document details the geometric principles, interpupillary distance (IPD) calculations, parallax budget formulas, and camera rigging configurations used in stereoscopic 3D capture.

---

## 1. Geometric Optics of Binocular Disparity

Stereoscopic depth perception relies on horizontal disparity between the images captured by two offset lenses or cameras.

```
                         P (Target Object in 3D Space)
                        / \
                       /   \
                      /     \
                     /       \
                    /         \
                   /           \
                  /             \
                 /               \
                /                 \
        L1 (Left Lens)      L2 (Right Lens)
           |                       |
           +<-------- B ---------->+ (Baseline / Interpupillary Distance)
           |                       |
     Left Image Plane        Right Image Plane
      [--- x_L ---]           [--- x_R ---]
```

```mermaid
graph TD
    P((Target Object P)) --> L1[Left Lens L1]
    P --> L2[Right Lens L2]

    L1 --> ImgL[Left Image Plane x_L]
    L2 --> ImgR[Right Image Plane x_R]

    subgraph Disparity & Convergence
        L1 <---|Baseline B|---> L2
        ImgL --> Disp[Screen Disparity d = x_L - x_R]
        ImgR --> Disp
    end
```

---

## 2. Parallax Types and Screen Convergence

Parallax ($p$) is the distance between corresponding points of the left and right eye images on the display screen.

```
1. ZERO PARALLAX (Screen Plane)
   Left Eye Ray  \
                  +---> Point on Screen Surface (P_screen)
   Right Eye Ray /

2. NEGATIVE PARALLAX (In Front of Screen / Pop-Out)
   Left Eye Ray  ----\ /----
                      X  Point Appears in Space (P_popout)
   Right Eye Ray ----/ \----

3. POSITIVE PARALLAX (Behind Screen / Into Depth)
   Left Eye Ray  -----\
                       \  Point Appears Behind Screen (P_depth)
   Right Eye Ray ------/
```

```mermaid
block-beta
    columns 1
    block:popout
        P1["Negative Parallax (Pop-out): Left/Right rays cross in front of screen"]
    end
    block:zero
        P2["Zero Parallax Plane: Points converge exactly on display screen surface"]
    end
    block:depth
        P3["Positive Parallax (In-depth): Left/Right rays converge behind screen"]
    end

    style P1 fill:#f9d,stroke:#333
    style P2 fill:#dfd,stroke:#333
    style P3 fill:#ddf,stroke:#333
```

---

## 3. Mathematical Calculations for Camera Baseline

### 3.1 The 1/30th Rule (Rule of Thumb)

A traditional practical rule for natural depth:

$$
B = \frac{D_{\text{near}}}{30}
$$

Where:
- $B$ = Camera baseline (distance between lens centers)
- $D_{\text{near}}$ = Distance from camera to nearest subject in scene

### 3.2 Precise Parallax Budget Formula (Berkovitz Model)

To keep maximum screen parallax within comfortable human limits ($\le 2\% \text{ to } 3\%$ of screen width $W_{\text{screen}}$):

$$
p_{\text{max}} = W_{\text{sensor}} \cdot \frac{f \cdot B}{W_{\text{sensor}}} \cdot \left( \frac{1}{D_{\text{near}}} - \frac{1}{D_{\text{far}}} \right)
$$

Where:
- $f$ = Lens focal length
- $B$ = Interocular baseline
- $D_{\text{near}}$ = Near clipping distance
- $D_{\text{far}}$ = Far clipping distance

---

## 4. Camera Rigging Configurations

```
1. PARALLEL RIG WITH HIT (Horizontal Image Translation)
   L1 [ || ] <--- B ---> [ || ] L2
   - Optical axes are strictly parallel (no keystone distortion).
   - Convergence plane is set digitally in post via horizontal offset.

2. CONVERGED / TOE-IN RIG
   L1 [ // ] <--- B ---> [ \\ ] L2
   - Optical axes angle inward towards a focal point.
   - Causes vertical parallax at corners (keystone distortion) requiring correction.

3. BEAM-SPLITTER / MIRROR RIG
   Camera 1 (Shooting through 45-degree semi-silvered mirror)
      |
      V  [Mirror] ---> Camera 2 (Shooting reflection at 90 degrees)
   - Allows baseline B to be reduced below physical camera body width (B < 65mm).
```

```mermaid
graph TD
    A[Camera Rig Types] --> B[Parallel Rig + HIT]
    A --> C[Toe-in / Converged Rig]
    A --> D[Beam-Splitter / Mirror Rig]

    B --> B_Note[Zero Keystone distortion; convergence adjusted in post]
    C --> C_Note[Causes Keystone distortion; requires optical rectification]
    D --> D_Note[Allows sub-65mm baseline for close-up macro work]
```

---

## Summary Parameters Table

| Rig Type | Baseline Range | Distortions | Typical Usage |
| :--- | :--- | :--- | :--- |
| Side-by-Side Bar | $> 65\text{ mm}$ | Mild Hyperstereo | Landscapes, Distant subjects |
| Beam-Splitter | $0 - 65\text{ mm}$ | Reflection polarization mismatch | Close-ups, Close dialogue |
| Toe-In Rig | Variable | Keystone (Vertical Parallax) | Discouraged for modern production |

---

## References

- Lipton, Lenny. *Foundations of the Stereoscopic Cinema*, Van Nostrand Reinhold, 1982.
- Mendiburu, Bernard. *3D Movie Making: Stereoscopic Digital Cinema from Script to Screen*, Focal Press, 2009.
- Woods, Andrew. *"Distortions in Stereoscopic Displays"*, SPIE Proceedings, 1993.
