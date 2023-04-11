#!/bin/bash

NETWORK="postgresql-network"
POSTGRES="postgres"
PGADMIN="pgadmin"

echo "Checking if network $NETWORK is created."
if [ "$(docker network ls -q -f name=$NETWORK)" ]; then
  echo "Network $NETWORK is already created."
else
  echo "Network $NETWORK is not created."
  echo "Creating $NETWORK network."
  docker network create "$NETWORK"
fi

echo "Checking if container $POSTGRES is created."
if [ "$(docker ps -aq -f name="$POSTGRES")" ]; then
  if [ "$(docker ps -aq -f name="$POSTGRES" -f status=running)" ]; then
    echo "Stopping container $POSTGRES"
    docker stop "$POSTGRES"
  else
    echo "Running container $POSTGRES"
    docker start "$POSTGRES"
  fi
else
  echo "Container $POSTGRES is not created."
  echo "Creating $POSTGRES container."
  docker run \
  -d \
  -p 5432:5432 \
  -e "POSTGRES_PASSWORD=root" \
  -v /data:/var/lib/postgresql/data \
  --network="$NETWORK" \
  --name "$POSTGRES" \
  postgres
fi

echo "Checking if container $PGADMIN is created."
if [ "$(docker ps -aq -f name="$PGADMIN")" ]; then
  if [ "$(docker ps -aq -f name="$PGADMIN" -f status=running)" ]; then
    echo "Stopping container $PGADMIN"
    docker stop "$PGADMIN"
  else
    echo "Running container $PGADMIN"
    docker start "$PGADMIN"
  fi
else
  echo "Container $PGADMIN is not created."
  echo "Creating container $PGADMIN."
  docker run \
  -d \
  -p 5050:80 \
  -e "PGADMIN_DEFAULT_EMAIL=root@root.root" \
  -e "PGADMIN_DEFAULT_PASSWORD=root" \
  -e "PGADMIN_CONFIG_SERVER_MODE=False" \
  -e "PGADMIN_CONFIG_MASTER_PASSWORD_REQUIRED=False" \
  --network="$NETWORK" \
  --name "$PGADMIN" \
  dpage/pgadmin4
fi
