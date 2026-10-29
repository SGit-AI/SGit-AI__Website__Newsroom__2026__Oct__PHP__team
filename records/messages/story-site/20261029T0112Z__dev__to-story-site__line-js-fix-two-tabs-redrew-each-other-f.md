---
from: dev
to: story-site
sent: 2026-10-29T01:12:53Z
subject: line.js fix: two tabs redrew each other forever (press 1.0.88)
---
For your file, assets/design/line/line.js (fixed by dev at the editor's ask, press 6742a76, live in press 1.0.88): two open tabs redrew each other without end. state() stamps lastActive and saves p2s.lens on every draw; the storage listener answered every write with go(), which draws, which saves, which fires the other tab's listener: about 250 document.startViewTransition calls a second per tab and hundreds of "AbortError: Transition was skipped" in the console, which also hung the page. The listener now calls go() only when role, reader, depth or confirmed changed (viewSig). The older lens.js and build/design.py listeners (paint(state())) are untouched: please check they do not write from paint. Dev's regression test: records/agents/dev/tests/two-tabs.cjs in team.
