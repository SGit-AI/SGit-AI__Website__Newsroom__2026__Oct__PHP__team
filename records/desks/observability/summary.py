#!/usr/bin/env python3
"""The readers' executive summary: what the site's readers did today, the last drain, the days so far, and what looks
worth a look. Kept by observability@php.newsroom; printed in every scheduled wake's report (the editor, 27 October 2026).

Counts only. It prints no session id, no city or region, no row. Every event is an untrusted claim (the token and the key
are published), so every number is "what the events say", and the groups are the classifier's guesses
(telemetry_classes.py, from the press), declared where the browser declared.

    python -I summary.py --vault <telemetry vault clone> --classifier <folder holding telemetry_classes.py> [--day YYYY-MM-DD]
"""
import argparse, collections, datetime, glob, json, os, sys

BAR = 24


def bars(pairs, width=BAR):
    top = max([n for _, n in pairs] + [1])
    return '\n'.join(f'  {str(k)[:34]:<34} {"█" * max(1 if n else 0, round(width * n / top)):<{width}} {n}' for k, n in pairs)


def share(n, d):
    return f'{round(100 * n / d)}%' if d else '–'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--vault', required=True); ap.add_argument('--classifier', required=True); ap.add_argument('--day')
    a = ap.parse_args()
    sys.path.insert(0, a.classifier)
    import telemetry_classes as tc
    V = os.path.abspath(a.vault)
    rows = []
    for f in sorted(glob.glob(os.path.join(V, 'drain', '*.jsonl'))):
        for line in open(f, encoding='utf-8'):
            try: r = json.loads(line)
            except ValueError: continue
            if r.get('v') == 1 and not r.get('test') and r.get('_received') and r.get('sid'): rows.append(r)
    cls = tc.classify(rows)
    for r in rows:
        r['_c'] = cls[r['sid']][0]
        r['_t'] = datetime.datetime.fromtimestamp(r['_received'] / 1000, datetime.timezone.utc)
    day = a.day or max(r['_t'] for r in rows).strftime('%Y-%m-%d')
    T = [r for r in rows if r['_t'].strftime('%Y-%m-%d') == day]
    R = [r for r in T if r['_c'] == 'reader']
    latest = json.load(open(os.path.join(V, 'reports', 'latest.json')))
    N = int(latest.get('drained_now') or 0)
    last = sorted(rows, key=lambda r: r['_file'])[-N:] if N else []   # the file ids sort in arrival order
    top = lambda rs, k, n=6: collections.Counter(str(r.get(k) or '(none)') for r in rs).most_common(n)
    sessions = lambda rs: len({r['sid'] for r in rs})
    by_day = collections.defaultdict(collections.Counter); sess_day = collections.defaultdict(set)
    for r in rows:
        d = r['_t'].strftime('%m-%d'); by_day[d][r['_c']] += 1
        if r['_c'] == 'reader': sess_day[d].add(r['sid'])
    when = max(r['_t'] for r in T).strftime('%H:%M')
    out = []
    out.append(f'READERS: {day}, events up to {when} UTC (vault: {len(rows):,} events, {sessions(rows):,} sessions)')
    out.append(f'  today: {len(T)} events; readers {len(R)} views in {sessions(R)} sessions; synthetic {sum(1 for r in T if r["_c"] == "synthetic")}; '
               f'crawlers {sum(1 for r in T if r["_c"] == "crawler")}; the editor and team {sum(1 for r in T if r["_c"] in ("editor", "power-user"))}')
    if last:
        lr = [r for r in last if r['_c'] == 'reader']
        out.append(f'  last drain: {len(last)} events, {datetime.datetime.fromtimestamp(min(r["_received"] for r in last) / 1000, datetime.timezone.utc):%H:%M} to '
                   f'{datetime.datetime.fromtimestamp(max(r["_received"] for r in last) / 1000, datetime.timezone.utc):%H:%M} UTC; readers {len(lr)} views in {sessions(lr)} sessions')
    out.append('\nREADER VIEWS PER DAY (UTC; the last day is partial)')
    out.append(bars([(d, by_day[d]['reader']) for d in sorted(by_day)[-7:]]))
    out.append('\nWHAT READERS READ TODAY'); out.append(bars(top(R, 'path', 8)))
    out.append('\nWHERE THEY CAME FROM'); out.append(bars(top(R, 'ref', 6)))
    out.append('\nWHERE (COUNTRY), DEVICE'); out.append(bars(top(R, 'country', 6) + top(R, 'screen', 2)))
    hours = collections.Counter(r['_t'].strftime('%H') for r in R)
    out.append('\nREADER VIEWS BY HOUR (UTC)'); out.append('  ' + ' '.join(f'{h}:{hours[h]}' for h in sorted(hours)))
    # observations: only what the numbers say
    obs = []
    prev = sorted(d for d in by_day if d < day[5:])[-1:] if day[5:] in by_day else sorted(by_day)[-2:-1]
    if prev:
        p = prev[0]; obs.append(f'readers: {len(R)} views so far today against {by_day[p]["reader"]} on {p} in all ({len(sess_day[day[5:]])} sessions against {len(sess_day[p])})')
    ss = collections.defaultdict(list)
    for r in R: ss[r['sid']].append(r)
    internal = [r for r in R if str(r.get('ref') or '').endswith('newsroom.sgit.ai')]
    obs.append(f'a reader session is one tab on one host, so a move between the site, refs, updates and team starts a new session: '
               f'{len(internal)} of {len(R)} reader views came from one of our own hosts, yet only {sum(1 for v in ss.values() if len(v) > 1)} of {len(ss)} sessions read a second page here')
    G = [r for r in T if r['_c'] == 'crawler']
    obs.append(f'crawlers: {len(G)} events today over {len({r["path"] for r in G})} pages; {len({r["path"] for r in rows if r["_c"] == "crawler"}):,} different pages seen all time '
               f'(the re-crawl after the rebuild; {sum(1 for r in G if r.get("agent") == "googlebot")} of today\'s declare googlebot)')
    syn = sum(1 for r in T if r['_c'] == 'synthetic')
    obs.append(f'synthetic (agents\' and tests\' headless browsers): {syn} events, {share(syn, len(T))} of today\'s')
    ents = collections.Counter(sorted(v, key=lambda r: r['_received'])[0]['path'] for v in ss.values())
    if ents: obs.append('readers arrive mostly on: ' + ', '.join(f'{p} ({n})' for p, n in ents.most_common(3)))
    out.append('\nWORTH A LOOK'); out.extend('  - ' + o for o in obs)
    print('\n'.join(out))


if __name__ == '__main__':
    main()
