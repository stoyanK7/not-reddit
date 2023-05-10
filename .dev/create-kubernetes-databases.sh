#!/bin/bash

source util.sh

assert_in_api_dir

# User
kubectl apply -f src/main/user/k8s/database.yml

# Post
kubectl apply -f src/main/post/k8s/database.yml

# Comment
kubectl apply -f src/main/comment/k8s/database.yml

# Vote
kubectl apply -f src/main/vote/k8s/database.yml

