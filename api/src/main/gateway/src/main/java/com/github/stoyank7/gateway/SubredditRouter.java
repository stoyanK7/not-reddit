package com.github.stoyank7.gateway;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.cloud.gateway.route.RouteLocator;
import org.springframework.cloud.gateway.route.builder.RouteLocatorBuilder;
import org.springframework.context.annotation.Bean;

public class SubredditRouter {

    @Value("${service.url.subreddit}")
    private String subredditServiceUrl;

    @Bean
    public RouteLocator buildSubredditRouter(RouteLocatorBuilder builder) {
        return builder
                .routes()
                .route(p -> p
                        .path("/subreddit/**")
                        .filters(f -> f.rewritePath("/subreddit/(?<segment>.*)", "/${segment}"))
                        .uri(subredditServiceUrl))
                .build();
    }

}
