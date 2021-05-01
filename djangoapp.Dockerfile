FROM python:3.8.2

RUN mkdir -p /app/
WORKDIR /app/

RUN pip install gunicorn==20.0.4 django==3.1.7 mysqlclient==1.4.2 django-mysql==3.11.1 mysql-connector-python==8.0.23 pylint-django==2.4.2

COPY . /app/

CMD ["gunicorn", "--chdir", "home", "--bind", ":8000", "home.wsgi:application"]
