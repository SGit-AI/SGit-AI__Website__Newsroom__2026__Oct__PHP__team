# The ontologist's Chromium tests (kept from the session that wrote the component)

Run against a built box (the press's `tools/build.sh --make`, then its build), served locally:

    cd <box> && python3 -m http.server 8766 &
    BASE=http://127.0.0.1:8766/ NODE_PATH=$(npm root -g) node wikipedia.test.mjs   # 23 checks: the Wikipedia pages and graph
    BASE=http://127.0.0.1:8766/ node sg-graph.test.mjs                              # 37 checks: the component
    BOX=<box> node core.test.mjs                                                    # the component's pure core on the story graph

Playwright is pre-installed in the cloud sessions; `createRequire('/opt/node22/lib/node_modules/')` finds it. The tests
were last run green on 27 October 2026 against the component v1.0.1, including the case the new design creates (the line
moves the address bar to a view, so a page's relative addresses must resolve against `window.P2S_BASE`).
