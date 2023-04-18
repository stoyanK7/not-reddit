package com.github.stoyank7.gateway;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.cloud.gateway.route.RouteLocator;
import org.springframework.cloud.gateway.route.builder.RouteLocatorBuilder;
import org.springframework.context.annotation.Bean;
import org.springframework.stereotype.Component;

@Component
public class UserRouter {

    @Value("${service.url.user}")
    private String userServiceUrl;

    @Bean
    public RouteLocator buildUserRouter(RouteLocatorBuilder builder) {
        return builder
                .routes()
                .route(p -> p
                        .path("/user/**")
                        .filters(f -> f.rewritePath("/user/(?<segment>.*)", "/${segment}"))
                        .uri(userServiceUrl))
                .build();
    }

}
