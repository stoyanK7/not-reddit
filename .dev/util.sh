#!/bin/bash

function assert_in_api_dir {
  # Assert that the script is being run from the api directory.
  if [[ ! -d .venv ]]; then
    echo "Please run this script from the api directory."
    exit 1
  fi
}
