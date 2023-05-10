#!/bin/bash

source util.sh

assert_in_api_dir

# User
kubectl apply -f src/main/user/k8s/user-database-deployment.yml

# Post
kubectl apply -f src/main/post/k8s/post-database-deployment.yml

# Comment
kubectl apply -f src/main/comment/k8s/comment-database-deployment.yml

# Vote
kubectl apply -f src/main/vote/k8s/vote-database-deployment.yml

