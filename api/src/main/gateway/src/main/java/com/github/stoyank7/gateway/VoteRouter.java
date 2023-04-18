package com.github.stoyank7.gateway;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.cloud.gateway.route.RouteLocator;
import org.springframework.cloud.gateway.route.builder.RouteLocatorBuilder;
import org.springframework.context.annotation.Bean;

public class VoteRouter {

    @Value("${service.url.vote}")
    private String voteServiceUrl;

    @Bean
    public RouteLocator buildVoteRouter(RouteLocatorBuilder builder) {
        return builder
                .routes()
                .route(p -> p
                        .path("/vote/**")
                        .filters(f -> f.rewritePath("/vote/(?<segment>.*)", "/${segment}"))
                        .uri(voteServiceUrl))
                .build();
    }

}
