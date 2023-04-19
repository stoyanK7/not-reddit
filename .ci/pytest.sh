#!/bin/bash

set -e

cd api/src/test || exit
pytest
