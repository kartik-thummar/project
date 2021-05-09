# project

<!--<br>Services are built once and then tagged, by default as project_service. 
<br>For example, composetest_db. If the Compose file specifies an image name, the image is tagged with that name, 
substituting any variables beforehand.
<br>If you change a service’s Dockerfile or the contents of its build directory, run "docker-compose build" to rebuild it.
<br>command - docker-compose build -->

<!--<br><br>Builds, (re)creates, starts, and attaches to containers for a service.
<!--<br>command - docker-compose up

<!--<br>Go to http://0.0.0.0:8000 to see django application through nginx -->

<br>Create common network for 4 containers internal communication
<br> <b>sudo docker network create django-db</b>

<br> Build image of django application
<br><b> sudo docker build -t djangoapp -f djangoapp.Dockerfile . </b>

<br>Give permissions to execute script
<br><b> sudo chmod +x start.sh stop.sh </b>

<br>To start all 4 containers
<br><b> sudo ./start.sh </b>

<br>To stop all 4 containers
<br><b> sudo ./stop.sh</b>

<br> Serve djangoapp at </br>
<br><b> http://localhost:8000/ </b></br>

<br> Serve PhpMyAdmin at </br>
<br><b> http://localhost:8001/ </b></br>
