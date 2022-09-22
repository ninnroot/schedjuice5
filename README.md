# Schedjuice5

The school management system API written
in [Django REST Framework](https://www.django-rest-framework.org/). This would also be the successor of [Schedjuice4](https://github.com/Ninroot-Eater/schedjuice4).

I am trying to make this modular and to be compatible with many educational organizations' systems. After completion, this will be released under the GNU License.



# Technical specs

Python version is 3.9 for compatibility reasons with older packages (but, all seem good so far, 
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
option yet. Will update later).
```shell
docker-compose down api
docker-compose build api --no-cache
docker-compose up api
```

And, that's it. The server will be running on localhost:8000.

# Setting up the development environment
For ease of development, run a Postgres container first and run the Django app with a traditional `python manage.py runserver`.

```bash
docker run -p 5432:5432 -e POSTGRES_PASSWORD=psql_pass -e POSTGRES_DB=psql_db -e POSTGRES_USER=psql_user postgres
```
```
python manage.py runserver
```


# References and additional resources

### Dockerizing the Django project with PostgreSQL
https://computingforgeeks.com/dockerize-django-application-with-postgresql/
https://docs.docker.com/samples/django/


### Stateless JWT authentication
https://django-rest-framework-simplejwt.readthedocs.io/en/latest/stateless_user_authentication.html


### Multiple user types
https://simpleisbetterthancomplex.com/tutorial/2018/01/18/how-to-implement-multiple-user-types-with-django.html


### Using Black
https://black.readthedocs.io/en/stable/usage_and_configuration/the_basics.html


### Using pre-commit
https://pre-commit.com/


### Custom exception handling
https://www.django-rest-framework.org/api-guide/exceptions/#custom-exception-handling


### Field-level permission (I think)
https://stackoverflow.com/questions/19128793/per-field-permission-in-django-rest-framework/32302088#32302088

### On group-within-group relationship
https://stackoverflow.com/questions/4048151/what-are-the-options-for-storing-hierarchical-data-in-a-relational-database

### nested serializer circular problem (solved!)
https://github.com/rsinger86/drf-flex-fields#reference-serializer-as-a-string-lazy-evaluation-

