FROM alpine

RUN apk update && apk upgrade && apk add curl tar make gcc build-base wget gnupg

RUN mkdir -p /usr/src/perl
WORKDIR /usr/src/perl

RUN curl -SLO https://www.cpan.org/src/5.0/perl-5.30.0.tar.gz && \
	tar --strip-components=1 -xzf perl-5.30.0.tar.gz -C /usr/src/perl && \
	rm perl-5.30.0.tar.gz && \
	./Configure -des \
		-Duse64bitall \
		-Dcccdlflags='-fPIC' \
		-Dcccdlflags='-fPIC' \
		-Dccdlflags='-rdynamic' \
		-Dlocincpth=' ' \
		-Duselargefiles \
		-Dusethreads \
		-Duseshrplib \
		-Dd_semctl_semun \
		-Dusenm && \
	make libperl.so && \
	make -j$(nproc) && \
	true TEST_JOBS=$(nproc) make test_harness && \
	make install
	
RUN curl -LO http://xrl.us/cpanm && \
	chmod +x cpanm && \
	./cpanm App::cpanminus && \
	rm -fr ./cpanm /root/.cpanm /usr/src/perl
	
RUN cpanm Net::SNMP && cpanm Net::SNMP
	