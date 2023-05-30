# Security Testing

// TODO: Add table of contents

## Denial of Service (DoS)

The `https://notredditapi.switzerlandnorth.cloudapp.azure.com/api/post` endpoint is being tested. It was filled with 10 post of relatively large size before the test. Below is a visualization of the data that is being transferred at each request.

![img](img/2023-05-30-page-size.png)

The DoS attack was peformed with _Apache JMeter_ by sending a thousand threads in the span of 10 seconds with each thread requesting forever.

![img](img/2023-05-30-ddos-thread.png)

A total of `37030` requests were sent in the span of `3 minutes 54 seconds`.

![img](img/2023-05-30-ddos-length.png)

![img](img/2023-05-30-ddos-amount-of-requests.png)

The graph below shows the response time results from the run.

![img](img/2023-05-30-ddos-response.png)
Some of the requests failed because the server was not able to handle the load but they were in the `1-2%` range of the total requests.
![img](img/2023-05-30-failures.png)

There is a noticeable drop in response time some 30 seconds into the test because Kubernetes autoscaled the cluster to handle the load.

![img](img/2023-05-30-scale.png)
![img](img/2023-05-30-scale-2.png)

In conclusion, the server handled the load that was sent to it though response times were severely hurt by the load. Normal times have been shown to be `200ms` but now the average was `6000ms`. Unfortunately, I couldn't perform a DDoS attack since I was not in posession of multiple machines.

[The whole DDoS was recorded. Quality is a bit bad but I had to compress it since the original was 80+ MB.](img/DoS%20Attack_compressed.mp4)

### Mitigation

Even though results were not **that** bad, there are still some things that can be done to mitigate the effects of a DoS attack.

I decided to put rate and connection limiting based off this article: https://medium.com/@chadsaun/mitigating-a-ddos-attack-with-ingress-nginx-and-kubernetes-12f309072367

The limit is connections per IP to 2 and 120 requests per minute. 120 requests might be on the low side but it's a good starting point. The limits can be changed in the future with testing if needed.

File: [api.ingress.yml](../k8s/api-ingress.yml)
```yaml
nginx.ingress.kubernetes.io/limit-connections: '2'
nginx.ingress.kubernetes.io/limit-rpm: '120'
```

To test if this does a better job, I ran a similar test as before. This time the amount of threads was `2` since this is how many the ingress allows. The loop count was set to `150`. Theoretically, we expect `1/3` of those requests to get refused.

![img](img/2023-05-30-ddos-mitigation-thread.png)

And this is what happened. Around the `261st` request, the rest were outright refused.

![img](img/2023-05-30-ddos-mitigation-table.png)

Below is the response time chart. An interesting drop in response time can be seen at the end. This is when the requests were refused.

![img](img/2023-05-30-ddos-mitigation-result.png)

## SQL Injection

## XSS
