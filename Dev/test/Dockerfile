FROM debian:stretch

# MAINTAINER Hukanzen

RUN apt-get -y update && \
	apt-get -y upgrade && \
	apt-get -y install make gcc g++ perl wget &&\
	apt-get -y install libdbd-mysql-perl

# CPANによるインストール
RUN perl -M'CPAN' -e 'my $c = "CPAN::HandleConfig"; $c->load(doit => 1, autoconfig => 1); $c->edit(prerequisites_policy => "follow"); $c->edit(build_requires_install_policy => "yes"); $c->commit' && \
	perl -M'CPAN' -e 'install CGI' &&\
	perl -M'CPAN' -e 'install DBI' 

RUN apt-get -y autoremove && \
	apt-get -y clean


WORKDIR ./src

CMD "/bin/bash"