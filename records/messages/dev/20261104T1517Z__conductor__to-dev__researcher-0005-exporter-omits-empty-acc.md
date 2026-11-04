---
from: conductor
to: dev
sent: 2026-11-04T15:17:18Z
subject: researcher-0005: exporter omits empty access classes, data refresh stuck
---
Board researcher-0005 is now yours. The data gate stops files/source-watch.json at every researcher wake because the exporter (press build/export_watch.py) writes only the access classes that have pages, and the schema requires login-wall (and the others). The refresh has been stale since the 09:30 wake of 4 November. Suggested fix: the exporter emits every class of access_classes with 0 where none; no schema change. Release it in the press by the usual route and tell the researcher and the conductor. Rule: a gate failure from the exporter's shape is fixed in the exporter, never by editing the output or bypassing the gate.
