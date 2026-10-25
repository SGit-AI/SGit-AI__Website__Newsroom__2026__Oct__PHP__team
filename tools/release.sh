#!/usr/bin/env bash
# Release the team repository: take in dev, write the front page, gate, commit, push. In that order, every time.
# Usage: tools/release.sh "<one sentence: what changed and why>"
# Never --no-verify, never a force-push, never main.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"; cd "$ROOT"
MSG="${1:?release message required}"
BRANCH="${RELEASE_BRANCH:-dev}"
git fetch -q origin "$BRANCH" 2>/dev/null || true
if git rev-parse -q --verify "origin/$BRANCH" >/dev/null && ! git merge-base --is-ancestor "origin/$BRANCH" HEAD; then
  if ! git merge -q --ff-only "origin/$BRANCH" 2>/dev/null; then
    echo "release stopped: origin/$BRANCH has commits this clone does not; commit or stash your change, merge origin/$BRANCH by hand, and run this again"
    exit 3
  fi
fi
python3 tools/front.py
python3 tools/gate.py
git add -A
if git diff --cached | grep -E -n 'sgit_private_(vault|read)_[0-9a-f]{12,}|BEGIN [A-Z ]*PRIVATE KEY|AKIA[0-9A-Z]{16}|ghp_[A-Za-z0-9]{30,}' ; then
  echo "tripwire: credential shape in the staged diff; release aborted"; exit 1
fi
if git diff --cached --quiet; then echo "nothing to release"; exit 0; fi
if [ -n "${RELEASE_TRAILER:-}" ]; then git commit -q -m "$MSG" -m "$RELEASE_TRAILER"; else git commit -q -m "$MSG"; fi
git push -q -u origin "HEAD:$BRANCH"
echo "pushed to $BRANCH"
