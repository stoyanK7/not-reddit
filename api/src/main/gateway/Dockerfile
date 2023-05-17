FROM nginx:1.24-alpine-slim

LABEL org.opencontainers.image.source="https://github.com/stoyanK7/not-reddit"
LABEL org.opencontainers.image.description="Not-reddit API gateway service"
LABEL org.opencontainers.image.licenses="GPL-3.0"

COPY ./src/main/gateway/nginx.conf.template /etc/nginx/templates/nginx.conf.template

EXPOSE 8080
