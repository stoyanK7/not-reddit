# CI/CD Pipeline

The purpose of this document is to show the history of the CI/CD pipeline for the project. Latest
is always on the top.

## 24 May 2023 (Latest)

A deployment job was added. It first run tests, then builds and pushes the Docker images to Azure
Container Registry and finally deploys the application to Azure Kubernetes Service via a rolling
deployment.

![img](../../docs/img/2023-05-24-cicd.png "CI/CD from 24 May 2023")

## 14 April 2023

The project now has a workflow to build and push the Docker images to Azure Container Registry.

![img](../../docs/img/2023-04-14-cicd.png "CI/CD from 14 April 2023")

## 17 March 2023

The pipeline is triggered by a push to the `main` branch and is composed of 2 workflows:

- `Pytest`: Runs the unit tests.
- `Flake8`: Runs the linter.

![img](../../docs/img/2023-03-17-cicd.png "CI/CD from 5 March 2023")
