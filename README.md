# jibrel-test

## Demloyment
- ./manage.py migrate
- ./manage.py deploy

./manage.py deploy запустит первичную загрузку валют в БД

## Start Celery
- celery worker -n worker2@%h -E -A core.celery -Q normal --loglevel=DEBUG
- celery -A core.celery beat --loglevel=debug

## Requests
- curl -X GET   http://127.0.0.1:8000/currencies   -H 'Authorization: Basic dGVzdDpwYXNzd29yZA=='
- curl -X GET   http://127.0.0.1:8000/rate/1   -H 'Authorization: Basic dGVzdDpwYXNzd29yZA=='
- curl -X GET   http://127.0.0.1:8000/rate/2   -H 'Authorization: Basic dGVzdDpwYXNzd29yZA=='
- curl -X GET   http://127.0.0.1:8000/rate/3   -H 'Authorization: Basic dGVzdDpwYXNzd29yZA=='
- curl -X GET   http://127.0.0.1:8000/rate/4   -H 'Authorization: Basic dGVzdDpwYXNzd29yZA=='
- curl -X GET   http://127.0.0.1:8000/rate/5   -H 'Authorization: Basic dGVzdDpwYXNzd29yZA=='
