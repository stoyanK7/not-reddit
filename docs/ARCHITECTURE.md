# Architecture

This document describes the history of the architecture of the project. Latest is always on the top.

## 11 April 2023 (Latest)

The application has a single point of entry, the API gateway. It is responsible for routing the
requests and for authentication. The subreddit and vote services are now implemented:
See [06. Decision record for API Gateway](decisions/api/06-api-gateway.md) and
[05. Decision record for Votes](decisions/api/05-votes-microservice.md) for more details.

![img](img/2023-04-11-architecture.png "Architecture from 11 April 2023")

## 18 March 2023

Three API endpoints for users, comments and posts. See
[03. Microservice containers](decisions/api/04-microservice-containers.md) for more details.:

![img](img/2023-03-18-architecture.png "Architecture from 18 March 2023")

## 5 March 2023

Initial walking skeleton:

![img](img/2023-03-05-architecture.png "Architecture from 5 March 2023")
