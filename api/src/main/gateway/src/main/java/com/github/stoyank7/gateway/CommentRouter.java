package com.github.stoyank7.gateway;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.cloud.gateway.route.RouteLocator;
import org.springframework.cloud.gateway.route.builder.RouteLocatorBuilder;
import org.springframework.context.annotation.Bean;

public class CommentRouter {

    @Value("${service.url.comment}")
    private String commentServiceUrl;

    @Bean
    public RouteLocator buildCommentRouter(RouteLocatorBuilder builder) {
        return builder
                .routes()
                .route(p -> p
                        .path("/comment/**")
                        .filters(f -> f.rewritePath("/comment/(?<segment>.*)", "/${segment}"))
                        .uri(commentServiceUrl))
                .build();
    }

}
