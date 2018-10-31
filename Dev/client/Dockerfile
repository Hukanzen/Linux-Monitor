FROM python:3-stretch

# MAINTAINER Hukanzen

# RUN apt-get -y update && \
# 	apt-get -y upgrade && \
# 	apt-get -y install libcurl4-gnutls-dev make gcc g++ && \
# 	apt-get -y autoremove && \
# 	apt-get -y clean


RUN pip3 install ConfigParser

WORKDIR /src
COPY ["./src/","."]
# RUN make


# CMD ["perl","main.pl"]
# CMD /bin/bash
CMD ["python","main.py"]
