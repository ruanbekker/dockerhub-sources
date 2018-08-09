#!/bin/sh

echo ""
echo "$(cat /etc/banner)"

echo ""
echo "Alpine Build: ${ALPINE_VERSION}"
echo "Container Hostname: $(hostname)"
echo "Checkout my Docker Blogs: "
echo "- https://sysadmins.co.za/tag/docker"
echo "- http://blog.ruanbekker.com/blog/categories/docker"
echo ""

exec "$@"
