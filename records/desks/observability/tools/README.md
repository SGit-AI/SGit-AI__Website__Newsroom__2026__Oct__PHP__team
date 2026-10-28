# The telemetry application's dry-run host and its browser checks

Kept by observability@php.newsroom. A host that runs the telemetry application (vault 5wnsr5h8, `app/`) over a copy of
the telemetry vault's data, with the lane's list and fetch going to the real server (read-only calls) and **no publish
and no mark-processed**: those two answer as if done and change nothing. For screenshots and checks of Queue & drain
and One page; never for draining. Nothing here holds a key: the enum key is read from a file you point it at.

```
node harness.mjs <clone of 5wnsr5h8> <a COPY of the 84wr8mib clone> <file holding the lane's enum key> [port=8790] [delay ms per lane call]
node drive.cjs <folder for screenshots>     # check the lane, drain, screenshots   (needs playwright)
node focus.cjs <folder>                      # the page tools and One page
node fail.cjs <folder>                       # a drain whose publish fails (open /?fail=publish)
node notel.cjs <folder>                      # the framed page loads no script and sends no telemetry
node par.cjs <folder>                        # the parallel drain across two lanes
node phone.cjs <folder>                      # One page at 390 px
```

The enum key of a vault is `SHA-256("sg-inbox-enum:" + read key)`; `../drain.py` derives it (`enum_key()`) from the vault
key file. The scripts expect the harness on port 8790 and a Chromium with playwright (`require('playwright')`).
