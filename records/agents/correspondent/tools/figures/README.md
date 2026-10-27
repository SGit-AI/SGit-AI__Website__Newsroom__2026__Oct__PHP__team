# The correspondent's figure and deck generators

The code that drew the figures and decks of the two reader-question articles of 26 October 2026
(`has-anyone-been-hacked`, `steal-my-bitcoin`), kept here so they can be redrawn in a new session.

- `charts.py`: the seven figures of has-anyone-been-hacked (ladder, statements, offline-vs-breached, evidence, pipeline,
  timeline, weight), from the data pinned at v0.1.33; writes `figures.html`.
- `charts2.py`: the four figures of steal-my-bitcoin (three-things, chain, replicable, funnel); conceptual, no exploit detail.
- `deck.py`, `deck2.py`: the HTML decks (16:9, one slide a page when printed).
- `shot.js`, `shot2.js`: each figure's SVG to PNG (Playwright); `pdf.js`, `pdf2.js`: each deck to PDF and slide PNGs.

Run from a scratch folder: `python3 charts.py && node shot.js <folder>`, then copy the PNGs to the press's
`assets/articles/<slug>/`. The press's copies of the decks carry a CSP that others added: edit them in place, do not
overwrite them with a fresh `deck.py` output.
