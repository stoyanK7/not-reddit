#!/bin/bash

source util.sh

assert_in_api_dir

# Auth
kubectl delete secret auth-api-secret --ignore-not-found
kubectl create secret generic auth-api-secret --from-env-file=src/main/auth/k8s/deployment.env

# Email
kubectl delete secret email-api-secret --ignore-not-found
kubectl create secret generic email-api-secret --from-env-file=src/main/email/k8s/deployment.env

# Gateway
kubectl delete secret gateway-api-secret --ignore-not-found
kubectl create secret generic gateway-api-secret --from-env-file=src/main/gateway/k8s/deployment.env

# Comment
kubectl delete secret comment-api-secret --ignore-not-found
kubectl delete secret comment-database-secret --ignore-not-found
kubectl create secret generic comment-api-secret --from-env-file=src/main/comment/k8s/deployment.env
kubectl create secret generic comment-database-secret --from-env-file=src/main/comment/k8s/database.env

# Post
kubectl delete secret post-api-secret --ignore-not-found
kubectl delete secret post-database-secret --ignore-not-found
kubectl create secret generic post-api-secret --from-env-file=src/main/post/k8s/deployment.env
kubectl create secret generic post-database-secret --from-env-file=src/main/post/k8s/database.env

# User
kubectl delete secret user-api-secret --ignore-not-found
kubectl delete secret user-database-secret --ignore-not-found
kubectl create secret generic user-api-secret --from-env-file=src/main/user/k8s/deployment.env
kubectl create secret generic user-database-secret --from-env-file=src/main/user/k8s/database.env

# Vote
kubectl delete secret vote-api-secret --ignore-not-found
kubectl delete secret vote-database-secret --ignore-not-found
kubectl create secret generic vote-api-secret --from-env-file=src/main/vote/k8s/deployment.env
kubectl create secret generic vote-database-secret --from-env-file=src/main/vote/k8s/database.env
