FROM debian:stretch

# MAINTAINER Hukanzen

RUN apt-get -y update && \
	apt-get -y upgrade && \
	apt-get -y install libcurl4-gnutls-dev make gcc g++ perl libwww-perl

# CPANによるインストール
# RUN perl -M'CPAN' -e 'my $c = "CPAN::HandleConfig"; $c->load(doit => 1, autoconfig => 1); $c->edit(prerequisites_policy => "follow"); $c->edit(build_requires_install_policy => "yes"); $c->commit' && \
	# perl -M'CPAN' -e 'install URI::Fetch'

RUN apt-get -y autoremove && \
	apt-get -y clean


WORKDIR /src

CMD ["perl","main.pl"]
#CMD /bin/bash
