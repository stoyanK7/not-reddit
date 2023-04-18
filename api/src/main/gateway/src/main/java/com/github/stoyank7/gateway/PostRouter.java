package com.github.stoyank7.gateway;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.cloud.gateway.route.RouteLocator;
import org.springframework.cloud.gateway.route.builder.RouteLocatorBuilder;
import org.springframework.context.annotation.Bean;
import org.springframework.stereotype.Component;

@Component
public class PostRouter {

    @Value("${service.url.post}")
    private String postServiceUrl;

    @Bean
    public RouteLocator buildPostRouter(RouteLocatorBuilder builder) {
        return builder
                .routes()
                .route(p -> p
                        .path("/post/**")
                        .filters(f -> f.rewritePath("/post/(?<segment>.*)", "/${segment}"))
                        .uri(postServiceUrl))
                .build();
    }

}
