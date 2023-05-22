# Non-Functional Requirements

## Introduction

The purpose of this document is to describe the non-functional requirements of the project.

[_Testing Strategy_](test/testing-strategy.md) and [_Test Report_](test/test-report.md) document
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

- **The application should be protected from SQL injections.**

  From `Misuse Case 1: SQL Injection`.

  To mitigate this misuse case, the application should use avoid using raw SQL queries and instead
  rely on an ORM library to generate the SQL queries [[3]](#references) - `SQLAlchemy`. Moreover,
  the application should ensure that sensitive data is encrypted - both at rest and in transit.
  Sensitive data includes user credentials, personal and financial information. The encryption
  method should be recommended by the developers of the technology used in the application.

- **The application should have monitoring mechanisms.**

  From `Misuse Case 2: Denial-of-Service (DoS)` and `Misuse Case 3: Spamming`.

  To mitigate this misuse case, the application should have monitoring mechanisms in place
  [[4]](#references). This includes logging and alerts. All errors should be logged. All requests
  that include sensitive data should be logged. Alerts should be sent to the administrator's email
  address. In addition, rate limiting of 10 requests per 5 seconds for unregistered users should be
  imposed. And rate limiting of 30 requests per 5 seconds for registered users should be imposed.
  Finally, if those limits are exceeded, the user should be asked to fill in a CAPTCHA.

- **The application should allow only certain media filetypes of uploads.**

  From `Misuse Case 4: Malware and Phishing`.

  To mitigate this misuse case, the application should allow only certain media filetypes of
  uploads. The allowed filetypes should be limited to the following:
    - Image: `jpg`, `jpeg`, `png`, `gif`
    - Video: `mp4`, `webm`

  Links to external media should also be allowed. The application should also visually warn
  users
  that this is an external link. Possibly, by adding a small icon next to the link. Ideally, it
  should compare the link against a list of known malicious websites [[5]](#references).

- **The application support the 0Auth2 standard.**

  The provider of the 0Auth2 service could be any of the following:
    - Google
    - Facebook
    - GitHub
    - LinkedIn

  Or the application could implement its own 0Auth2 service.

## References

    [1] [Reddit Statistics](https://www.businessofapps.com/data/reddit-statistics/)

    [2] [OWASP Top 10](https://owasp.org/www-project-top-ten/)

    [3] [Stackoverflow answer on SQL Injections in SQLAlchemy](https://stackoverflow.com/a/6501664/9553927)

    [4] [What is DDoS Mitigation & 6 Tips to Prevent an Attack](https://www.liquidweb.com/blog/ddos-mitigation/)

    [5] [List of known malicious websites](https://www.kaggle.com/datasets/sid321axn/malicious-urls-dataset)
