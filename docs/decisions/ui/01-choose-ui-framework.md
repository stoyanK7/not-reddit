# Choose UI framework

## Status

Accepted.

## Context

Deciding on the UI framework is a very important decision that needs to be taken early on. Once
decided and used for a while, switch to another one is virtually impossible without rewriting the
codebase. The time constraints of this project (18 weeks) do not allow for such mistake to occur.

## Decision

To narrow down to a few from the hundreds of available frameworks, a set of criteria is used:

1. Range of applicability.

   The framework needs to be able to support UI development and have the ability to make calls to
   the API to retrieve data and visualize it. A single framework is required for this task.

2. Development speed.

   The development is expected and **has to** to go quick due to short time constraints. The focus
   of this project is higher level architecture and features need to be implemented quickly.

3. Manageability & flexibility.

   The framework should allow for flexibility in terms of design and development. It should be easy
   to maintain and extend. A framework that is component-based is preferred because of that.
   Reusability of components will also improve the development speed.

Based on the 3 above-mentioned criteria, **NextJS** is chosen as the UI framework. Previous
experience with React means it is easy to get started with NextJS because of the similarities in
syntax. Moreover, NextJS supports numerous dependencies to make API calls and data fetching.
Finally, server-side rendering is supported out of the box, which is a huge plus for performance.

## Consequences

Development of the UI should take the least amount of time possible.
