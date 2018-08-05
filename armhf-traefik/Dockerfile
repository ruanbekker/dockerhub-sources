FROM rbekker87/armhf-alpine:3.8

ADD https://github.com/containous/traefik/releases/download/v1.6.0-rc6/traefik_linux-arm /traefik

RUN apk upgrade &&\
    apk add --no-cache ca-certificates &&\
    chmod +x /traefik

EXPOSE 80 8080 443
ENTRYPOINT ["/traefik"]
