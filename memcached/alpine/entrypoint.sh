#!/bin/sh

set -e

cat > /etc/conf.d/memcached << EOF
MEMCACHED_BINARY="/usr/bin/memcached"
MEMUSAGE="${MEMCACHED_MEMUSAGE:-64}"
MEMCACHED_RUNAS="memcached"
MAXCONN="${MEMCACHED_MAXCONN:-1024}"
LISTENON="${MEMCACHED_HOST:-127.0.0.1}"
PORT="${MEMCACHED_PORT:-11211}"
UDPPORT="${PORT}"
PIDBASE="/var/run/memcached/memcached"
MISC_OPTS=""
EOF

exec "$@"
