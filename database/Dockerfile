# Official mysql image as the base image
FROM mysql


# Add a database
ENV MYSQL_DATABASE noteapp


# All scripts in docker-entrypoint-initdb.d/ 
# are automatically executed during container startup
COPY ./database/sqlscripts/ /docker-entrypoint-initdb.d/


#docker build -t imosudi/noteappdb .
##docker run -d -p 3306:3306 --name imosudi/noteappdb \
##-e MYSQL_ROOT_PASSWORD=supersecret imosudi/noteappdb