# Choose database

## Status

Accepted.

## Context

The projects needs a place to store all the data that will be collected. The data is expected to
consist of text, images and video.

## Decision

A research was conducted to find a database that would be suitable for the project. The final
conclusion is that it really
[does not matter what database is used initially](https://www.reddit.com/r/webdev/comments/x2l2uy/if_you_were_tasked_with_creating_a_reddit_clone/).

> Whatever I use now because I’m familiar with it and can work far faster than if I picked something
> I don’t know well. If the app gains traction in a year or two, they’ll be at the next level of
> funding so they can rebuild it with some stack that doesn’t exist yet.

_reddit_ developers
[say they use PostgreSQL](https://www.reddit.com/r/programming/comments/z9sm8/comment/c62u7gw/?utm_source=share&utm_medium=web2x&context=3):

> I thought reddit was using ..., running alongside Postgres?

> We are.

**PostgreSQL** will be the initial choice for the database. It is a mature, well maintained and a
relational database will allow to define complex data relationships which are a lot in the scope of
the project.

## Consequences

Storing of posts, comments, users, images and videos should be possible now.
