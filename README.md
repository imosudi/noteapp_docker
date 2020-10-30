# noteapp_docker
Dockerizing a basic CRUD Python web application.

<img src="https://github.com/imosudi/noteapp_docker/blob/master/app/static/images/web_view.png" />

	Ensure that Docker and Docker compose are installed
	docker -v
	docker-compose -v
	Otherwise, install docker and docker-compose
	
	Ubuntu 18.04 LTS
	sudo apt-get update && sudo apt-get upgrade -y && sudo apt-get -y install docker docker-compose

Then run the following commands:
	
	if ! command -v docker &> /dev/null && ! command -v docker-compose &> /dev/null ; then   echo "docker or docker-compose could not be found" ; echo "Confirm the proper installation Docker and Docker Compose"; else git clone https://github.com/imosudi/noteapp_docker.git ; cd noteapp_docker; sudo docker container prune -f && sudo docker image prune -f ; sudo docker-compose up --build; fi

Then visit:
	
	http://server-ip-address/     		noteapp
	
	http://server-ip-address:8080/		app database phpmyadmin









