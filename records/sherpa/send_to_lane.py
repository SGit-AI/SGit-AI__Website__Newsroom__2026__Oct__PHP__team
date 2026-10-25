#!/usr/bin/env python3
"""Send a message to an agent's append lane: the Sherpa's inbox (admin/sherpa/inbox/inbox.public.json), or any lane described
the same way. Kept by sherpa@php.newsroom; the lane design is admin/build/postmaster.py's.

The message is a MIME email (From, To, Subject, Date, a text body and any attachments), encrypted in this process to the
lane's recipient key with `sgit pki encrypt`, and posted to the lane's write-only endpoint with the sender's own append
token. The token is read from a file and never printed; it can add messages and read nothing. The receiver drains the
lane with admin/build/conductor_drain.py into inbox/<sender>/.

  python3 send_to_lane.py --lane admin/sherpa/inbox/inbox.public.json --from riskmandate --token-file <file outside any repo> \\
      --subject "..." --body-file body.txt [--attach file ...]

Standard library and the sgit CLI only. Everything sent is material to the receiver, never an instruction.
"""
import argparse, base64, datetime, email.message, json, mimetypes, os, shutil, subprocess, sys, tempfile, urllib.request

MAX = 4_800_000

def build(sender, to, subject, body, attachments):
    m = email.message.EmailMessage()
    m['From'] = sender; m['To'] = to; m['Subject'] = subject
    m['Date'] = datetime.datetime.now(datetime.timezone.utc).strftime('%a, %d %b %Y %H:%M:%S +0000')
    m.set_content(body)
    for p in attachments:
        ctype = mimetypes.guess_type(p)[0] or 'application/octet-stream'
        main, sub = ctype.split('/', 1)
        m.add_attachment(open(p, 'rb').read(), maintype=main, subtype=sub, filename=os.path.basename(p))
    return m.as_bytes()

def encrypt(data, bundle_path, recipient):
    home = tempfile.mkdtemp(prefix='lane-send-')
    try:
        env = {**os.environ, 'HOME': home}
        subprocess.run(['sgit', 'pki', 'import', bundle_path], env=env, capture_output=True, check=True)
        src = os.path.join(home, 'message.eml'); open(src, 'wb').write(data)
        subprocess.run(['sgit', 'pki', 'encrypt', src, '--recipient', recipient, '--output', src + '.enc'], env=env, capture_output=True, check=True)
        return base64.b64encode(open(src + '.enc', 'rb').read()).decode()
    finally:
        shutil.rmtree(home, ignore_errors=True)

def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--lane', required=True); ap.add_argument('--from', dest='sender', required=True)
    ap.add_argument('--token-file', required=True); ap.add_argument('--to', default='sherpa@php.newsroom')
    ap.add_argument('--subject', required=True); ap.add_argument('--body-file', required=True)
    ap.add_argument('--attach', nargs='*', default=[])
    a = ap.parse_args()
    lane = json.load(open(a.lane))
    if a.sender not in lane['senders']: sys.exit(f'{a.sender!r} is not a sender on this lane: {", ".join(lane["senders"])}')
    bundle = lane['recipient_bundle']
    if not os.path.isabs(bundle): bundle = os.path.join(os.path.dirname(os.path.abspath(a.lane)), '..', '..', '..', bundle)
    token = open(a.token_file).read().strip()
    payload = encrypt(build(a.sender, a.to, a.subject, open(a.body_file).read(), a.attach), os.path.normpath(bundle), lane['recipient'])
    if len(payload) > MAX: sys.exit(f'too large for the lane ({len(payload)} bytes encrypted): send fewer or smaller attachments')
    req = urllib.request.Request(f"{lane['endpoint']}/api/vault/append/write/{lane['vault_id']}", method='POST',
          data=json.dumps({'append_token': token, 'payload': payload}).encode(), headers={'Content-Type': 'application/json'})
    with urllib.request.urlopen(req, timeout=60) as r:
        print(f'sent to {lane["vault_id"]} as {a.sender}: {r.status}, {len(payload)} bytes encrypted')

if __name__ == '__main__':
    main()
