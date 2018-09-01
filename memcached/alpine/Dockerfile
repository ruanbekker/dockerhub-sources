FROM alpine:3.7

ARG BD
LABEL built_date=${BD}

RUN apk --no-cache add memcached
COPY boot.sh /boot.sh
RUN chmod +x /boot.sh

USER memcached
CMD ["/boot.sh"]
