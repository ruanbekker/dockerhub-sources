FROM alpine:3.7

ARG BD
LABEL built_date=${BD}

COPY boot.sh /boot.sh
RUN apk --no-cache add memcached && chmod +x /boot.sh

USER memcached
CMD ["/boot.sh"]
