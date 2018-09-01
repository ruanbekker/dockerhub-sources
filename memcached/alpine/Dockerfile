FROM rbekker87/alpine:3.8

ARG BD
LABEL built_date=${BD}

COPY entrypoint.sh /entrypoint.sh
RUN apk --no-cache add memcached && chown memcached /etc/conf.d/memcached && chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

USER memcached
CMD ["memcached"]
