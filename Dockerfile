# start from an official image
FROM python:3.8.2

# arbitrary location choice: we can change the directory
RUN mkdir -p /opt/services/djangoapp/src
WORKDIR /opt/services/djangoapp/src

# install our dependencies
RUN pip install gunicorn==20.0.4 django==3.1.7 mysqlclient==1.4.2 django-mysql==3.11.1 mysql-connector-python==8.0.23 pylint-django==2.4.2

# copy our project code
COPY . /opt/services/djangoapp/src

# expose the port 8000
EXPOSE 8000

# define the default command to run when starting the container
CMD ["gunicorn", "--chdir", "home", "--bind", ":8000", "home.wsgi:application"]
