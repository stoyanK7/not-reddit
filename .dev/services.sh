#!/bin/bash

source util.sh

assert_in_api_dir
assert_venv_active

SERVICES=(
  "gateway"
  "post"
  "user"
  "comment"
  "vote"
  "subreddit"
)
STARTING_PORT=8000
for SERVICE in "${SERVICES[@]}"; do
  echo "Starting $SERVICE service on port $STARTING_PORT."
  gnome-terminal --tab -- uvicorn src.main."$SERVICE".main:app --reload --port "$STARTING_PORT"
  STARTING_PORT=$((STARTING_PORT + 1))
done
