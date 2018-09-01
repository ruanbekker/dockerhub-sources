## Dockerized Memcached

Memcached on Alpine

## Buidling this Image:

```
$ docker build -t user/repo:tag --build-arg BD=$(date +%F) .
```

## Environment Variables:

Environment variables that is not defined will use the default values

```
MEMUSAGE="${MEMCACHED_MEMUSAGE:-64}"
MAXCONN="${MEMCACHED_MAXCONN:-1024}"
LISTENON="${MEMCACHED_HOST:-127.0.0.1}"
PORT="${MEMCACHED_PORT:-11211}"
```

## Example Run:

```
$ docker run -it --name memcached \
  -p 11211:11211 \
  -e MEMCACHED_MEMUSAGE=128 \
  -e MEMCACHED_MAXCONN=1024 \
  -e MEMCACHED_HOST=127.0.0.1 \
  -e MEMCACHED_PORT=11211 \
  rbekker87/memcached:alpine 
```

## Docker Hub:

- https://hub.docker.com/r/rbekker87/memcached/
