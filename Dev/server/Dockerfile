FROM httpd:2.4

RUN apt-get -y update && \
	apt-get -y upgrade && \
	apt-get -y install make gcc perl  && \
	apt-get -y autoremove && \
	apt-get -y clean
	
	
RUN sed -ri 's/#LoadModule cgid_module/LoadModule cgid_module/g; \ 
             s/DirectoryIndex index.html/DirectoryIndex index.cgi/g; \ 
             s/Options Indexes FollowSymLinks/Options Indexes FollowSymLinks ExecCGI/g; \
             s/#AddHandler cgi-script .cgi/AddHandler cgi-script .pl .cgi/g' /usr/local/apache2/conf/httpd.conf

RUN rm /usr/local/apache2/htdocs/index.html
