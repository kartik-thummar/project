# project

<!--<br>Services are built once and then tagged, by default as project_service. 
<br>For example, composetest_db. If the Compose file specifies an image name, the image is tagged with that name, 
substituting any variables beforehand.
<br>If you change a service’s Dockerfile or the contents of its build directory, run "docker-compose build" to rebuild it.
<br>command - docker-compose build -->

<!--<br><br>Builds, (re)creates, starts, and attaches to containers for a service.
<!--<br>command - docker-compose up

<!--<br>Go to http://0.0.0.0:8000 to see django application through nginx -->

<br>Create network for project
<br> <b>sudo docker network create django-db</b>

<br> Build image of django application
<br><b> sudo docker build -t djangoapp -f djangoapp.Dockerfile .

<br>Give permissions to execute script
<br><b> sudo chmod +x start.sh stop.sh </b>

<br>To start containers
<br><b> sudo ./start.sh </b>

<br>To stop containers
<br>< sudo ./stop.sh</b>
