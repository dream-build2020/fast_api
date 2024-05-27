FROM python:3.9

LABEL authors="zhangguangde"

WORKDIR /root

VOLUME /root /home/fastapi

EXPOSE 8088

ENTRYPOINT ["python3", "main.py"]