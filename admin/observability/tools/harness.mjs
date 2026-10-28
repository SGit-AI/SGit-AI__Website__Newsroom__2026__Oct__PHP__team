// A dry-run host for the telemetry app: the app from the 5wnsr5h8 clone, the data from a COPY of the 84wr8mib clone,
// the lane's list and fetch from the real server (read-only calls), and NO publish and NO mark-processed: those two
// answer as if done and change nothing. For screenshots and checks of the Queue & drain page, not for draining.
import http from 'http'; import fs from 'fs'; import path from 'path'
const [UX, DATA, ENUM_FILE, PORT = '8790', SLOW = '0'] = process.argv.slice(2)
const ENUM = fs.readFileSync(ENUM_FILE, 'utf8').trim(), VID = '84wr8mib', API = 'https://dev.send.sgraph.ai/api/vault/append/'
const TYPES = { '.js': 'text/javascript', '.css': 'text/css', '.json': 'application/json', '.html': 'text/html' }
const inside = (root, p) => { const f = path.resolve(root, '.' + path.posix.normalize('/' + p)); if (!f.startsWith(path.resolve(root))) throw new Error('outside'); return f }
const body = req => new Promise(r => { let b = ''; req.on('data', c => b += c); req.on('end', () => r(b)) })
const sleep = ms => new Promise(r => setTimeout(r, ms))
http.createServer(async (req, res) => {
  try {
    const u = new URL(req.url, 'http://x'), send = (code, data, type) => { res.writeHead(code, { 'content-type': type || 'application/json' }); res.end(typeof data === 'string' || Buffer.isBuffer(data) ? data : JSON.stringify(data)) }
    if (u.pathname === '/') return send(200, fs.readFileSync(path.join(path.dirname(new URL(import.meta.url).pathname), 'harness.html.txt'), 'utf8'), 'text/html')
    if (u.pathname.startsWith('/ux/')) { const f = inside(UX, u.pathname.slice(4)); return send(200, fs.readFileSync(f), TYPES[path.extname(f)] || 'text/plain') }
    if (u.pathname === '/vfs/read') { const f = inside(DATA, u.searchParams.get('p')); return fs.existsSync(f) ? send(200, fs.readFileSync(f, 'utf8'), 'text/plain') : send(404, 'missing', 'text/plain') }
    if (u.pathname === '/vfs/list') { const d = inside(DATA, u.searchParams.get('p')); return send(200, fs.existsSync(d) ? fs.readdirSync(d).map(n => ({ path: '/' + path.posix.join(u.searchParams.get('p'), n), type: fs.statSync(path.join(d, n)).isDirectory() ? 'folder' : 'file' })) : []) }
    if (u.pathname === '/vfs/write') { const f = inside(DATA, u.searchParams.get('p')); fs.mkdirSync(path.dirname(f), { recursive: true }); fs.writeFileSync(f, await body(req)); return send(200, { ok: true }) }
    if (u.pathname === '/lane/list' || u.pathname === '/lane/fetch') {
      await sleep(+SLOW)
      const r = await fetch(API + u.pathname.slice(6) + '/' + VID, { method: 'POST', headers: { 'content-type': 'application/json', 'x-sgraph-vault-enum-key': ENUM }, body: await body(req) })
      return send(r.status, await r.text())
    }
    if (u.pathname === '/lane/mark-processed') { const b = JSON.parse(await body(req)); await sleep(+SLOW / 2); return send(200, { moved: b.file_ids, missing: [], dry_run: true }) }
    send(404, 'not here', 'text/plain')
  } catch (e) { res.writeHead(500); res.end(String(e.message)) }
}).listen(+PORT, () => console.log('harness on ' + PORT))
