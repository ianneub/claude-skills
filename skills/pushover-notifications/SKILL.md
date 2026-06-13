---
name: pushover-notifications
description: Use when you need to push a notification to the user's phone or device — a long-running task finished, a build or deploy completed, something needs their attention while they're away, or the user asks to be notified, pinged, alerted, or texted. Sends via Pushover to their configured device.
---

# Pushover Notifications

## Overview

Send a push notification to the user's device through Pushover. Useful for alerting the user when a long task finishes, a deploy completes, an error needs attention, or any time they ask to be pinged.

## Deferred notifications: arm first

When you will send the notification on a **future event** (e.g. "ping me when the deploy finishes", "tell me when the instance is available") — not an immediate one-off send — **send an upfront "armed" confirmation ping first**, at the moment you commit to notifying.

```bash
send-pushover.sh "🔔 Armed — I'll notify you here when the RDS instance is available." -t "Claude Code"
```

Why: it proves the notification channel is live right now. If the channel were broken, this armed ping would fail loudly here instead of the real alert silently never arriving later. So if the user gets the armed ping but nothing afterward, they know the *event* didn't fire — not that Pushover is down.

- Verify the armed ping succeeded (`{"status":1}`) before relying on the deferred notification.
- Do **not** send an armed ping for immediate one-off sends ("text me this now") — those go straight through.

## Quick Reference

The script lives next to this SKILL.md. Run it by its path inside the skill directory:

```bash
"${CLAUDE_PLUGIN_ROOT}/skills/pushover-notifications/send-pushover.sh" "Your message here"
```

With options:

```bash
send-pushover.sh "Deploy finished" -t "CI" -p 0 -u "https://example.com/build/123"
```

| Flag | Meaning |
|------|---------|
| `-t, --title` | Notification title |
| `-p, --priority` | `-2` silent · `-1` quiet · `0` normal · `1` high · `2` emergency |
| `-u, --url` | Supplementary link shown in the notification |
| `-s, --sound` | Sound name (see https://pushover.net/api#sounds) |

Run `send-pushover.sh --help` for full usage.

## Behavior

- On success, Pushover returns `{"status":1,"request":"..."}` and the script exits 0.
- On failure (bad token, network error), `curl --fail` makes the script exit non-zero and print the error.

## Credentials

The script loads `PUSHOVER_APP_TOKEN` and `PUSHOVER_USER_KEY` from, in order:

1. The environment, if both are already exported.
2. The file named by `$PUSHOVER_CREDENTIALS`, if set.
3. `~/.config/pushover/credentials.sh` — the default location, kept at `chmod 600`.

Real tokens never live in this repo. To set up a new machine, copy `credentials.sh.example` to `~/.config/pushover/credentials.sh` and fill in the values. To point at a different Pushover app or device, edit that file — never hardcode tokens in commands or other files.

## Common Mistakes

- **Priority 2 (emergency) requires `retry` and `expire` params** in the Pushover API; this wrapper doesn't set them, so avoid `-p 2` unless you extend the script.
- **Message length** is capped at 1024 characters by Pushover; longer messages are rejected.
- **Don't spam** — send one meaningful notification per event, not per step.
