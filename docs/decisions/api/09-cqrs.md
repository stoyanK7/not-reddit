# Command Query Responsibility Segregation (CQRS)

## Status

Accepted.

## Context

While developing the endpoint for creating a post a problem occurs. The database table that stores
the posts has a column with a username. When a user creates a post they send their jwt token, but
it only contains the user email. With this email, we have to make a call to the user microservice
to get the username. This causes unnecessary coupling. The post microservice should not know about
the user microservice. There are a couple of solutions to this problem

- CQRS: https://microservices.io/patterns/data/cqrs.html
- API Composition: https://microservices.io/patterns/data/api-composition.html

API Composition is not a good solution because it adds an extra layer of complexity and creates
further problems - it needs to know about database schemas and how to join data. CQRS is a better
solution in this case because we already have a messaging queue for when a user is created and data
storage is not of concern.

## Decision

CQRS is going to be used for handling this particular problem and future ones like it. This involves
creating another table in the database that holds the username and the oid of the user, so we can
reference it. When the user microservice creates a user, a message is broadcast that the post
microservice can pick up and add the user to its database as well.

## Consequences

It becomes easier and faster to query data from other domain contexts. The drawback is more data
is duplicated between services but storage is cheap so that should not be a problem. Besides, it is
only 2 columns of data.
