#!/usr/bin/env sh
sed -i "s/UPSTREAM_NAME/${UPSTREAM_NAME:-127.0.0.1}/g" /etc/nginx/conf.d/web.conf
sed -i "s/UPSTREAM_PORT/${UPSTREAM_PORT:-80}/g" /etc/nginx/conf.d/web.conf
nginx -g "daemon off;"
