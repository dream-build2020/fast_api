FROM python:3.9

LABEL authors="zhangguangde"

WORKDIR /root

ADD /home/fast_api /root

EXPOSE 8088

ENTRYPOINT ["python3", "/root/main.py"]