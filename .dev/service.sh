#!/bin/bash

set -e

source util.sh

assert_in_api_dir
assert_venv_active
SERVICE=$1

if [[ -z "$SERVICE" ]]; then
  echo "service is not set"
  echo "Usage: $BASH_SCRIPT <service>"
  exit 1
fi

if [[ -z "$STARTING_PORT" ]]; then
  export STARTING_PORT=8080
fi

echo "Starting $SERVICE service on port $STARTING_PORT."
gnome-terminal --tab -- uvicorn src.main."$SERVICE".main:app \
  --reload \
  --reload-delay 3 \
  --reload-dir src/main/"$SERVICE" \
  --port "$STARTING_PORT"
STARTING_PORT=$((STARTING_PORT + 1))
