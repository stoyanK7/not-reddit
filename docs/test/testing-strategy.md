# Testing Strategy

The purpose of this document is to focus on laying down a strategy for testing the [non-functional
requirements](../non-functional-requirements.md) of the application.

The plan is to execute this strategy one time immediately after it is defined and then to execute it
after every major change to the application to ensure the metrics are still being met or even
better, improved.

I will strive to make these tests as automated as possible and remove manual work. Preferably,
they will be executed from a bash script.

For all tests, the application will be deployed to a staging environment and the tests will be
executed against that environment.

## Performance

### UI

The performance of the UI will be measured using
[_Lighthouse_](https://developers.google.com/web/tools/lighthouse/). The team at Google is regularly
doing research on the user's perception of performance and therefore have a good idea on how weigh
[performance
score](https://developer.chrome.com/en/docs/lighthouse/performance/performance-scoring/).

_Lighthouse_ will be installed locally and tested against the staging environment. From
[the documentation](https://github.com/GoogleChrome/lighthouse#using-the-node-cli), lighthouse can
be used as a node module and therefore can be integrated into a bash script.

### API

The performance of the API will be measured using [_Apache JMeter_](http://jmeter.apache.org/). The
application's GUI should be used to create a test plan and then the test plan should  be exported to
a `.jmx` file and executed from a bash script.
[_JMeter_ has CLI support](https://blog.e-zest.com/how-to-run-jmeter-in-non-gui-mode/).

## Scalability

The performance will be tested using _Lighthouse_ while the system is under load by
_JMeter_.

## Security

For penetration testing, [_OWASP ZAP_](https://owasp.org/www-project-zap/) will be used. The project
provides a [docker image](https://www.zaproxy.org/docs/docker/about/) and is beginner-friendly. Each
security requirement will be tested manually and then automated using _ZAP_ if possible.

## Notes

For performance and scalability, it is suggested that all security is disabled. This is because
it is hard to simulate thousands of Azure AD accounts. Therefore, the authentication service has
been set to always return 202 no matter.

All requests will have to include an `Authorization` header with the following token:
```
eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImJXOFpjTWpCQ25KWlMtaWJYNVVRRE5TdHZ4NCJ9.eyJ2ZXIiOiIyLjAiLCJpc3MiOiJodHRwczovL2xvZ2luLm1pY3Jvc29mdG9ubGluZS5jb20vOTE4ODA0MGQtNmM2Ny00YzViLWIxMTItMzZhMzA0YjY2ZGFkL3YyLjAiLCJzdWIiOiJBQUFBQUFBQUFBQUFBQUFBQUFBQUFKX1dzWURTa2tzeGpZMXlwNGVzR21rIiwiYXVkIjoiZDQ0OGQxOWMtYjdjMy00YzFmLThjMWItZTcyNmIzYTNiYTg4IiwiZXhwIjoxNjg0Nzc5MzM4LCJpYXQiOjE2ODQ3NzU0MzgsIm5iZiI6MTY4NDc3NTQzOCwibmFtZSI6IlN0b3lhbiBLb3N0YWRpbm92IiwicHJlZmVycmVkX3VzZXJuYW1lIjoic3RveWFuazEyN0BnbWFpbC5jb20iLCJvaWQiOiIwMDAwMDAwMC0wMDAwLTAwMDAtZDUxMC1iZTk1NGUwMDg1NzEiLCJ0aWQiOiI5MTg4MDQwZC02YzY3LTRjNWItYjExMi0zNmEzMDRiNjZkYWQiLCJhenAiOiJkNDQ4ZDE5Yy1iN2MzLTRjMWYtOGMxYi1lNzI2YjNhM2JhODgiLCJzY3AiOiJ1c2VyX2ltcGVyc29uYXRpb24iLCJhenBhY3IiOiIwIiwiYWlvIjoiRGV6UGRlcFU0ZU1RRlVsMXhwMDgyU25xdFFBZGdqVVhwTHlxUGlReDhQczlNVExUOEJJdDlOamcqYmFqQlBZMUhGZFNiRUdEVSFQUWVHNWhtYjhLZWtvb2k1NnVSbXkhTjFYTkdvYlljdEZkSmh1VUtlTjFGQ1dVaTdXU0IyeFNRc0tYRnZEWDEqTVBhMGw5WjVEclV5QSQifQ.wCCB4mPVDq76l2e9t78dpvrdK3QsmN8a2yDTUJvdwVPdHKLFTSu7WFZ8tmiIqagsGqqQdJ2ZMubhBEDKa_sB__iMgT6VJfJO_epsgnJnWBGg54qipWm3rlquWstsRnK5sde1I5F2cUCauKr1jphMDVccUqr1v6Fv4FsbHhkGQz0twIQm7RMXxQ8mUt6XZ-YjsPsWbcoVvVh9GPu5grF3CND5pxI7FwFt_RRhZy3_DirrSmc1GjhPablASTsCRctOFcGn_aYS6_MTrSk-yRLfvildObjgugGPAAZxizcr0M5ybW2bXoKDCAsTReYgzurz8Oyq5HcxaaDRtER3cTle9g
```
These are the 2 important fields in this token. Any token that contains those in the payload will
be fine.
```json
{
  "preferred_username": "stoyank127@gmail.com",
  "oid": "00000000-0000-0000-d510-be954e008571"
}
```

The email service is turned off as well. It will only print `Sending email...` to the console.

```bash
export JWT_TOKEN=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImJXOFpjTWpCQ25KWlMtaWJYNVVRRE5TdHZ4NCJ9.eyJ2ZXIiOiIyLjAiLCJpc3MiOiJodHRwczovL2xvZ2luLm1pY3Jvc29mdG9ubGluZS5jb20vOTE4ODA0MGQtNmM2Ny00YzViLWIxMTItMzZhMzA0YjY2ZGFkL3YyLjAiLCJzdWIiOiJBQUFBQUFBQUFBQUFBQUFBQUFBQUFKX1dzWURTa2tzeGpZMXlwNGVzR21rIiwiYXVkIjoiZDQ0OGQxOWMtYjdjMy00YzFmLThjMWItZTcyNmIzYTNiYTg4IiwiZXhwIjoxNjg0Nzc5MzM4LCJpYXQiOjE2ODQ3NzU0MzgsIm5iZiI6MTY4NDc3NTQzOCwibmFtZSI6IlN0b3lhbiBLb3N0YWRpbm92IiwicHJlZmVycmVkX3VzZXJuYW1lIjoic3RveWFuazEyN0BnbWFpbC5jb20iLCJvaWQiOiIwMDAwMDAwMC0wMDAwLTAwMDAtZDUxMC1iZTk1NGUwMDg1NzEiLCJ0aWQiOiI5MTg4MDQwZC02YzY3LTRjNWItYjExMi0zNmEzMDRiNjZkYWQiLCJhenAiOiJkNDQ4ZDE5Yy1iN2MzLTRjMWYtOGMxYi1lNzI2YjNhM2JhODgiLCJzY3AiOiJ1c2VyX2ltcGVyc29uYXRpb24iLCJhenBhY3IiOiIwIiwiYWlvIjoiRGV6UGRlcFU0ZU1RRlVsMXhwMDgyU25xdFFBZGdqVVhwTHlxUGlReDhQczlNVExUOEJJdDlOamcqYmFqQlBZMUhGZFNiRUdEVSFQUWVHNWhtYjhLZWtvb2k1NnVSbXkhTjFYTkdvYlljdEZkSmh1VUtlTjFGQ1dVaTdXU0IyeFNRc0tYRnZEWDEqTVBhMGw5WjVEclV5QSQifQ.wCCB4mPVDq76l2e9t78dpvrdK3QsmN8a2yDTUJvdwVPdHKLFTSu7WFZ8tmiIqagsGqqQdJ2ZMubhBEDKa_sB__iMgT6VJfJO_epsgnJnWBGg54qipWm3rlquWstsRnK5sde1I5F2cUCauKr1jphMDVccUqr1v6Fv4FsbHhkGQz0twIQm7RMXxQ8mUt6XZ-YjsPsWbcoVvVh9GPu5grF3CND5pxI7FwFt_RRhZy3_DirrSmc1GjhPablASTsCRctOFcGn_aYS6_MTrSk-yRLfvildObjgugGPAAZxizcr0M5ybW2bXoKDCAsTReYgzurz8Oyq5HcxaaDRtER3cTle9g
export API_URL=https://notredditapi.switzerlandnorth.cloudapp.azure.com
./.dev/setup-testing-environment.sh
```
