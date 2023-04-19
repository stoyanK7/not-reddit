#!/bin/bash

set -e

cd api || exit
flake8 --config .flake8 src/
