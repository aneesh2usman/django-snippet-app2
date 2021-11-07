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
* ```snippets/snippet/ #include operation CRUD```
* ```snippets/tag/  #include operation CRUD```


## API/endpoint examples

### Obtain token (Login)
```
curl --location --request POST 'http://localhost:8000/api/token/' \
--form 'username=admin' \
--form 'password=As@12345'


OUTPUT

{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYzNjM3OTYyMCwianRpIjoiZjU2NTFhOTk3MDEwNGEwNjgzYzg2NmZhYjRiZDVkN2IiLCJ1c2VyX2lkIjoxfQ.m-i03nlmGtCIdiIvoMPGy_x3cAZowg_XDjKlkT3t4w8",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjM2MjkzNTIwLCJqdGkiOiJmMjk2YTdkNzc1ZTA0YmZjODIxMzNmMjQ1NjBiODA4ZiIsInVzZXJfaWQiOjF9._QkI0epmw0lCmF3jybzgkhBV-mMaGoE4xbeV5yBGvuw"
}


```
### Refresh Token
```
curl --location --request POST 'http://localhost:8000/api/token/refresh/' \
--form 'refresh=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYzNjM3NDI1NSwianRpIjoiNjllNDAwZmUzY2E0NGQwZTg3M2I1NTI0ZjFiMmIxOTciLCJ1c2VyX2lkIjoxfQ.dRwUrIllYmpfn9HZShn5jdbfgQt6esXdOoRAdBkkF5A'

OUTPUT

{
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjM2MjkzNjgwLCJqdGkiOiIzMzEwZGI2ZWE2ZDg0NTg0OWI3YjU2MzE4OTU2OTg4ZiIsInVzZXJfaWQiOjF9.V88qfy3_ARe6ckMsgbJI3ff67PILuw1i8BrXl322VoM"
}

```

### Eg : Snippet Action (POST)
```
curl --location --request POST 'http://localhost:8000/snippets/snippet/' \
--header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjM2Mjg4MTU1LCJqdGkiOiI3NDg5NzBkMzYzMjE0ZWQwOTlkMTQ4ZTNlNmY4OTc2MyIsInVzZXJfaWQiOjF9.kM4dZtiCKJHAWigjADpj4XprucUOY1dIsx5vuBhBtgk' \
--header 'Content-Type: application/json' \
--data-raw '{
    "title":"test",
    "message":"test",
    "tags":[
        {"title":"test"}
    ]
    
}


OUTPUT

{
    "id": 6,
    "title": "test",
    "message": "test",
    "tags": [
        {
            "id": 2,
            "title": "test",
            "tag_details": "http://localhost:8000/snippets/tag/2/"
        }
    ],
    "author": "admin",
    "created": "2021-11-07T13:53:59.903365Z",
    "snippet_details": "http://localhost:8000/snippets/snippet/6/"
}
```
### Eg : Snippet Action (PUT)
```
curl --location --request PUT 'http://localhost:8000/snippets/snippet/6/' \
--header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjM2Mjk0MTI5LCJqdGkiOiJkMjgwYzliMzU3NjI0NGZlYTIzNDg1NjU3MWE5OGQyOCIsInVzZXJfaWQiOjF9.PBYvhjsfZQ7v3YyMyEaNUSf5gue7QVcHndT2jK4EVnU' \
--header 'Content-Type: application/json' \
--data-raw '{
    "title":"test",
    "message":"test",
    "tags":[
        {"title":"test3"}
    ]
    
}


OUTPUT

{
    "id": 6,
    "title": "test",
    "message": "test",
    "tags": [
        {
            "id": 1,
            "title": "test",
            "tag_details": "http://localhost:8000/snippets/tag/1/"
        },
        {
            "id": 2,
            "title": "test3",
            "tag_details": "http://localhost:8000/snippets/tag/2/"
        }
    ],
    "author": "admin",
    "created": "2021-11-07T13:53:59.903365Z",
    "snippet_details": "http://localhost:8000/snippets/snippet/6/"
}
```


### Eg : Snippet Action (Delete)
```
curl --location --request DELETE 'http://localhost:8000/snippets/snippet/6/' \
--header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjM2Mjk0MzI1LCJqdGkiOiIwZGVlMTA0MDUzMWM0MDRjYTQ0NzVlNWY2OTNkOGI5YiIsInVzZXJfaWQiOjF9.hWomgchpCKBU2jT4BeaW4UfBBdUAXuBPIwOHJDp2bs4' \
--data-raw ''


OUTPUT

{
    "count": 3,
    "next": "http://localhost:8000/snippets/snippet/6/?page=2",
    "previous": null,
    "results": [
        {
            "id": 3,
            "title": "test3",
            "message": "test",
            "tags": [
                {
                    "id": 1,
                    "title": "test",
                    "tag_details": "http://localhost:8000/snippets/tag/1/"
                }
            ],
            "author": "admin",
            "created": "2021-11-07T07:54:10.278422Z",
            "snippet_details": "http://localhost:8000/snippets/snippet/3/"
        },
        {
            "id": 4,
            "title": "test3",
            "message": "test",
            "tags": [
                {
                    "id": 1,
                    "title": "test",
                    "tag_details": "http://localhost:8000/snippets/tag/1/"
                }
            ],
            "author": "admin",
            "created": "2021-11-07T07:54:24.674901Z",
            "snippet_details": "http://localhost:8000/snippets/snippet/4/"
        }
    ]
}
```


### Eg : Snippet Action (List)
```
curl --location --request GET 'http://localhost:8000/snippets/snippet/' \
--data-raw ''


OUTPUT

{
    "count": 3,
    "next": "http://localhost:8000/snippets/snippet/6/?page=2",
    "previous": null,
    "results": [
        {
            "id": 3,
            "title": "test3",
            "message": "test",
            "tags": [
                {
                    "id": 1,
                    "title": "test",
                    "tag_details": "http://localhost:8000/snippets/tag/1/"
                }
            ],
            "author": "admin",
            "created": "2021-11-07T07:54:10.278422Z",
            "snippet_details": "http://localhost:8000/snippets/snippet/3/"
        },
        {
            "id": 4,
            "title": "test3",
            "message": "test",
            "tags": [
                {
                    "id": 1,
                    "title": "test",
                    "tag_details": "http://localhost:8000/snippets/tag/1/"
                }
            ],
            "author": "admin",
            "created": "2021-11-07T07:54:24.674901Z",
            "snippet_details": "http://localhost:8000/snippets/snippet/4/"
        }
    ]
}
```


### Eg : Snippet Action (Details)
```
curl --location --request GET 'http://localhost:8000/snippets/snippet/5' \
--data-raw ''


OUTPUT

{
    "id": 5,
    "title": "test",
    "message": "test",
    "tags": [
        {
            "id": 2,
            "title": "gfgfgfgghhghg",
            "tag_details": "http://localhost:8000/snippets/tag/2/"
        }
    ],
    "author": "admin",
    "created": "2021-11-07T12:25:12.890631Z",
    "snippet_details": "http://localhost:8000/snippets/snippet/5/"
}
```


### Eg : Tag Action (LIST)
```
curl --location --request GET 'http://localhost:8000/snippets/tag/' \
--data-raw ''

OUTPUT

{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "title": "test",
            "tag_details": "http://localhost:8000/snippets/tag/1/"
        },
        {
            "id": 2,
            "title": "gfgfgfgghhghg",
            "tag_details": "http://localhost:8000/snippets/tag/2/"
        }
    ]
}
```


### Eg : Tag Action (Details)
```
curl --location --request GET 'http://localhost:8000/snippets/tag/1' \
--data-raw ''

OUTPUT

{
    "id": 1,
    "title": "test",
    "tag_details": "http://localhost:8000/snippets/tag/1/"
}
```


## Resources
* Django REST Framework - https://www.django-rest-framework.org
* Django REST Framework Simple JWT - https://github.com/davesque/django-rest-framework-simplejwt
