FROM rbekker87/armhf-alpine:3.8

RUN apk add --no-cache nginx \
    && adduser -S www-data \
    && mkdir /run/nginx \
    && ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log \
    && chown -R www-data:www-data /var/lib/nginx /run/nginx

CMD ["nginx", "-g", "daemon off;"]
