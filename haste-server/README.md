## Haste Server
Haste Server on Alpine

## Setup the Server:

```
$ docker run -it -p 7777:7777 rbekker87/haste-server:alpine
```

For data persistency `/data`, for more settings see:
- https://www.npmjs.com/package/haste-server#settings

## Setup the Client:

```
haste() {
  data=$(cat);
  curl -X POST -s -d "${data}" http://localhost:7777/documents | awk -F '"' '{print "http://localhost:7777/"$4}';
}
```

Activate:

```
$ source haste-cli.sh
```

Echo something to paste:

```
$ echo "this is a test" | haste
http://localhost:7777/iwemejo
```

Send the content of a file:

```
$ cat myscript.py | haste
http://localhost:7777/uyixosu
```

## Screenshot:

![](screenshots/image1.png)
