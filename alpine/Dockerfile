FROM scratch

MAINTAINER Ruan Bekker <ruan@ruanbekker.com>
ENV alpine_version apline-3.8.0
LABEL creation_date=2018.08.08

ADD alpine-minirootfs-3.8.0-x86_64.tar.gz /
ADD entrypoint.sh /
ADD banner /etc/banner

RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
CMD ["/bin/sh"]
