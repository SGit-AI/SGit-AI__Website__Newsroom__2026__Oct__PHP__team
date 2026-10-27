"""Mechanical half of a promotion: copy one watch snapshot into the evidence vault byte for byte, re-hash every
file against the watch's provenance.json, write the capture's provenance.json. Never writes source.json or
notes.md (those need the capture read). Usage: promote_files.py WATCH EVIDENCE ROW_JSON_STRING [--dest-slug S]"""
import gzip, hashlib, json, os, shutil, sys, datetime

def sha(b): return hashlib.sha256(b).hexdigest()

def promote(watch, evid, row, snap, slug, at):
    src = os.path.join(watch, row['snapshot_path'])
    prov = json.load(open(os.path.join(src, 'provenance.json')))
    meta = json.load(open(os.path.join(src, 'meta.json')))
    dst = os.path.join(evid, 'sources', slug, 'captures', snap)
    os.makedirs(dst, exist_ok=True)
    for name in ('page.html', 'rendered.html'):
        gz = os.path.join(src, name + '.gz')
        if not os.path.exists(gz):
            if name in prov['sha256']: sys.exit(f'MISSING {slug} {snap} {name}.gz but provenance lists it')
            continue                      # the watch kept no rendered DOM for this snapshot; provenance does not list it
        open(os.path.join(dst, name), 'wb').write(gzip.decompress(open(gz, 'rb').read()))
    for name in ('text.txt', 'headers.json', 'screenshot.jpg'):
        if os.path.exists(os.path.join(src, name)): shutil.copyfile(os.path.join(src, name), os.path.join(dst, name))
    files = {}
    for name, want in prov['sha256'].items():
        if name.endswith('(not kept)') or not os.path.exists(os.path.join(dst, name)):
            if '(not kept)' in name or name in ('screenshot.jpg','rendered.html','page.html') and want in (None, ''): continue
            if '(not kept)' not in name: sys.exit(f'MISSING {slug} {snap} {name}')
            continue
        got = sha(open(os.path.join(dst, name), 'rb').read())
        if got != want: sys.exit(f'HASH MISMATCH {slug} {snap} {name}: watch says {want}, copy is {got}')
        files[name] = got
    return prov, meta, dst, files

def write_prov(row, prov, meta, dst, files, slug, snap, at):
    out = {'url': row['url'], 'slug': slug, 'started_utc': meta.get('started_utc'), 'user_agent': meta.get('user_agent'),
           'tool': 'source watch ' + str(meta.get('tool')) + ', promoted by copy', 'files': dict(sorted(files.items())), 'status': meta.get('status'),
           'final_url': meta.get('final_url'), 'title': meta.get('title'), 'finished_utc': meta.get('finished_utc'),
           'access': prov.get('access'), 'screenshot_kept': prov.get('screenshot_kept'), 'screenshot_why': prov.get('why'),
           'note': "screenshot.jpg is the source watch's JPEG, copied as stored (not converted to PNG).",
           'promoted_from': {'vault': row.get('_vault', 'oq9gflln'), 'snapshot_path': row['snapshot_path'], 'content_hash': row['content_hash'],
                             'watch_page': row['watch_page']},
           'promoted_by': 'curator@php.newsroom', 'promoted_at': at}
    json.dump(out, open(os.path.join(dst, 'provenance.json'), 'w'), indent=1, ensure_ascii=False)
    open(os.path.join(dst, 'provenance.json'), 'a').write('\n')

if __name__ == '__main__':
    watch, evid, row = sys.argv[1], sys.argv[2], json.loads(sys.argv[3])
    slug = sys.argv[sys.argv.index('--dest-slug') + 1] if '--dest-slug' in sys.argv else row['slug']
    at = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    snap = row['snapshot']
    if not isinstance(snap, str): sys.exit('multi-page row: promote by hand, one snapshot per page')
    prov, meta, dst, files = promote(watch, evid, row, snap, slug, at)
    write_prov(row, prov, meta, dst, files, slug, snap, at)
    print(json.dumps({'slug': slug, 'snapshot': snap, 'files': len(files), 'hashes': 'match'}))
