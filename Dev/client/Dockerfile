FROM python:3-stretch

# MAINTAINER Hukanzen

RUN	pip3 install psutil ConfigParser

WORKDIR /src
COPY ["./src/","."]

CMD ["python","main.py"]
