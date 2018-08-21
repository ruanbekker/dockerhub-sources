FROM rbekker87/alpine:3.7

RUN apk add --no-cache \
    ca-certificates \
    apache2 \
    apache2-utils \
    php5 \
    php5-dev \
    php5-apache2 \
    php5-openssl \
    php5-mysql \
    php5-curl \
    php5-common \
    php5-cli \
    php5-ctype \
    php5-gd \
    php5-imap \
    php5-json \
    php5-soap \
    php5-zlib \
    php5-zip

RUN mkdir /run/apache2 && chown -R apache:apache /run/apache2 \
    && ln -s $(which php5) /usr/bin/php \
    && ln -sf /dev/stdout /var/log/apache2/access.log \
    && ln -sf /dev/stderr /var/log/apache2/error.log

COPY httpd.conf /etc/apache2/httpd.conf
ADD htdocs /var/www/localhost/htdocs

CMD ["/usr/sbin/httpd", "-DFOREGROUND", "-f", "/etc/apache2/httpd.conf"]
