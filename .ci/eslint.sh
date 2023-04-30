#!/bin/bash

set -e

cd ui/src/main || exit
npm run lint
