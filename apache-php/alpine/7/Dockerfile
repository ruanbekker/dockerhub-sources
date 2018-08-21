FROM rbekker87/alpine:3.8

RUN apk add --no-cache \
    ca-certificates \
    apache2 \
    apache2-utils \
    php7 \
    php7-dev \
    php7-apache2 \
    php7-openssl \
    php7-mysqlnd \
    php7-curl \
    php7-common \
    php7-cli \
    php7-ctype \
    php7-gd \
    php7-imap \
    php7-json \
    php7-soap \
    php7-zlib \
    php7-zip

RUN mkdir /run/apache2 && chown -R apache:apache /run/apache2 \
    && ln -sf /dev/stdout /var/log/apache2/access.log \
    && ln -sf /dev/stderr /var/log/apache2/error.log

COPY httpd.conf /etc/apache2/httpd.conf
ADD htdocs /var/www/localhost/htdocs

CMD ["/usr/sbin/httpd", "-DFOREGROUND", "-f", "/etc/apache2/httpd.conf"]
