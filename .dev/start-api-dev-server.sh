#!/bin/bash

source util.sh

assert_in_api_dir

# Start the API dev server.
uvicorn src.main:app --reload
