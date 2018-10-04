FROM httpd:2.4

RUN apt-get -y update && \
	apt-get -y upgrade && \
	apt-get -y install wget make gcc perl libdbd-mysql-perl libgd-graph-perl && \
	perl -M'CPAN' -e 'my $c = "CPAN::HandleConfig"; $c->load(doit => 1, autoconfig => 1); $c->edit(prerequisites_policy => "follow"); $c->edit(build_requires_install_policy => "yes"); $c->commit' && \
	perl -M'CPAN' -e 'install CGI' &&\
	perl -M'CPAN' -e 'install DBI' &&\
	apt-get -y autoremove && \
	apt-get -y clean


RUN sed -ri 's/#LoadModule cgid_module/LoadModule cgid_module/g; \ 
             s/DirectoryIndex index.html/DirectoryIndex index.cgi/g; \ 
             s/Options Indexes FollowSymLinks/Options Indexes FollowSymLinks ExecCGI/g; \
             s/#AddHandler cgi-script .cgi/AddHandler cgi-script .pl .cgi/g' /usr/local/apache2/conf/httpd.conf

RUN rm /usr/local/apache2/htdocs/index.html
