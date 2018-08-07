FROM rbekker87/armhf-alpine:3.8

RUN apk add --no-cache nginx \
    && mkdir /run/nginx \
    && ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log \
    && chown -R nginx:nginx /var/lib/nginx /run/nginx

CMD ["nginx", "-g", "daemon off;"]
