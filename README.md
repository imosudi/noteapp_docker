# noteapp_docker
Dockerizing a basic CRUD Python web application.

	Ensure that Docker and Docker compose are installed
	docker -v
	docker-compose -v
	Otherwise install docker and docker-compose

Then run the following commands:
	if [[ $(docker -v | echo $?) == 0 ]] && [[ $(docker-compose -v | echo $?) == 0 ]]; then git clone https://github.com/imosudi/noteapp_docker.git && cd noteapp_docker; docker container prune -f && docker image prune -f ; docker-compose up --build ; else  echo "Confirm the proper installation Docker and Docker Compose";  fi


Then visit:
	
	http://server-ip-address/     		noteapp
	
	http://server-ip-address:8080/		app database phpmyadmin

<img src="https://github.com/imosudi/noteapp_docker/blob/master/app/static/images/web_view.png" />







