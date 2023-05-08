# Testing Strategy

The purpose of this document is to focus on laying down a strategy for testing the [non-functional
requirements](non-functional-requirements.md) of the application.

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


