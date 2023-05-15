#!/bin/sh

pip install -q -r /django/requirements.txt &&
python3 manage.py migrate --no-input &&
python3 manage.py collectstatic --no-input &&
python3 manage.py runserver 0.0.0.0:8000
