# Apache with PHP

Dockerized Minimal Apache with PHP 7

## Releases

- rbekker87/apache-php:7

```
Distro: Alpine 3.7
Apahce: 2.4.34-r0
PHP: 7.2.8-r0
Content Path: /var/www/localhost/htdocs
```

## Usage:

```
$ docker run -it -p 80:80 rbekker87/apache-php:7

       ______       _____
______ ___  /__________(_)___________
_  __ `/_  /___  __ \_  /__  __ \  _ \
/ /_/ /_  / __  /_/ /  / _  / / /  __/
\__,_/ /_/  _  .___//_/  /_/ /_/\___/
            /_/

Alpine Build: apline-3.8.0
Container Hostname: 43a420a7bc51
Checkout my Docker Blogs:
- https://sysadmins.co.za/tag/docker
- http://blog.ruanbekker.com/blog/categories/docker

[Tue Aug 21 14:13:38.188388 2018] [mpm_prefork:notice] [pid 1] AH00163: Apache/2.4.34 (Unix) PHP/7.2.8 configured -- resuming normal operations
[Tue Aug 21 14:13:38.188448 2018] [core:notice] [pid 1] AH00094: Command line: '/usr/sbin/httpd -D FOREGROUND -f /etc/apache2/httpd.conf'
```

Client:

```
$ curl -i http://localhost:80/
HTTP/1.1 200 OK
Date: Tue, 21 Aug 2018 14:13:58 GMT
Server: Apache/2.4.34 (Unix)
X-Powered-By: PHP/7.2.8
Content-Length: 30
Content-Type: text/html; charset=UTF-8

My Hostname is: 43a420a7bc51
```

## Dockerhub:

- https://hub.docker.com/r/rbekker87/apache-php/

## Notes:

- [Graze:Docker-PHP-Alpine](https://github.com/graze/docker-php-alpine/tree/master/7.2)
