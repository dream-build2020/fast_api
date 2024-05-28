FROM python:3.9

LABEL authors="zhangguangde"

WORKDIR /root

COPY . .

RUN pip3 install -r requeirements.txt

EXPOSE 8088

ENTRYPOINT ["python3", "main.py"]