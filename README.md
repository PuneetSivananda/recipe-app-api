@username LondonAppDeveloper

# recipe-app-api

Recipe app api source code

Start a app
`docker-compose run app sh -c "python manage.py startapp core"`

Run Tests
`docker-compose run app sh -c "python manage.py test && flake8"`

Make Migrations
`docker-compose run app sh -c "python manage.py makemigrations core"`

## Remove the pyc files

TODO: Automate the code

```bash
find . -name "*.pyc" -exec rm -f {} \;
```

## Docker Postgres Debugging

```bash
sudo lsof -i:5432
sudo pkill -u postgres
```

## Run API Server

docker-compose run --rm app sh -c "python manage.py wait_for_db && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"

docker-compose run --rm app sh -c "python manage.py runserver 0.0.0.0:8000"


# Command for start
1.1 `docker-compose run app sh -c "django-admin.py startproject app ."`