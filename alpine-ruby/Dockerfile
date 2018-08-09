FROM rbekker87/alpine:3.8

MAINTAINER Ruan Bekker <ruan@ruanbekker.com>

ENV APLINE_VERSION apline-3.8.0
LABEL CREATION_DATE=2018.08.08

ADD banner /etc/banner
ADD entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh \
  && apk add --no-cache build-base ruby ruby-dev ruby-irb ruby-bundler ruby-rdoc openssl-dev \
  && gem install json --no-rdoc --no-ri \
  && gem cleanup \
  && rm -rf /usr/lib/ruby/gems/*/cache/* /var/cache/apk/* /tmp/* /var/tmp/*

ENTRYPOINT ["/entrypoint.sh"]
CMD ["/bin/sh"]
