FROM alpine:3.5

ENV DOCKER_VERSION 18.09.2

RUN apk update && apk add --no-cache g++ make python jq tmux nodejs bash ca-certificates curl git zip unzip && update-ca-certificates && apk add --no-cache nodejs openssl \
 && curl -sl https://download.docker.com/linux/static/stable/x86_64/docker-${DOCKER_VERSION}.tgz --output docker-${DOCKER_VERSION}.tgz \
 && tar xzvf docker-${DOCKER_VERSION}.tgz && rm docker-${DOCKER_VERSION}.tgz && cp docker/* /usr/bin/

RUN git clone https://github.com/c9/core.git /cloud9 \
  && curl -s -L https://raw.githubusercontent.com/c9/install/master/link.sh | bash \
  && /cloud9/scripts/install-sdk.sh \
  && apk del g++ make \
  && rm -rf /var/cache/apk/* /opt/cloud9/.git /tmp/* \
  && npm cache clean

RUN apk add --no-cache libc-dev linux-headers  build-base libffi-dev openssl-dev libxml2-dev libxslt-dev gcc make python3 py2-pip py-virtualenv ruby ruby-dev ruby-irb ruby-bundler ruby-rdoc  
    
RUN apk add --no-cache --virtual .build-deps bash gcc musl-dev openssl go \
    && wget --no-check-certificate -O go.tgz https://dl.google.com/go/go1.12.1.src.tar.gz \
    && tar -C /usr/local -xzf go.tgz \
    && rm -rf go.tgz \
    && cd /usr/local/go/src/ \
    && ./make.bash && mkdir -p /opt/go && apk del .build-deps \
    && echo 'export GOPATH=/opt/go' > /etc/profile.d/golang.sh && echo 'export PATH=$PATH:/usr/local/go/bin:$GOPATH/bin' >> /etc/profile.d/golang.sh 
 
WORKDIR /cloud9

RUN sed -i -e 's_127.0.0.1_0.0.0.0_g' /cloud9/configs/standalone.js

RUN mkdir /workspace
VOLUME /workspace

EXPOSE 8000
EXPOSE 3000

ENV USERNAME username
ENV PASSWORD password

ENTRYPOINT ["sh", "-c", "/usr/bin/node /cloud9/server.js -l 0.0.0.0 -p 8000 -w /workspace -a $USERNAME:$PASSWORD --collab --packed"]
