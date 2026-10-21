#!/usr/bin/env python3
"""Count consecutive weekly-scan failures per link.

Within one scan, lychee already retries a failing link with a growing wait.
Across scans, this keeps a history: a link that fails is counted once per scan,
and a link that passes again leaves the history, so its count starts over.
Only a link that fails OFFLINE_AFTER scans in a row is reported as offline;
fewer failures are listed in the job summary as possibly temporary.

usage: link_history.py LYCHEE_JSON PREVIOUS_HISTORY NEW_HISTORY ISSUE_BODY
"""
import datetime
import json
import os
import sys

OFFLINE_AFTER = 3


def failures(report):
    found = {}
    for key in ('error_map', 'timeout_map'):
        for source, entries in (report.get(key) or {}).items():
            for entry in entries:
                url = entry.get('url')
                if not url:
                    continue
                status = entry.get('status') or {}
                text = status.get('text', '') if isinstance(status, dict) else str(status)
                item = found.setdefault(url, {'status': (text or 'failed').replace('|', '\\|'), 'files': set()})
                item['files'].add(source.removeprefix('./'))
    return found


def table(links):
    rows = ['| Link | Failed scans in a row | Failing since | Last result | In |', '|---|---|---|---|---|']
    for url, v in sorted(links.items(), key=lambda kv: (-kv[1]['fails'], kv[0])):
        rows.append(f"| <{url}> | {v['fails']} | {v['since']} | {v['status']} | {', '.join(v['files'])} |")
    return '\n'.join(rows)


def main(report_path, previous_path, history_path, body_path):
    with open(report_path) as f:
        report = json.load(f)
    try:
        with open(previous_path) as f:
            previous = json.load(f)
    except (OSError, ValueError):
        previous = {}
    today = datetime.date.today().isoformat()

    history = {}
    for url, now in failures(report).items():
        old = previous.get(url, {})
        history[url] = {
            'fails': old.get('fails', 0) + 1,
            'since': old.get('since', today),
            'status': now['status'],
            'files': sorted(now['files']),
        }
    with open(history_path, 'w') as f:
        json.dump(history, f, indent=1, sort_keys=True)

    offline = {u: v for u, v in history.items() if v['fails'] >= OFFLINE_AFTER}
    temporary = {u: v for u, v in history.items() if v['fails'] < OFFLINE_AFTER}

    body = [f'# Links offline for {OFFLINE_AFTER} weekly scans in a row', '',
        f'Each failing link was retried after 30, 60 and 120 seconds in every scan. Updated {today}.', '']
    body.append(table(offline) if offline else 'None.')
    with open(body_path, 'w') as f:
        f.write('\n'.join(body) + '\n')

    summary = [f"Checked {report.get('total', 0)} links: {len(offline)} offline, {len(temporary)} possibly temporary.", '']
    if offline:
        summary += ['## Offline', '', table(offline), '']
    if temporary:
        summary += ['## Possibly temporary (counted again next scan, cleared when they pass)', '', table(temporary), '']
    if os.environ.get('GITHUB_STEP_SUMMARY'):
        with open(os.environ['GITHUB_STEP_SUMMARY'], 'a') as f:
            f.write('\n'.join(summary) + '\n')
    else:
        print('\n'.join(summary))
    if os.environ.get('GITHUB_OUTPUT'):
        with open(os.environ['GITHUB_OUTPUT'], 'a') as f:
            f.write(f'offline={len(offline)}\n')


if __name__ == '__main__':
    if len(sys.argv) != 5:
        sys.exit(__doc__)
    main(*sys.argv[1:])
