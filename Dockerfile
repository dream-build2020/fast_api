FROM python:3.9

LABEL authors="zhangguangde"

WORKDIR /root

COPY /home/fastapi .

VOLUME /root /home/fastapi

EXPOSE 8088

ENTRYPOINT ["top"]