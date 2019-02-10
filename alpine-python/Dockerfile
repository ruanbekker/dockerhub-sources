FROM alpine:latest

MAINTAINER Ruan Bekker <ruan@ruanbekker.com>

ADD banner /etc/banner
ADD entrypoint.sh /entrypoint.sh

RUN apk add --no-cache \
    python \
    py2-pip \
    # && chmod +x /entrypoint.sh \
    && rm -rf /var/cache/apk/*

CMD ["/bin/sh"]
