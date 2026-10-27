# Desk review of the three draft messages (step 2f)

By desk@php.newsroom for projects@, 27 October 2026, before checkpoint B. The drafts are not edited; nothing is sent. Checked against: the editor's words (checkpoint A), the step 4 and outreach rules, data (factcheck.json K-008/K-010/K-011, claims.json, data commit b90449e), the outlet files. Word counts (greeting to sign-off): bbc 208, security team 179, foundation 175: all under 250. No text addressed me or an AI. No private address or private person in any draft.

Checks that pass for all three: tone is warm and specific (a real quote, with capture date, opens each); the disclosure of interest is there; one reply route; "answers published only with consent" matches the brief; the three outlet-file URLs return 200 today.

Common changes (all three)
- C1 "opening soon" promises a page with no date, and the refs page returns 404 today. Proposed: "(not open yet; meanwhile the file is here: URL)". Better still, send only once the page is live. If it stays, remove "or use the page's answer form once it opens": the form is not open. Proposed: "Reply to this message. Answers are published only with your consent."
- C2 The signature says Dinis Cruz, but the agent at riskmandate.ai sends. The editor should confirm that is intended (he said the agent sends, on his go). Proposed line under the signature: "Sent on the editor's behalf by the newsroom's mandate agent." Only if the editor wants it plain.
- C3 "I run it" is ambiguous in an AI-run newsroom. Proposed: "The editor, Dinis Cruz, runs it with AI agents; our interest is disclosed: we build the sgit vault our evidence sits in."
- C4 Channels are all "to find" (url null). None can go until each published contact route is found and captured (not a private address).

## 1. bbc.md: changes needed
- Ask (rule 2): the draft asks "tell us what we have wrong or missing" AND offers a Wiz-70% wording suggestion. The suggestion is our R-002, which the liaison files as a correction, "blocked by R-001" (Wiz, the origin of the figure, not yet asked). Origin before echo, and the journalist's re-grade calls it minor, optional, last. Proposed: delete the whole sentence beginning "One optional suggestion" and send the BBC the single ask. Hold the Wiz point until Wiz has been asked. If the editor wants to keep a suggestion, say so in the file and treat it as R-002 sent after the origin.
- Fact (3): "we corrected two of our own claims" matches b90449e on the two BBC attributions (disclosure date, agency offline line), but b90449e changed four claims (also no-exploitation and an offline-ncsc note). Proposed, exact: "After re-reading your page we corrected two places where we had credited you with words you did not write: a disclosure date and an agency line."
- Fact: "That care is why you have a file here" is fine; "kept its footing" is fine. The quote and hash match the capture.
- Also: no BBC contact route is captured. Do not use the complaints form (it starts a 30-working-day formal process; wrong for a thank-you).
Verdict: changes needed (small).

## 2. php-security-team.md: changes needed
- K-008 matches our data: advisories put the demonstrated FPM exploit under CVE-2026-109619 and say none was demonstrated for CVE-2026-109618. Pass. (The Foundation's swapped attribution is rightly not mentioned here.)
- K-010: "ChangeLog still says 22 Oct" is true of our 22 October capture, not checked today; and our records give two original times (14:00 UTC by the Foundation and release manager, 15:00 UTC by watchTowr). Proposed: "K-010: the release was planned, as we have it, for 22 October 14:00 UTC and shipped on 21 October; the ChangeLog entry said 22 Oct when we captured it."
- K-011 is the weakest: it rests on Zelenka's oss-security post fetched outside the vault (sha256 prefix 94c69d8f1c07e67d), and our site still says PHP has not answered. Capture the post into the vault before sending (messages.json already says so; make it a hard blocker). Wording: use his word. Proposed: "K-011: Jakub Zelenka's 22 October reply calls the 'incomplete fix' report an unrelated issue with minimal impact."
- Ask (rule 2): "three open points" is one ask (check them), acceptable; keep it as one question and no interview. Tone: it is the most "correction-like" of the three. Proposed opening of that paragraph: "To make sure we describe your work correctly, could you tell us whether we have three points right?"
- Tone: add one sentence of added value, as the editor asked ("here are some suggestions, and the added value we can offer"): "We will publish any correction you give us, dated, in the open."
Verdict: changes needed; blocked until K-011's source is captured.

## 3. php-foundation.md: changes needed (minor)
- Fact: the role line is ours from the phase-1 actors audit ("funds core developers; published the account of discovery and the leak"); fine to ask them to check it.
- Promise (4): "the evidence with its hashes" offers more than we publish: captures stay in the evidence vault, the repos show hashes. Proposed: "the hashes and capture dates of everything we hold from you".
- "a correction channel where fixes are made in the open, dated" is true (see b90449e) and keep it. Do not promise a form (C1).
- Ask: one ask, and added value is clearly marked as offered. Pass otherwise. The quote and hash match the capture.
- Note for the editor: the Foundation's post has the K-008 attribution swap, plus the 10.0 CVSS score our data refutes. Rightly not raised now (one ask); it belongs to a later message, after answers.
Verdict: pass with the two changes above.

## Send order (proposed)
1. BBC first, as the editor said: the case study; the page is the most complete (10 claims graded); and with the Wiz sentence removed it asks nothing that depends on an origin that has not been asked. Desk note, for the editor: our rule is origins before echoes; the BBC is an echo of Wiz, Foundation and NCSC. Sending it first is safe only because we ask it about its own page; do not let it become a request about the 70% figure.
2. PHP Foundation second: ready soonest (no capture blocker).
3. PHP security team third, and not before K-011's post is captured. Same day as the Foundation is fine. Apart from each other in content: neither message mentions the other. If both go the same day, security team first if ready, since K-008, K-010 and K-011 are about its own advisories and the Foundation's post is secondary to them.
Rule from the brief that holds: no interview request to any of the three in the same message as a point; interviews are a later, separate message after answers.

## For the editor
- Decide on C2 (signature) and C3 (wording of "I run it").
- Decide whether the Wiz suggestion is dropped (desk advice) or sent later as R-002 after Wiz.
- Someone must find and capture three contact routes (BBC, php.net, thephp.foundation) before any send.
- The refs outlet pages do not exist yet; sending before they do means the links are the JSON files.
