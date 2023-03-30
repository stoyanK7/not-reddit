# Non-Functional Requirements

## Introduction

The purpose of this document is to describe the non-functional requirements of the project.

[_Testing Strategy_](testing-strategy.md) and [_Test Report_](test-report.md) document
the testing strategy and results for validating the non-functional requirements.

## Non-Functional Requirements

The [performance](#performance) and [scalability](#scalability) metrics are derived from the real
reddit application statistics [[1]](#references) and some are scaled down to a reasonable level for
our application.

Some security metrics are derived from the OWASP Top 10 [[2]](#references) and others are made up to
fit the application context.

### Performance

- **The application should support 500 landing page visitors per second.**

    - all visitors should be served the landing page in under 5 seconds.
    - all text and images should be rendered.

  Derived from the fact that:
  > Reddit received 30 billion average monthly views in 2020.

   ```math
   30,000,000,000 views / 365 days / 24 hours / 60 minutes / 60 seconds ~= 951 views per second
   ```

  This number is scaled down to 500 visitors per second for our application.

- **The application should process 10 posts per second.**

    - 6 of these posts should be text posts ranging from 1,000 to 10,000 characters in length.
    - 3 of these posts should be image posts with images from 1MB to 5MB in size.
    - 1 of these posts should be a video post with a video from 1MB to 10MB in size.
    - all posts should be processed in under 20 seconds.

  Derived from the fact that:
  > 303.4 million posts were uploaded in 2020.

  ```math
  303,400,000 posts / 365 days / 24 hours / 60 minutes / 60 seconds ~= 10 posts per second
  ```

  Obviously, reddit does not receive 10 posts per second equally throughout the whole year but this
  sounds like a reasonable metric for our application, so we stick with it.

- **The application should process 63 comments per second.**

    - all comments should be text comments ranging from 500 to 2,000 characters in length.
    - all comments should be processed in under 10 seconds.

  Derived from the fact that:
  > In 2020, Reddit users posted over two billion comments.

  ```math
  2,000,000,000 comments / 365 days / 24 hours / 60 minutes / 60 seconds ~= 63 comments per second
  ```

This number also seems reasonable for our application.

- **The application should process 1585 votes per second.**

    - all votes should a mix of upvotes and downvotes.

  Derived from the fact that:
  > In 2020, Reddit users posted ... and 49.2 billion upvotes

  ```math
  50,000,000,000 votes / 365 days / 24 hours / 60 minutes / 60 seconds ~= 1585 votes per second
  ```

  Again, this number seems reasonable for our application. Though, it is a bit on the high side.

### Scalability

The scalability metrics are derived from the real reddit application statistics [[1]](#references)
and some are scaled down to a reasonable level for our application. The metrics are as follows:

- **The application should support 30 concurrent users.**

    - all visitors should be served the landing page in under 2 seconds.

  Reddit does not disclose the number of concurrent users, therefore, we will use 30 concurrent
  users as a reasonable metric.

- **The application should support an increase from 30 concurrent users to 300 in less than
  10 seconds.**

    - the influx of users will be **instantaneous**.
    - all visitors should be served the landing page in under 3 seconds.

  Derived from the fact that:
  > Reddit ... reporting that 52 million users logged on daily to the app.

  ```math
  52,000,000 users / 24 hours / 60 minutes / 60 seconds ~= 601 users per second
  ```

- **The application should support an increase from 300 concurrent users to 3000 in a minute.**

  Further clarification:
    - the influx of users will be **gradual**.
    - all visitors should be served the landing page in under 5 seconds.

### Security

- **The application should ensure that sensitive data is encrypted.**

    - all sensitive data should be encrypted both at rest and in transit.
    - all sensitive data should be encrypted using AES-256.
    - sensitive data includes user credentials, personal and financial information.

- **The application should validate all user input to prevent injection attacks.**

    - the input includes credentials and content.

- **The application should have monitoring mechanisms.**

    - this includes logging and alerts.
    - all errors should be logged.
    - all requests that include sensitive data should be logged.
    - alerts should be sent to the administrator's email address.
    - alerts should be sent when there are more than 10 errors in a 30 seconds timeframe.

- **The application support the 0Auth2 standard.**

    - the provider can be any of the following:
        - Google
        - Facebook
        - GitHub
        - LinkedIn

## References

    [1] [Reddit Statistics](https://www.businessofapps.com/data/reddit-statistics/)

    [2] [OWASP Top 10](https://owasp.org/www-project-top-ten/)
