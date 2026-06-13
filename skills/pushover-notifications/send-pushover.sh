#!/usr/bin/env bash
#
# Send a push notification via Pushover.
#
# Usage:
#   send-pushover.sh "message text" [-t TITLE] [-p PRIORITY] [-u URL] [-s SOUND]
#
# Options:
#   -t, --title     Notification title (default: app name in Pushover)
#   -p, --priority  -2 (lowest) .. 2 (emergency). Default: 0 (normal)
#   -u, --url       Supplementary URL shown with the notification
#   -s, --sound     Sound name (see https://pushover.net/api#sounds)
#
# Credentials (PUSHOVER_APP_TOKEN, PUSHOVER_USER_KEY) are loaded from, in order:
#   1. The environment, if both are already set.
#   2. The file named by $PUSHOVER_CREDENTIALS, if set.
#   3. ~/.config/pushover/credentials.sh (the default location).
# See credentials.sh.example for the file format.
set -euo pipefail

# Load credentials unless already present in the environment.
if [[ -z "${PUSHOVER_APP_TOKEN:-}" || -z "${PUSHOVER_USER_KEY:-}" ]]; then
  CRED_FILE="${PUSHOVER_CREDENTIALS:-$HOME/.config/pushover/credentials.sh}"
  if [[ -f "$CRED_FILE" ]]; then
    # shellcheck source=/dev/null
    source "$CRED_FILE"
  fi
fi

: "${PUSHOVER_APP_TOKEN:?Set PUSHOVER_APP_TOKEN in the environment or ~/.config/pushover/credentials.sh}"
: "${PUSHOVER_USER_KEY:?Set PUSHOVER_USER_KEY in the environment or ~/.config/pushover/credentials.sh}"

TITLE="" PRIORITY="" URL="" SOUND="" MESSAGE=""
while [[ $# -gt 0 ]]; do
  case "$1" in
    -t|--title)    TITLE="$2";    shift 2 ;;
    -p|--priority) PRIORITY="$2"; shift 2 ;;
    -u|--url)      URL="$2";      shift 2 ;;
    -s|--sound)    SOUND="$2";    shift 2 ;;
    -h|--help)     grep '^#' "$0" | sed 's/^# \{0,1\}//'; exit 0 ;;
    *)             MESSAGE="$1";  shift ;;
  esac
done

if [[ -z "$MESSAGE" ]]; then
  echo "Usage: send-pushover.sh \"message\" [-t title] [-p priority] [-u url] [-s sound]" >&2
  exit 1
fi

# --form-string keeps values literal (a message starting with @ or & won't be misread).
args=(--silent --show-error --fail
  --form-string "token=${PUSHOVER_APP_TOKEN}"
  --form-string "user=${PUSHOVER_USER_KEY}"
  --form-string "message=${MESSAGE}")
[[ -n "$TITLE" ]]    && args+=(--form-string "title=${TITLE}")
[[ -n "$PRIORITY" ]] && args+=(--form-string "priority=${PRIORITY}")
[[ -n "$URL" ]]      && args+=(--form-string "url=${URL}")
[[ -n "$SOUND" ]]    && args+=(--form-string "sound=${SOUND}")

curl "${args[@]}" https://api.pushover.net/1/messages.json
echo
