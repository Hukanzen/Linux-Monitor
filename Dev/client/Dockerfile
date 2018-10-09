FROM debian:stretch

# MAINTAINER Hukanzen

RUN apt-get -y update && \
	apt-get -y upgrade && \
	apt-get -y install libcurl4-gnutls-dev make gcc g++ perl && \
	apt-get -y autoremove && \
	apt-get -y clean


WORKDIR /src

COPY ["./src/Clang/","."]

RUN make


# CMD ["perl","main.pl"]
# CMD /bin/bash
CMD ["./client.out"]
