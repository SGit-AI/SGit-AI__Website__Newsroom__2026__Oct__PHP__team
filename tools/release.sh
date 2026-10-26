#!/usr/bin/env bash
# Release the team repository: take in dev, write the front page, gate the records and the pages, commit, push. In that order, every time.
# Usage: tools/release.sh "<one sentence: what changed and why>"
# Never --no-verify, never a force-push, never main.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"; cd "$ROOT"
MSG="${1:?release message required}"
BRANCH="${RELEASE_BRANCH:-dev}"
git fetch -q origin "+refs/heads/$BRANCH:refs/remotes/origin/$BRANCH" 2>/dev/null || true   # the tracking ref itself: a clone made for one branch does not move it on a plain fetch
if git rev-parse -q --verify "origin/$BRANCH" >/dev/null && ! git merge-base --is-ancestor "origin/$BRANCH" HEAD; then
  if ! git merge -q --ff-only "origin/$BRANCH" 2>/dev/null; then
    echo "release stopped: origin/$BRANCH has commits this clone does not; commit or stash your change, merge origin/$BRANCH by hand, and run this again"
    exit 3
  fi
fi
python3 tools/front.py
python3 tools/gate.py
if [ -f tools/pages_gate.py ]; then python3 tools/pages_gate.py; fi   # the pages, partitioned from v1 by the press
git add -A
if git diff --cached | grep -E -n 'sgit_private_(vault|read)_[0-9a-f]{12,}|BEGIN [A-Z ]*PRIVATE KEY|AKIA[0-9A-Z]{16}|ghp_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{30,}|\bsk-(or-v1-|proj-|ant-[a-z0-9]+-)?[A-Za-z0-9_]{32,}' ; then
  echo "tripwire: credential shape in the staged diff; release aborted"; exit 1
fi
if git diff --cached --quiet; then echo "nothing to release"; exit 0; fi
# Every member releases here, minutes apart. A rejected push undoes the commit, takes in what landed (one file per
# record, so two members' changes rarely meet), and pushes again. Five tries.
for attempt in 1 2 3 4 5; do
  if [ -n "${RELEASE_TRAILER:-}" ]; then git commit -q -m "$MSG" -m "$RELEASE_TRAILER"; else git commit -q -m "$MSG"; fi
  if git push -q -u origin "HEAD:$BRANCH" 2>/dev/null; then echo "pushed to $BRANCH"; exit 0; fi
  echo "push rejected (someone released meanwhile): taking it in ($attempt of 5)"
  git reset -q --soft HEAD~1
  git fetch -q origin "+refs/heads/$BRANCH:refs/remotes/origin/$BRANCH"
  git merge -q --ff-only "origin/$BRANCH" || { echo "release stopped: your change and someone else's touch the same file; merge origin/$BRANCH by hand and run this again"; exit 3; }
  python3 tools/front.py >/dev/null && git add -A
done
echo "release stopped: five tries, five releases by others in between; run this again"; exit 3
