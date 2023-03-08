#!/bin/bash

NETWORK="postgresql-network"
POSTGRESQL="postgresql"
PGADMIN="pgadmin"

echo "Checking if network $NETWORK is created."
if [ "$(docker network ls -q -f name=$NETWORK)" ]; then
  echo "Network $NETWORK is already created."
else
  echo "Network $NETWORK is not created."
  echo "Creating $NETWORK network."
  docker network create "$NETWORK"
fi

echo "Checking if container $POSTGRESQL is created."
if [ "$(docker ps -aq -f name="$POSTGRESQL")" ]; then
  if [ "$(docker ps -aq -f name="$POSTGRESQL" -f status=running)" ]; then
    echo "Stopping container $POSTGRESQL"
    docker stop "$POSTGRESQL"
  else
    echo "Running container $POSTGRESQL"
    docker start "$POSTGRESQL"
  fi
else
  echo "Container $POSTGRESQL is not created."
  echo "Creating $POSTGRESQL container."
  docker run \
  -d \
  -p 5432:5432 \
  -e "POSTGRES_PASSWORD=root" \
  -v /data:/var/lib/postgresql/data \
  --network="$NETWORK" \
  --name "$POSTGRESQL" \
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
