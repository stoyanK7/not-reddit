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
  "award" # 8085
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

# Start auth service on 8090
gnome-terminal --tab -- uvicorn src.main.auth.main:app \
  --reload \
  --reload-delay 3 \
  --reload-dir src/main/auth \
  --port 8090

# Start email service
PYTHONPATH=$(pwd) python3 src/main/email/main.py
