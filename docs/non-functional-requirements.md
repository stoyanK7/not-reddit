# Non-Functional Requirements

## Introduction

The purpose of this document is to describe the non-functional requirements of the project.

[_Testing Strategy_](testing-strategy.md) and [_Test Report_](test-report.md) document
the testing strategy and results for validating the non-functional requirements.

## Non-Functional Requirements

### Performance

The performance metrics are derived from the real reddit application statistics [[1]](#references)
and some are scaled down to a reasonable level for our application. The metrics are as follows:

- **The application should support 500 landing page visitors per second.**

  > Further clarification:
  > - all visitors should be served the landing page in under 5 seconds.
  > - all text and images should be rendered.

  Derived from the fact that:
  > Reddit received 30 billion average monthly views in 2020.

  To make this metric more digestible:

  ```math
  30,000,000,000 views / 365 days / 24 hours / 60 minutes / 60 seconds ~= 951 views per second
  ```

  This number is scaled down to 500 visitors per second for our application.

- **The application should process 10 posts per second.**

  > Further clarification:
  > - 6 of these posts should be text posts ranging from 1,000 to 10,000 characters in length.
  > - 3 of these posts should be image posts with images from 1MB to 5MB in size.
  > - 1 of these posts should be a video post with a video from 1MB to 10MB in size.
  > - all posts should be processed in under 20 seconds.

  Derived from the fact that:
  > 303.4 million posts were uploaded in 2020.

  To make this metric more digestible:

  ```math
  303,400,000 posts / 365 days / 24 hours / 60 minutes / 60 seconds ~= 10 posts per second
  ```

  Obviously, reddit does not receive 10 posts per second equally throughout the whole year but this
  sounds like a reasonable metric for our application, so we stick with it.

- **The application should process 63 comments per second.**

  > Further clarification:
  > - all comments should be text comments ranging from 500 to 2,000 characters in length.
  > - all comments should be processed in under 10 seconds.

  Derived from the fact that:
  > In 2020, Reddit users posted over two billion comments.

  To make this metric more digestible:

  ```math
  2,000,000,000 comments / 365 days / 24 hours / 60 minutes / 60 seconds ~= 63 comments per second
  ```

  This number also seems reasonable for our application.

- **The application should process 1585 votes per second.**

  > Further clarification:
  > - all votes should a mix of upvotes and downvotes.

  Derived from the fact that:
  > In 2020, Reddit users posted .. and 49.2 billion upvotes

  To make this metric more digestible:

  ```math
  50,000,000,000 votes / 365 days / 24 hours / 60 minutes / 60 seconds ~= 1585 votes per second
  ```

  Again, this number seems reasonable for our application. Though, it is a bit on the high side.

### Scalability

### Security

### Privacy/GDPR

## References

    [1] [Reddit Statistics](https://www.businessofapps.com/data/reddit-statistics/)
