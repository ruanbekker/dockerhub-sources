FROM rbekker87/armhf-alpine:3.8
RUN apk add --update --no-cache nodejs nodejs-npm ca-certificates \
    && rm -rf /tmp/* /var/cache/apk/*
CMD ["node", "-v"]
