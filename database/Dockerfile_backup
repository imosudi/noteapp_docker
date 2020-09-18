# Official mysql image as the base image
#FROM mysql
FROM mariadb

#RUN sed -e '/BBB/s/^/#/g' -i /etc/mysql/my.cnf

RUN sed  '/\[mysqld\]/a skip-networking'  -i /etc/mysql/my.cnf 
RUN sed  '/\[mysqld\]/a  bind-address = 0.0.0.0' -i /etc/mysql/my.cnf


#Use docker secret in PRODUCTION
#ENV MYSQL_ROOT_PASSWORD PASSWimosudi@gmail.co767868FFGFFDD#m
ENV MYSQL_ROOT_PASSWORD password


# Add a database
ENV MYSQL_DATABASE noteappdb

# All scripts in docker-entrypoint-initdb.d/ 
# are automatically executed during container startup

COPY ./sqlscripts/ /docker-entrypoint-initdb.d/

EXPOSE 3306

#docker build -t imosudi/noteappdb .
##docker run -d -p 3306:3306 --name imosudi/noteappdb \
##-e MYSQL_ROOT_PASSWORD=supersecret imosudi/noteappdb



