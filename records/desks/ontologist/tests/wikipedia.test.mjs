// The Wikipedia section in real Chromium against the locally served site. No mocks.
import { createRequire } from 'module'
const require = createRequire('/opt/node22/lib/node_modules/')
const pw = require('playwright')
const BASE = (process.env.BASE || 'http://127.0.0.1:8766/')
const SHOTS = process.argv[2]
const results = []
const check = (name, ok, info = '') => { results.push({ name, ok }); console.log(`${ok ? 'PASS' : 'FAIL'} ${name}${info ? ' :: ' + info : ''}`) }
const browser = await pw.chromium.launch()
async function open(path, width = 1280, scheme = 'light') {
    const ctx = await browser.newContext({ viewport: { width, height: 900 }, colorScheme: scheme })
    const page = await ctx.newPage()
    const errors = []
    page.on('console', m => { if (m.type() === 'error' && (m.location().url || BASE).startsWith(BASE) && !/ipapi|ipwho/.test(m.text())) errors.push(m.text()) })
    page.on('pageerror', e => errors.push(String(e)))
    await page.goto(BASE + path)
    await page.waitForFunction(() => [...document.querySelectorAll('sg-graph')].every(g => g.dataset.state), null, { timeout: 20000 })
    return { ctx, page, errors }
}
const shadow = (page, fn) => page.evaluate(fn => { const g = document.querySelector('sg-graph'); return new Function('root', 'el', fn)(g.shadowRoot, g) }, fn)

{   // the article page: the graph loads in its own vocabulary, and a zoom leads out to the story graph
    const { ctx, page, errors } = await open('wikipedia/php2shell/index.html')
    const st = await page.$eval('sg-graph', g => g.dataset.state + ' ' + (g.dataset.error || ''))
    check('article graph ready', st.startsWith('ready'), st)
    const m = await shadow(page, `const G = el.model; return { n: G.nodes.length, verbs: [...new Set(G.edges.map(e => e.verb))].sort().join(','), focus: root.querySelector('.n.focus')?.getAttribute('aria-label'), inv: G.ontology.verbs.cites?.inverse }`)
    check('focus is the article, verbs are the scope\'s', /Article/.test(m.focus || '') && /has_section|revises/.test(m.verbs), JSON.stringify(m).slice(0, 200))
    check('inverses come from the scope', m.inv === 'cited by', String(m.inv))
    await page.evaluate(() => { const g = document.querySelector('sg-graph'); const ref = g.model.nodes.find(n => n.kind === 'reference' && g.core.neighbours(g.model, n.id).some(r => r.edge.verb === 'captured_as')); g.focusOn(ref.id); const src = g.core.neighbours(g.model, ref.id).find(r => r.edge.verb === 'captured_as').other; g.focusOn(src.id) })
    const z = await shadow(page, `return [...root.querySelectorAll('.zoomin')].map(b => b.textContent)`)
    check('a captured reference\'s source offers a zoom into the story graph', z.some(t => /story graph/.test(t)), z.join(' | '))
    await page.evaluate(() => [...document.querySelector('sg-graph').shadowRoot.querySelectorAll('.zoomin')].find(b => /story graph/.test(b.textContent)).click())
    await page.waitForFunction(() => document.querySelector('sg-graph').model.byId.has('claim:scale-70pc-internet'), null, { timeout: 8000 })
    const f = await shadow(page, `return root.querySelector('.n.focus')?.getAttribute('aria-label')`)
    check('the zoom lands on the same source in the story graph', /Source:/.test(f || ''), f)
    await page.locator('sg-graph').first().screenshot({ path: `${SHOTS}/wiki-article-1280.png` })
    check('article page: no console errors', errors.length === 0, errors.join(' | ').slice(0, 200))
    await ctx.close()
}
{   // the story graph: the Wikipedia source node zooms into the article's graph
    const { ctx, page } = await open('graph/index.html')
    await page.evaluate(() => document.querySelector('sg-graph').focusOn('source:wikipedia-php2shell'))
    const z = await shadow(page, `return [...root.querySelectorAll('.zoomin')].map(b => b.textContent)`)
    check('the article\'s source node zooms inside the article', z.some(t => /Inside the article/.test(t)), z.join(' | '))
    await page.evaluate(() => [...document.querySelector('sg-graph').shadowRoot.querySelectorAll('.zoomin')].find(b => /Inside the article/.test(b.textContent)).click())
    await page.waitForFunction(() => document.querySelector('sg-graph').model.byId.has('article:php2shell'), null, { timeout: 8000 })
    const f = await shadow(page, `return { focus: root.querySelector('.n.focus')?.getAttribute('aria-label'), trail: root.querySelector('[data-role=trail]').textContent }`)
    check('inside: focus is the article, trail leads back', /Article:/.test(f.focus || '') && /↑/.test(f.trail), JSON.stringify(f).slice(0, 160))
    await ctx.close()
}
{   // statements, references and history pages: every statement has a class, every reference a row, every revision an entry; phone width is fine
    for (const [path, sel, min] of [['wikipedia/php2shell/statements/index.html', 'li.wst', 30], ['wikipedia/php2shell/references/index.html', 'span[id^="r-"]', 40], ['wikipedia/php2shell/history/index.html', 'ol.whistory > li', 300]]) {
        const { ctx, page, errors } = await open(path, 390, 'dark')
        const n = await page.$$eval(sel, els => els.length)
        const over = await page.evaluate(() => document.documentElement.scrollWidth - window.innerWidth)
        check(`${path.split('/')[2]}: ${n} entries, no horizontal scroll at 390`, n >= min && over <= 0, `${n} entries, overflow ${over}px`)
        check(`${path.split('/')[2]}: no console errors`, errors.length === 0, errors.join(' | ').slice(0, 200))
        if (sel === 'li.wst') {
            const noClass = await page.$$eval('li.wst', els => els.filter(e => !e.querySelector('.st')).length)
            const objs = await page.evaluate(() => /\[object /.test(document.body.innerText))
            check('every statement carries a class pill and no [object]', noClass === 0 && !objs, `${noClass} without`)
            await page.screenshot({ path: `${SHOTS}/wiki-statements-390.png` })
        }
        await ctx.close()
    }
}
{   // the evolution and talk pages: the lifelines draw, the threads parse, phone width holds
    for (const [path, sel, min] of [['wikipedia/php2shell/evolution/index.html', '.wevo rect.life', 100], ['wikipedia/php2shell/talk/index.html', 'li.wpost', 15]]) {
        const { ctx, page, errors } = await open(path, 390, 'dark')
        const n = await page.$$eval(sel, els => els.length)
        const over = await page.evaluate(() => document.documentElement.scrollWidth - window.innerWidth)
        check(`${path.split('/')[2]}: ${n} entries, no horizontal scroll at 390`, n >= min && over <= 0, `${n}, overflow ${over}px`)
        check(`${path.split('/')[2]}: no console errors`, errors.length === 0, errors.join(' | ').slice(0, 200))
        await ctx.close()
    }
    const { ctx, page } = await open('wikipedia/php2shell/evolution/index.html', 1280)
    const t = await page.$eval('.wevo rect.life', r => r.querySelector('title').textContent)
    check('a lifeline names its class and dates', /(record|stated|attributed|quote|hedged), (removed|still)/.test(t), t.slice(0, 100))
    await page.locator('.wevo').screenshot({ path: `${SHOTS}/wiki-evolution-1280.png` })
    await ctx.close()
    const g = await open('wikipedia/php2shell/index.html', 1280)
    const chain = await g.page.evaluate(() => { const el = document.querySelector('sg-graph'); const G = el.model; const r = G.nodes.find(n => n.kind === 'revision'); return el.core.neighbours(G, r.id).map(x => x.phrase).sort().join(',') })
    check('a revision is walkable: follows, followed by, made by, revises', /follows|followed by/.test(chain) && /made by/.test(chain), chain)
    const th = await g.page.evaluate(() => { const el = document.querySelector('sg-graph'); return el.model.nodes.filter(n => n.kind === 'thread').length })
    check('the talk threads are in the graph', th >= 8, String(th))
    await g.ctx.close()
}
{   // the fallback without JavaScript
    const ctx = await browser.newContext({ javaScriptEnabled: false }); const page = await ctx.newPage()
    await page.goto(BASE + 'wikipedia/php2shell/index.html')
    const txt = await page.$eval('sg-graph', g => g.innerText)
    check('no-JS fallback names the three subpages', /every statement/i.test(txt) && (await page.$$('sg-graph a')).length >= 3, txt.slice(0, 80))
    await ctx.close()
}
await browser.close()
const failed = results.filter(r => !r.ok)
console.log(`\n${results.length - failed.length}/${results.length} passed`)
process.exit(failed.length ? 1 : 0)
