# CI/CD Pipeline

The purpose of this document is to show the history of the CI/CD pipeline for the project. Latest
is always on the top.

## 17 March 2023 (Latest)

The pipeline is triggered by a push to the `main` branch and is composed of 2 workflows:

- `Pytest`: Runs the unit tests.
- `Flake8`: Runs the linter.

![img](../../docs/img/2023-03-17-cicd.png "CI/CD from 5 March 2023")
