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

## Run a Memcache Container:

```
$ docker run -it --name memcached \
  -p 11211:11211 \
  -e MEMCACHED_MEMUSAGE=128 \
  -e MEMCACHED_MAXCONN=1024 \
  -e MEMCACHED_HOST=127.0.0.1 \
  -e MEMCACHED_PORT=11211 \
  rbekker87/memcached:alpine 
```

## Run the Example Client

Writes 100000 keys with random data to memcached, and reads one random key:

```
$ python client.py
7ukk1iw20g9fy872heiw9thpt5zlrf1wx5ujc7cd1cdvzc6twgorfo70r50vc9e0fr7yvfxqnk5n8yptardvskfz9riup364iqbj57qvrjax0stb9sj6xt69uv9wkcpx87yv3mz6t8sl44sywd14amepqm2u9bhie77qmoyubaasbh8e6gijie0ktfp1dlqk5sm7w4h45uzryaevh9nd3uayrfr879ug5yfuxqe5e466egl1cbgimyl7v0xwu0yx5epo7sxtn5p7pcetmk4ughk9q3ov7i66pv9nett1n7fk85808cdfe9uiev41qtzlbwmeuf6siyrlt4gbzkithzmxb50y10eyrv6jimoxoyv4e68a6tcj9p93dsdgrodh5558jeor8rooagyk4cri4khuf7oalld8mqsiqtt2mmqxg71tkrr3lcbblymj384kzsbnk7rc8dr78r2a73aalep9u3zm26jvk116zcntmjfk3d1yyt7bg5glhrqky0e0
Took 30 seconds to write 100000 using 1 node
```

If the key was evicted, you will find this:

```
None
Took 30 seconds to write 100000 using 1 node
```

## Docker Hub:

- https://hub.docker.com/r/rbekker87/memcached/
