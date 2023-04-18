#!/bin/bash

set -e

source util.sh

assert_in_api_dir
assert_venv_active

SERVICES=(
  "user" # 8081
  "post" # 8082
  "vote" # 8083
  "comment" # 8084
)
STARTING_PORT=8081

for SERVICE in "${SERVICES[@]}"; do
  echo "Starting $SERVICE service on port $STARTING_PORT."
  gnome-terminal --tab -- uvicorn src.main."$SERVICE".main:app \
  --reload \
  --reload-delay 3 \
  --reload-dir src/main/"$SERVICE" \
  --port "$STARTING_PORT"
  STARTING_PORT=$((STARTING_PORT + 1))
done
