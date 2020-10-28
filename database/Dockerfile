# Official mysql image as the base image
#FROM mysql
FROM mariadb:10.1

#Setting local timezone
ENV TZ=Africa/Lagos
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone


ENV MYSQL_ROOT_PASSWORD=password


# Add a database
ENV MYSQL_DATABASE=noteappdb
ENV MYSQL_USER=noteappdb
ENV MYSQL_PASSWORD=password

# All scripts in docker-entrypoint-initdb.d/ 
# are automatically executed during container startup

COPY ./sqlscripts/ /docker-entrypoint-initdb.d

#ADD sqlscripts/init.sql /docker-entrypoint-initdb.d

RUN chown -R mysql:mysql /docker-entrypoint-initdb.d/

EXPOSE 3306
