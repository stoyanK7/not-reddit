# Azure Blob Storage

## Status

Accepted.

## Context

We need a way to store images and videos. However, SQL databases are not the best way to store them
according to multiple sources.
[This Stackoverflow answer](https://stackoverflow.com/a/3751/9553927) explains a couple of
important key points:

- database storage is usually more expensive than file system storage
- it is difficult (within the context of a web application) to guarantee data has been flushed to
  disk on the filesystem
- Latency may be slower than direct file access
- Heavier load on the database server

And the main takeaway is:
> We've found that **storing file paths** in the database to be best.

And it makes sense. This way image metadata and the image itself are stored separately. Moreover,
once an image is uploaded, it is not modified.

## Decision

Since _Azure_ is the provider for all services for _not-reddit_ until now and they offer a solution
for storing BLOBs(Binary Large OBjects), we will use
it - [Azure Blob Storage](https://azure.microsoft.com/en-us/products/storage/blobs). One benefit
is that they use containers to store the blobs in so images and videos can be further organized.
Maybe every subreddit can have its own container, but that is a future decision to do. Point is,
they provide a scalable solution for storing BLOBs.

## Consequences

It becomes possible to store and serve large amounts of BLOBs.
