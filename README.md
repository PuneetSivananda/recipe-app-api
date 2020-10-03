# recipe-app-api
Recipe app api source code

Start a app
```docker-compose run app sh -c "python manage.py startapp core"```

Run Tests
```docker-compose run app sh -c "python manage.py test && flake8"```

Make Migrations
```docker-compose run app sh -c "python manage.py makemigrations core"```