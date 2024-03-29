#!/bin/bash

set -e

function assert_in_api_dir {
  # Assert that the script is being run from the api directory.
  if [[ ! $(pwd) =~ api$ ]]; then
    echo "Please run this script from the api directory."
    exit 1
  fi
}

function assert_venv_active {
  # Assert that the virtual environment is active.
  if [[ -z "$VIRTUAL_ENV" ]]; then
    echo "Please activate the virtual environment before running this script."
    exit 1
  fi
}

function checkForVariable {
  VAR_NAME=$1
  if [ ! -v "$VAR_NAME" ]; then
    echo "[Error] Define $1 environment variable"
    exit 1
  fi

  VAR_VALUE="${!VAR_NAME}"
  if [ -z "$VAR_VALUE" ]; then
    echo "[Error] Set not empty value to $1 environment variable"
    exit 1
  fi
}
