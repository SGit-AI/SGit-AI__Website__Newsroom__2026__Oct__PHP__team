// Integration test for <sg-graph> in real Chromium against the locally served site. No mocks.
import { createRequire } from 'module'
const require = createRequire('/opt/node22/lib/node_modules/')
let pw
try { pw = require('playwright') } catch { pw = require('playwright') }
const BASE = (process.env.BASE || 'http://127.0.0.1:8766/')
const SHOTS = process.argv[2]
const results = []
const check = (name, ok, info = '') => { results.push({ name, ok, info }); console.log(`${ok ? 'PASS' : 'FAIL'} ${name}${info ? ' :: ' + info : ''}`) }

const browser = await pw.chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' }).catch(() => pw.chromium.launch())
async function open(path, width, scheme = 'light') {
    const ctx = await browser.newContext({ viewport: { width, height: 900 }, colorScheme: scheme, deviceScaleFactor: 1 })
    const page = await ctx.newPage()
    const errors = []
    // the site's telemetry asks an outside geolocation service, which CORS blocks on localhost; only errors from this site count
    page.on('console', m => { if (m.type() === 'error' && !/ipapi\.co|ipwho\.is/.test(m.text() + (m.location().url || '')) && (m.location().url || BASE).startsWith(BASE)) errors.push(m.text() + ' @ ' + (m.location().url || '')) })
    page.on('pageerror', e => errors.push(String(e)))
    await page.goto(BASE + path)
    await page.waitForFunction(() => [...document.querySelectorAll('sg-graph')].every(g => g.dataset.state), null, { timeout: 15000 })
    return { ctx, page, errors }
}
const shadow = (page, sel, fn, idx = 0) => page.evaluate(([sel, fn, idx]) => { const g = document.querySelectorAll('sg-graph')[idx]; return new Function('root', 'el', fn)(g.shadowRoot, g) }, [sel, fn, idx])

// 1. the story graph at desktop width
{
    const { ctx, page, errors } = await open('graph/index.html', 1280)
    const state = await page.$eval('sg-graph', g => g.dataset.state + ' ' + (g.dataset.error || ''))
    check('graph page: component ready', state.startsWith('ready'), state)
    const m = await shadow(page, '', `const G = el.model; return { n: G.nodes.length, e: G.edges.length, verbs: new Set(G.edges.map(x => x.verb)).size, focus: el.shadowRoot.querySelector('.n.focus')?.getAttribute('aria-label'), drawn: root.querySelectorAll('svg .n').length, links: root.querySelectorAll('.list a.page').length }`)
    check('model loaded with >= 4 verbs', m.verbs >= 4, JSON.stringify(m))
    check('focus is the 70% claim', /70%/.test(m.focus || ''), m.focus)
    const noHref = await shadow(page, '', `return el.model.nodes.filter(n => !n.href).map(n => n.id).slice(0, 5)`)
    check('every node has a page (href)', noHref.length === 0, noHref.join(','))
    await page.locator('sg-graph').first().screenshot({ path: `${SHOTS}/graph-1280.png` })
    // walk: click a party in the drawing (Wiz), the graph re-centres
    await page.evaluate(() => { const r = document.querySelector('sg-graph').shadowRoot; [...r.querySelectorAll('svg .n')].find(g => /Party: Wiz/.test(g.getAttribute('aria-label'))).dispatchEvent(new MouseEvent('click', { bubbles: true })) })
    const f2 = await shadow(page, '', `return root.querySelector('.n.focus').getAttribute('aria-label')`)
    check('click walks to Wiz', /Wiz/.test(f2), f2)
    const trail = await shadow(page, '', `return root.querySelector('[data-role=trail]').textContent`)
    check('trail records the walk', /70%/.test(trail), trail.slice(0, 80))
    // keyboard: tab to a node and press Enter
    await page.evaluate(() => { const r = document.querySelector('sg-graph').shadowRoot; [...r.querySelectorAll('svg .n')].find(g => !g.classList.contains('focus')).focus() })
    const before = await shadow(page, '', `return root.querySelector('.n.focus').getAttribute('aria-label')`)
    await page.keyboard.press('Enter')
    const after = await shadow(page, '', `return root.querySelector('.n.focus').getAttribute('aria-label')`)
    check('Enter on a node walks to it and keeps keyboard focus', before !== after && await shadow(page, '', `return root.activeElement?.classList.contains('focus') || false`), after)
    // path: how is Wiz connected to the BBC
    const p = await page.evaluate(() => { const g = document.querySelector('sg-graph'); g.focusOn('party:wiz'); const r = g.pathTo('party:bbc'); return r && r.nodes.map(n => n.label) })
    const ptext = await shadow(page, '', `return root.querySelector('ol.path')?.textContent || ''`)
    check('path Wiz to BBC found and read as a sentence', !!p && /states|relay/.test(ptext), ptext.slice(0, 160))
    await page.locator('sg-graph').first().screenshot({ path: `${SHOTS}/graph-path-1280.png` })
    // fractal: open the CVE node's inner graph (another vocabulary)
    await page.evaluate(() => document.querySelector('sg-graph').focusOn('claim:two-cves-9.2'))
    const hasCve = await shadow(page, '', `return el.core.neighbours(el.model, 'claim:two-cves-9.2').some(r => r.other.kind === 'cve' && r.other.zoom.length > 0)`)
    check('a claim is one link from a CVE that opens a graph', hasCve)
    await page.evaluate(() => document.querySelector('sg-graph').focusOn('cve:CVE-2026-109618'))
    await page.evaluate(() => document.querySelector('sg-graph').shadowRoot.querySelector('.zoomin').click())
    await page.waitForFunction(() => document.querySelector('sg-graph').model.byId.has('fix-commit'), null, { timeout: 5000 })
    const inner = await shadow(page, '', `const G = el.model; return { focus: root.querySelector('.n.focus')?.getAttribute('aria-label'), verbs: [...new Set(G.edges.map(e => e.verb))].join(','), trail: root.querySelector('[data-role=trail]').textContent }`)
    const det = await shadow(page, '', `return root.querySelector('[data-role=detail]').textContent + root.querySelector('[data-role=foot]').textContent`)
    check('detail panel shows text, not [object ...]', !/\[object /.test(det), det.slice(0, 120))
    check('review graph has no dangling edges', !/left out/.test(det), det.slice(-90))
    check('zoom opens the code-review graph in its own vocabulary', /touches|realised in/.test(inner.verbs), JSON.stringify(inner).slice(0, 200))
    await page.locator('sg-graph').first().screenshot({ path: `${SHOTS}/graph-zoom-1280.png` })
    await page.evaluate(() => document.querySelector('sg-graph').shadowRoot.querySelector('.trail .up').click())
    const back = await shadow(page, '', `return el.model.byId.has('claim:two-cves-9.2')`)
    check('trail leads back out of the zoom', back)
    for (const v of ['layers', 'map', 'list']) {
        await page.evaluate(v => document.querySelector('sg-graph').setAttribute('view', v), v)
        const drawn = await shadow(page, '', `return root.querySelectorAll('svg .n').length`)
        check(`view ${v} renders`, v === 'list' ? true : drawn > 0, `${drawn} nodes drawn`)
        await page.locator('sg-graph').first().screenshot({ path: `${SHOTS}/graph-${v}-1280.png` })
    }
    // tokens: every custom property the component reads resolves on the page (a broken token drew a node black once)
    const css = await (await fetch(BASE + 'assets/components/sg-graph/v1/v1.0/v1.0.0/sg-graph.css')).text()
    const toks = [...new Set([...css.matchAll(/var\((--[a-z0-9-]+)/g)].map(m => m[1]))]
    const unset = await page.evaluate(ts => ts.filter(t => !getComputedStyle(document.documentElement).getPropertyValue(t).trim()), toks)
    check('every token the component uses resolves', unset.length === 0, `${toks.length} tokens; unset: ${unset.join(',')}`)
    // bridges: a CVE opens two graphs; a party steps into the risk graph and reads its own inverses
    const z = await shadow(page, '', `const n = el.model.byId.get('cve:CVE-2026-109618'); return n.zoom.map(z => z.graph)`)
    check('a CVE opens the code-review and the risk graph', z.includes('data/review.json') && z.includes('data/grc-graph.json'), z.join(','))
    await page.evaluate(() => { const g = document.querySelector('sg-graph'); g.setAttribute('view', 'ego'); g.focusOn('party:cloudflare') })
    await page.evaluate(() => [...document.querySelector('sg-graph').shadowRoot.querySelectorAll('.zoomin')].find(b => /risk graph/.test(b.textContent)).click())
    await page.waitForFunction(() => document.querySelector('sg-graph').model.byId.has('stakeholder:waf-vendors'), null, { timeout: 5000 })
    const rg = await shadow(page, '', `const G = el.model; return { focus: root.querySelector('.n.focus')?.getAttribute('aria-label'), phrases: [...new Set(el.core.neighbours(G, 'stakeholder:waf-vendors').map(r => r.phrase))].join('|') }`)
    check('a party steps into the risk graph, focused on its stakeholder class', /WAF vendors/.test(rg.focus || ''), rg.focus)
    check('the risk graph reads its own inverses, not arrows', rg.phrases.length > 0 && !/←/.test(rg.phrases), rg.phrases)
    await page.evaluate(() => document.querySelector('sg-graph').shadowRoot.querySelector('.trail .up').click())
    // a zoom to another site is refused and nothing is fetched from it
    const hits = []
    page.on('request', r => { if (!r.url().startsWith(BASE)) hits.push(r.url()) })
    await page.evaluate(() => { const g = document.querySelector('sg-graph'); const n = g.model.byId.get('party:wiz'); g._zoom(n, { graph: 'https://example.com/graph.json', focus: 'x' }) })
    await page.waitForTimeout(300)
    const foot = await shadow(page, '', `return root.querySelector('[data-role=foot]').textContent`)
    check('a zoom to another site is refused', /not this site/.test(foot) && !hits.some(u => u.includes('example.com')), foot)
    // review findings, kept as regressions
    await page.evaluate(() => { const g = document.querySelector('sg-graph'); g.setAttribute('view', 'ego'); g.focusOn('claim:scale-70pc-internet') })
    await page.evaluate(() => [...document.querySelector('sg-graph').shadowRoot.querySelectorAll('.chip')].find(c => c.dataset.verb === 'cites').focus())
    await page.keyboard.press('Space')
    const chipKept = await shadow(page, '', `return root.activeElement?.dataset.verb || null`)
    check('a chip keeps the keyboard after toggling', chipKept === 'cites', String(chipKept))
    const pub = await page.evaluate(() => { const g = document.querySelector('sg-graph'); g.focusOn('party:wiz'); return g.core.neighbours(g.model, 'party:wiz', g._filter).map(r => r.edge.verb) })
    check('hiding cites at a claim keeps a party\'s other verbs', pub.includes('published_by') && pub.includes('states') && !pub.includes('cites'), [...new Set(pub)].join(','))
    const hidden = await page.evaluate(() => { const g = document.querySelector('sg-graph'); return [...g._filter.hide] })
    check('the hidden set is exactly the verb toggled', hidden.length === 1 && hidden[0] === 'cites', hidden.join(','))
    await page.evaluate(() => document.querySelector('sg-graph').focusOn('cve:CVE-2026-109618'))
    await page.evaluate(() => document.querySelector('sg-graph').shadowRoot.querySelector('.zoomin').click())
    await page.waitForFunction(() => document.querySelector('sg-graph').model.byId.has('fix-commit'), null, { timeout: 5000 })
    const innerHide = await page.evaluate(() => [...document.querySelector('sg-graph')._filter.hide])
    check('an inner graph starts with no hidden verbs', innerHide.length === 0, innerHide.join(','))
    await page.evaluate(() => document.querySelector('sg-graph').shadowRoot.querySelector('.trail .up').click())
    const restored = await page.evaluate(() => [...document.querySelector('sg-graph')._filter.hide])
    check('leaving the inner graph restores the outer filter', restored.join(',') === 'cites', restored.join(','))
    await page.evaluate(() => { const g = document.querySelector('sg-graph'); g._filter.hide.clear(); g.focusOn('party:wiz'); g.pathTo('party:wiz') })
    const self = await shadow(page, '', `return root.querySelector('.path')?.textContent || ''`)
    check('a path to the node in focus says so', /node in focus/.test(self), self)
    check('graph page: no console errors', errors.length === 0, errors.join(' | ').slice(0, 300))
    await ctx.close()
}

// 2. phone width, dark: label size in real pixels
{
    const { ctx, page, errors } = await open('graph/index.html', 390, 'dark')
    const sizes = await shadow(page, '', `const svg = root.querySelector('svg'); const scale = svg.getBoundingClientRect().width / svg.viewBox.baseVal.width; return [...root.querySelectorAll('svg .n text')].map(t => parseFloat(getComputedStyle(t).fontSize) * scale)`)
    const min = Math.min(...sizes)
    check('labels at least 12px at 390', sizes.length > 0 && min >= 11.99, `${sizes.length} labels, min ${min.toFixed(2)}px`)
    const overflow = await page.evaluate(() => document.documentElement.scrollWidth - window.innerWidth)
    check('no horizontal scroll at 390', overflow <= 0, `overflow ${overflow}px`)
    await page.locator('sg-graph').first().screenshot({ path: `${SHOTS}/graph-390-dark.png` })
    check('390 dark: no console errors', errors.length === 0, errors.join(' | ').slice(0, 300))
    await ctx.close()
}

// 3. the component page: inline data, review.json in layers, the parties page
for (const path of ['graph/component/index.html', 'graph/parties/index.html']) {
    const { ctx, page, errors } = await open(path, 1280)
    const states = await page.$$eval('sg-graph', gs => gs.map(g => g.dataset.state + (g.dataset.error ? ':' + g.dataset.error : '')))
    check(`${path}: every component ready`, states.every(s => s === 'ready'), states.join(','))
    check(`${path}: no console errors`, errors.length === 0, errors.join(' | ').slice(0, 300))
    await page.screenshot({ path: `${SHOTS}/${path.split('/')[1]}-1280.png`, fullPage: true })
    await ctx.close()
}

// 3b. an empty graph says so instead of failing
{
    const ctx = await browser.newContext(); const page = await ctx.newPage()
    await page.goto(BASE + 'graph/component/index.html')
    await page.evaluate(() => { const el = document.createElement('sg-graph'); el.innerHTML = '<script type="application/json">{"nodes":[],"edges":[]}<\/script>'; document.body.append(el) })
    await page.waitForFunction(() => document.querySelectorAll('sg-graph')[2]?.dataset.state, null, { timeout: 5000 })
    const st = await page.evaluate(() => document.querySelectorAll('sg-graph')[2].dataset.state)
    check('an empty graph renders, not fails', st === 'ready', st)
    await ctx.close()
}

// 4. without JavaScript the fallback shows
{
    const ctx = await browser.newContext({ javaScriptEnabled: false, viewport: { width: 390, height: 800 } })
    const page = await ctx.newPage()
    await page.goto(BASE + 'graph/index.html')
    const txt = await page.$eval('sg-graph', g => g.innerText)
    check('no-JS fallback is visible with links', /needs JavaScript/.test(txt) && (await page.$$('sg-graph a')).length >= 5, txt.slice(0, 80))
    await ctx.close()
}

await browser.close()
const failed = results.filter(r => !r.ok)
console.log(`\n${results.length - failed.length}/${results.length} passed`)
process.exit(failed.length ? 1 : 0)
