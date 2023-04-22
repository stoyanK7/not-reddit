# Database per microservice

## Status

Accepted.

## Context

There are multiple reasons for having a database per microservice:

- Loose coupling: Changes to one microservice do not affect other microservices.
- Performance: Each microservice can have its own database instance, which can be optimized for the specific
  microservice. For instance, the _vote_ microservice should have a different database type optimized for events since
  every vote is an event.
- Fault isolation: If one microservice's database fails, the other microservices are not affected.

## Decision

We will have a database per microservice - https://microservices.io/patterns/data/database-per-service.html.

## Consequences

We can be ensured that changes to one microservice do not affect other microservices. Each microservice can have its
own database that is suited to its needs. However, implementing queries that span multiple
databases can be challenging. Moreover, it is more complex to manage multiple databases.
