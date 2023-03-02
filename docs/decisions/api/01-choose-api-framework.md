# Choose API framework

## Status

Accepted.

## Context

Deciding on the API framework is a very important decision that needs to be taken early on. Once
decided and used for a while, switch to another one is virtually impossible without rewriting the
codebase. The time constraints of this project (18 weeks) do not allow for such mistake to occur.

## Decision

To narrow down to a few from the hundreds of available frameworks, a set of criteria is used:

1. Range of applicability.

   The framework needs to be able to support API development only. A single framework is required.

2. Development speed.

   The development is expected and **has to** to go quick due to short time constraints. The focus
   of this project is higher level architecture and features need to be implemented quickly.

3. Manageability & flexibility.

   The architecture of the system needs to be microservice-based to allow independent deployment and
   scaling of each service and enhance manageability and flexibility. Security is also a concern.

Based on the 3 above-mentioned criteria, below is a table with potential candidates:

| Criteria            | Weight (1-10) | Flask | Grails | Spring Boot | FastAPI |
| ------------------- | ------------- | ----- | ------ | ----------- | ------- |
| Ease of use         |               | 6     | 8      | 5           | 10      |
| Active maintenance  |               | 6     | 5      | 8           | 8       |
| Maturity of product |               | 6     | 6      | 7           | 5       |
| Familiarity         |               | 3     | 0      | 5           | 2       |
| Total               |               | 21    | 19     | 25          | 25      |

As a final decision, **FastAPI** is chosen due to it's speed of development capabilities. These will
outweigh _Spring Boot_ in the long-run. Moreover, documentation is full of examples. The framework
is also very easy to use and understand.

## Consequences

Development of the API should take the least amount of time possible.
