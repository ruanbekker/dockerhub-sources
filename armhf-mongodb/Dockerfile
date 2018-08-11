FROM arm32v7/debian:jessie-slim

RUN apt update \
    && mkdir -p /data/db \
    && apt install mongodb-server -y \
    && rm -rf /var/cache/apt/* /var/lib/apt/*

ADD ADD boot.sh /boot.sh

CMD ["/bin/bash", "/boot.sh"]
