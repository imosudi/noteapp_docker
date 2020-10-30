# noteapp_docker
Dockerizing a basic CRUD Python web application.

Ensure that Docker and Docker compose are installed

	git clone https://github.com/imosudi/noteapp_docker.git
	cd noteapp_docker
	docker container prune -f && docker image prune -f
	docker-compose up --build 

Then visit:
	http://server-ip-address/     		noteapp
	http://server-ip-address:8080/		app database phpmyadmin

<img src="https://github.com/imosudi/noteapp_docker/blob/master/app/static/images/web_view.png" />







