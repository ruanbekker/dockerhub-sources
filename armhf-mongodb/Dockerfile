FROM arm32v7/debian:jessie-slim

RUN apt update \
    && mkdir -p /data/db \
    && apt install mongodb-server -y \
    && rm -rf /var/cache/apt/* /var/lib/apt/*

CMD ["/usr/bin/mongod", "--bind_ip", "127.0.0.1", "--port", "27017", "--nojournal"]
