FROM debian:stretch

# MAINTAINER Hukanzen

RUN apt-get -y update && \
	apt-get -y upgrade && \
	apt-get -y install make gcc g++ perl && \
	apt-get -y autoremove && \
	apt-get -y clean

WORKDIR /src

CMD ["perl","main.pl"]