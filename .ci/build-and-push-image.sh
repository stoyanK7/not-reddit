#!/bin/bash

set -e

source ./.ci/util.sh

checkForVariable "REGISTRY_LOGIN_SERVER"
checkForVariable "SERVICE_NAME"
checkForVariable "CONTEXT"
checkForVariable "DOCKERFILE_PATH"

cd "$CONTEXT" || exit

IMAGE_NAME="$REGISTRY_LOGIN_SERVER/$SERVICE_NAME-service:latest"
docker build . \
  -t "$IMAGE_NAME" \
  -f "$DOCKERFILE_PATH"
docker push "$IMAGE_NAME"
