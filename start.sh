#!/bin/bash

red='\033[0;31m'
green='\033[0;32m'
NC='\033[0m'

printf '\n # MYSQL database is starting...\n'
if (docker run -d --rm --name db --network django-db --env-file ./db.env -v $(pwd)/db/:/var/lib/mysql mysql); then 
    printf "${green}  MYSQL database is started ${NC}\n"
else 
    printf "${red}  Faild to start database.${NC}\n"
fi

printf '\n # Django App is starting...\n'
if (docker run -d --rm --name djangoapp --network django-db -v $(pwd)/:/app djangoapp); then
    printf "${green}  Django App is started ${NC}\n"
else
    printf "${red}  Faild to start django application.${NC}\n"
fi

printf '\n # Nginx is Starting...\n'
if (docker run -d --rm --name nginx -p 8000:80 --network django-db -v $(pwd)/config/nginx/conf.d:/etc/nginx/conf.d -v $(pwd)/home/static:/app/home/static nginx); then
    printf "${green}  Nginx Started ${NC}\n"
else
    printf "${red}  Faild to start Nginx.${NC}\n"
fi

printf "\n # PhpMyAdmin is Starting...\n"
if (docker run -d --rm --name db-admin -p 8001:80 --env-file phpmyadmin.env -v $(pwd)/db/ --network django-db phpmyadmin); then
    printf "${green}  PhpMyAdmin started ${NC}\n"
else
    printf "${red}  Faild to start PhpMyAdmin.${NC}\n"
fi

printf "${green}\n # Docker Runing Containers...${NC}\n"
docker ps
