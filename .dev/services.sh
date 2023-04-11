#!/bin/bash

source util.sh

assert_in_api_dir
assert_venv_active

SERVICES=(
  "gateway" # 8000
  "post" # 8001
  "user" # 8002
  "comment" # 8003
  "vote" # 8004
  "subreddit" # 8005
)
STARTING_PORT=8000
for SERVICE in "${SERVICES[@]}"; do
  echo "Starting $SERVICE service on port $STARTING_PORT."
  gnome-terminal --tab -- uvicorn src.main."$SERVICE".main:app --reload --port "$STARTING_PORT"
  STARTING_PORT=$((STARTING_PORT + 1))
done
