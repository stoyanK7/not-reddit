#!/bin/bash

source util.sh

assert_in_api_dir

# Export the list of dependencies to a file.
pip freeze >requirements.txt
