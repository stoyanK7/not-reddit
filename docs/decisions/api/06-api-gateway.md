# API Gateway

## Status

Accepted.

## Context

One of the security non-functional requirements is
that [the API should support the OAuth2 protocol.](../../non-functional-requirements.md#security)
Moreover, the microservices should be closed to the outside world, and only the API Gateway should
be exposed to the public. In addition, it might come in handy for monitoring and logging purposes
in the future.

## Decision

To achieve this goal, an API Gateway will be
implemented - https://microservices.io/patterns/apigateway.html
It will be the single point that will take care of the authentication and authorization of the
requests, and will forward them to the appropriate microservice. All of the microservices will
have to be closed to the outside world and allow only requests from the API Gateway.

## Consequences

Security is improved, however extra complexity is added since requests must go through the API
Gateway first.
