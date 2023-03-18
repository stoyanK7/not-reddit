# Microservice containers

## Status

Accepted.

## Context

An event storming session was performed and the following aggregates were identified:
![img](../../img/2023-03-18-event-storming.png "Event Storming")

The full event storming session is available under the `docs/event-storming` file.

## Decision

The decision is made to have the following microservices:

- `posts`
- `comments`
- `votes` (explanation of this decision is kept in `05-votes-microservice.md`)
- `users`
- `subreddits`
- `payments`

## Consequences

Scalability and performance should be improved when the system is under big load. However,
development time will be increased because we will have to implement more microservices.
