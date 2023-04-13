#!/bin/bash

cd api || exit
flake8 --config .flake8 src/
