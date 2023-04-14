#!/bin/bash

set -e

source ./.ci/util.sh

checkForVariable REGISTRY_LOGIN_SERVER
checkForVariable SERVICE

cd api/src/main || exit

IMAGE_NAME="$REGISTRY_LOGIN_SERVER/$SERVICE-api:latest"
docker build . \
  -t "$IMAGE_NAME" \
  -f "$SERVICE"/Dockerfile
docker push "$IMAGE_NAME"
