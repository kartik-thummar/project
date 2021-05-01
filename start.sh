#!/bin/bash
# docker run -d --rm --name djangoapp -v .:./app --network django-db djangoapp

printf '\n # MYSQL database is starting...\n'
docker run -d --rm --name db --network django-db --env-file ./db.env -v /home/kartik/Downloads/p15/db/:/var/lib/mysql mysql
printf '     MYSQL database is started\n'

printf '\n # Django App is starting...\n'
docker run -d --rm --name djangoapp --network django-db -v /home/kartik/Downloads/p15/:/app djangoapp
printf '     Django App is started\n'

printf '\n # Nginx is Starting...\n'
docker run -d --rm --name nginx -p 8000:80 --network django-db -v /home/kartik/Downloads/p15/config/nginx/conf.d:/etc/nginx/conf.d -v /home/kartik/Downloads/p15/home/static:/app/home/static nginx
printf '     Nginx Started\n'

printf "\n # PhpMyAdmin is Starting...\n"
docker run -d --rm --name db-admin -p 8001:80 --env-file phpmyadmin.env -v /home/kartik/Downloads/p15/db/ --network django-db phpmyadmin
printf "     PhpMyAdmin started \n"

printf '\n # Docker Runing Containers...\n'
docker ps
