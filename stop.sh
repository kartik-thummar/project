#!/bin/bash

printf "\nRuning Containers djangoapp, nginx, db-admin and db are stopping...\n"
docker stop djangoapp nginx db db-admin

printf "\nRuning Containers :\n"
docker ps