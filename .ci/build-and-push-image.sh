#!/bin/bash

set -e

source ./.ci/util.sh

checkForVariable REGISTRY_LOGIN_SERVER
checkForVariable SERVICE

cd api || exit

IMAGE_NAME="$REGISTRY_LOGIN_SERVER/$SERVICE-service:latest"
docker build . \
  -t "$IMAGE_NAME" \
  -f src/main/"$SERVICE"/Dockerfile
docker push "$IMAGE_NAME"
