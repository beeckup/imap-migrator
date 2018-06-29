FROM alpine:latest
MAINTAINER samuele@nutellino.it


RUN apk add --update python
RUN apk add --update py-pip
ADD imapclient.zip /imapclient.zip
RUN pip install six /imapclient.zip

WORKDIR /

RUN mkdir /database
RUN chmod 777 /database

ADD rootfs /code
WORKDIR /code

CMD ["python","-u","migrate-imap-account-to-gmail.py"]


