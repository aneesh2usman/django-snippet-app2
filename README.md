# django-snippet-app

## Requirements
1. Python 3.6+
1. Pipenv 

## Installation
1. Start Python virtual ENV
```
pipenv shell
```
2. Install dependencies
```
python3 pip install -r requirements.txt
```
3. Run database migrations
```
python manage.py migrate
```
4. Create admin user
```
python manage.py createsuperuser --username admin
```
5. Test
```
python manage.py test
```

## Run application
```
python manage.py runserver 0:8000
```
Once the server is running, visit http://localhost:8000 in your web browser. Now, you should see something like the following:

**Note:** access the Django admin interface here: http://localhost:8000/admin. Example:

## Postman

the Snipped postman Api file location : asset/snippet_project.postman_collection.json


Once the server is running, visit http://localhost:8000 in your web browser. Now, you should see something like the following:


## Endpoints
* ```api/token/```
* ```api/token/refresh/```
* ```snippets/snippet/```
* ```snippets/tag/```


## API/endpoint examples

### Obtain token (Login)
```
curl --location --request POST 'http://localhost:8000/api/token/' \
--form 'username=admin' \
--form 'password=As@12345'

```
### Refresh Token
```
curl --location --request POST 'http://localhost:8000/api/token/refresh/' \
--form 'refresh=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYzNjM3NDI1NSwianRpIjoiNjllNDAwZmUzY2E0NGQwZTg3M2I1NTI0ZjFiMmIxOTciLCJ1c2VyX2lkIjoxfQ.dRwUrIllYmpfn9HZShn5jdbfgQt6esXdOoRAdBkkF5A'

```

### Snippet Action (GET,PUT,POST,DELETE)
```
curl --location --request POST 'http://localhost:8000/snippets/snippet/' \
--header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjM2Mjg4MTU1LCJqdGkiOiI3NDg5NzBkMzYzMjE0ZWQwOTlkMTQ4ZTNlNmY4OTc2MyIsInVzZXJfaWQiOjF9.kM4dZtiCKJHAWigjADpj4XprucUOY1dIsx5vuBhBtgk' \
--header 'Content-Type: application/json' \
--data-raw '{
    "title":"test",
    "message":"test",
    "tags":[
        {"title":"gfgfgfgghhghg"}
    ]
    
}'

```

### Tag Action (GET)
```
curl --location --request GET 'http://localhost:8000/snippets/tag/' \
--data-raw ''

```


## Resources
* Django REST Framework - https://www.django-rest-framework.org
* Django REST Framework Simple JWT - https://github.com/davesque/django-rest-framework-simplejwt
