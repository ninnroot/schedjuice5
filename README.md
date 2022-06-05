# SuConnect

The financial module of the SuConnect platform written
in [Django REST Framework](https://www.django-rest-framework.org/), and is named __Schedjuice5__.
This would also be the successor of [Schedjuice4](https://github.com/Ninroot-Eater/schedjuice4).


# Technical specs

Python version is 3.9 for compatibility reason with older packages (but, all seem good so far, 
so might update in the future).

# Project setup
You will need Docker installed in your system. See [here](https://docs.docker.com/get-docker/) on how to install Docker.
Please also come and ask me for the .env file.
```shell
# start the database container first
docker-compose up db

# and then start the application itself
docker-compose up api 
```

For updating the server for source code changes, run this command. (probably not the perfect
option yet. Will update later)
```shell
docker-compose down api
docker-compose up api --force-recreate
```

And, that's it. The server will be running on localhost:8000.


# References and additional resources

### Dockerizing the Django project with PostgreSQL
https://computingforgeeks.com/dockerize-django-application-with-postgresql/
https://docs.docker.com/samples/django/

