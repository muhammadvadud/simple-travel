#!/bin/bash
#
#while ! nc -z $DB_HOST $DB_PORT; do
#  sleep 2
#  echo "Waiting postgress...."
#done


python3 manage.py collectstatic --noinput
python3 manage.py migrate --noinput
celery -A config worker -l info &
uvicorn config.asgi:application --host 0.0.0.0 --port 8000 --reload --reload-dir core --reload-dir config



exit $?


