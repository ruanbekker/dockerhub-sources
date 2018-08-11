#!/usr/bin/env bash
set -e

/usr/bin/mongod --bind_ip "${BIND_IP:-127.0.0.1}" --port "${BIND_PORT:-27017}" --nojournal
