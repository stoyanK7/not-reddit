# Choose message broker

## Status

Accepted.

## Context

A message broker is needed to allow the different microservices to communicate with each other. The
message broker should be able to handle a large number of messages per second, and should be able to
handle a large number of messages in the queue.

The point is to avoid the microservices to be dependent on each other, and to be able to scale.

## Decision

_RabbitMQ_ seems to be the defacto standard for message brokers. It is open source, and has a large
community. It is also used by many companies(_Robinhood_ and _reddit_ itself, for instance), and is
therefore well tested in real implementations.

## Consequences

Communication between microservices will be done through RabbitMQ. This will allow to scale the
microservices independently and make the system more-flexible to changes.
