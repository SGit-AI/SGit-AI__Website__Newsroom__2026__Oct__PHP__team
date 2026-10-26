# The fix, mapped to the code

> Research: collected from outside sources and what this site derives from them; every fact links to a saved copy of its source.

The php2shell fix as layered graphs: the two flaws, the design of the patch, and the php-src files and functions it changed, derived from the diff.

# The fix, mapped to the code

The editor asked for the kind of source-code mapping we did at [secrets.sgit.ai/review](https://secrets.sgit.ai/review/): the project as layered graphs, the intent on one side and the code derived from the syntax tree on the other, with the join between them. Here the intent is the two flaws and the design of the patch; the code is what the patch changed in [php-src](https://github.com/php/php-src), read from the diff by a parser rather than a model. Three layers, 54 nodes and 68 edges; [walk them in the navigator](ui/index.html), or read the map below.

**Commit** `3584a98bd` · **389** files changed, 37 of them in the engine and bundled extensions traced here · **36** areas

## The flaws

**CVE-2026-109618: RCE via OOM corruption** An out-of-memory condition during request handling could leave request memory in an uninitialised state that later cleanup reads. CVSS v4.0 9.2. GHSA-w8hw-w9fx-j79w. [CVE record](../sources/cve-cve-2026-109618/index.html)

**CVE-2026-109619: RCE via stale global state** Global state that referenced request memory was not always reset, so a later request on the same worker could read freed memory. CVSS v4.0 9.2. GHSA-6wmf-4rv5-p3rp. [CVE record](../sources/cve-cve-2026-109619/index.html)

## What the fix does, and where

Each card is one thing the patch does, with the functions it uses and the files it changed. The text describes the remediation; how the flaw is reached is on [the two flaws](../flaws/index.html) and [the code](../code/index.html), which this layer sits beside.

### [A soft memory limit that no longer jumps](ui/index.html#fix-soft-limit)

At the memory limit the allocator stops using the longjmp bailout; it queues a delayed error and lets the allocation proceed, so the fatal is raised later with request state intact.

**Functions.** `zend_mm_check_limit, zend_mm_delayed_error`

Addresses: CVE-2026-109618
- [Zend/zend_alloc.c](https://github.com/php/php-src/blob/3584a98bda0f2c0d367255b046798b0d3a221a19/Zend/zend_alloc.c) +527 / -122

### [A hard limit that ends the process cleanly](ui/index.html#fix-hard-limit)

A new memory_hard_limit_percent sets a ceiling above memory_limit; reaching it ends the worker with _exit(), leaving no cleanup to corrupt. zend_mm_panic also uses _exit now.

**Functions.** `zend_mm_hard_limit_error` · **new setting** `memory_hard_limit_percent`

Addresses: CVE-2026-109618

### [An orderly unwind at the next safe point](ui/index.html#fix-unwind)

The queued error is handled at a VM safe point: it throws an UnwindExit that unwinds the PHP frames in order before the fatal, rather than a C longjmp across half-built state.

**Functions.** `zend_handle_delayed_oom, zend_throw_unwind_exit`

Addresses: CVE-2026-109618
- [Zend/zend_execute_API.c](https://github.com/php/php-src/blob/3584a98bda0f2c0d367255b046798b0d3a221a19/Zend/zend_execute_API.c) +36 / -13

### [Request globals reset so nothing survives a failure](ui/index.html#fix-reset-globals)

Shutdown and deactivate paths set freed pointers to NULL or UNDEF, 'may be accessed before php_request_startup()', so a later request cannot find stale state.

**Functions.** `shutdown_executor, php_request_shutdown, sapi_deactivate`

Addresses: CVE-2026-109619
- [main/SAPI.c](https://github.com/php/php-src/blob/3584a98bda0f2c0d367255b046798b0d3a221a19/main/SAPI.c) +6 / -2
- [main/main.c](https://github.com/php/php-src/blob/3584a98bda0f2c0d367255b046798b0d3a221a19/main/main.c) +48 / -2

### [Bounded, deduplicated request parsing](ui/index.html#fix-bounded-parsing)

A new max_multipart_body_parts caps the number of parts the body parser accepts; the multipart header parser keeps only the two headers it uses and ignores duplicates; the session upload-progress callback is changed.

**Functions.** `multipart_buffer_headers, rfc1867_post_handler` · **new setting** `max_multipart_body_parts`

Addresses: CVE-2026-109619
- [ext/session/session.c](https://github.com/php/php-src/blob/3584a98bda0f2c0d367255b046798b0d3a221a19/ext/session/session.c) +56 / -11
- [main/rfc1867.c](https://github.com/php/php-src/blob/3584a98bda0f2c0d367255b046798b0d3a221a19/main/rfc1867.c) +188 / -27

### [Allocations that may fail instead of abort](ui/index.html#fix-fallible)

Allocation paths a caller can tolerate failing become 'fallible' and return NULL rather than jumping, which is what lets the new tests exercise the OOM handling at any allocation.

**Functions.** `fallible allocation family`

Addresses: CVE-2026-109618
- [Zend/zend_hash.c](https://github.com/php/php-src/blob/3584a98bda0f2c0d367255b046798b0d3a221a19/Zend/zend_hash.c) +259 / -43
- [Zend/zend_string.c](https://github.com/php/php-src/blob/3584a98bda0f2c0d367255b046798b0d3a221a19/Zend/zend_string.c) +20 / -2
- [Zend/zend_types.h](https://github.com/php/php-src/blob/3584a98bda0f2c0d367255b046798b0d3a221a19/Zend/zend_types.h) +15 / -11

## The change, by area

The patch is 389 files because the new allocation contract touched every place in the engine and the bundled extensions that used to abort on a failed allocation. The twenty largest areas:

| Area | Files | Added | Removed |
|---|---|---|---|
| Zend/ | 96 | 2932 | 268 |
| tests/ | 34 | 1109 | 1 |
| ext/standard | 52 | 1061 | 85 |
| ext/mbstring | 30 | 570 | 76 |
| ext/gd | 19 | 498 | 17 |
| ext/session | 5 | 416 | 63 |
| ext/soap | 14 | 375 | 8 |
| main/ | 7 | 345 | 50 |
| ext/zlib | 11 | 344 | 10 |
| ext/filter | 8 | 335 | 9 |
| ext/date | 17 | 326 | 122 |
| ext/exif | 8 | 318 | 23 |
| ext/zend_test | 8 | 278 | 42 |
| ext/xmlreader | 8 | 236 | 5 |
| ext/pcre | 8 | 186 | 10 |
| ext/fileinfo | 3 | 168 | 51 |
| ext/iconv | 7 | 146 | 11 |
| ext/json | 8 | 137 | 23 |
| ext/simplexml | 4 | 134 | 26 |
| ext/opcache | 7 | 113 | 11 |

The full per-file data, with the functions each hunk changed, is [data/review.json](../data/review.json) and [review/code/files.json](../review/code/files.json), derived from `git show` of the commit.

## How this was built
- **The code layer** is derived by a parser from `git show -U0` of the fix commit: files, the functions each hunk falls in, the symbols the patch adds. Never a model, so it cannot invent a function that is not in the diff.
- **The remediation layer** is written from the commit message and the diff and checked against the two GitHub advisories; it is the one layer a person wrote, and it is marked as such.
- **The join** is the "realised in" edges from each remediation node to the files that carry it.
- It follows the estate brief [Code review graphs in the repository](https://sgit.ai/docs/briefs/code-review-graphs-in-the-repository.html), at the smallest size that still maps a change to its code.


---
site v0.22.23 · data as of 2026-10-25T09:35Z · vault commit 87795d121200 · https://php.oct.2026.newsroom.sgit.ai/review/index.html
