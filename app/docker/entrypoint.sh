#!/bin/sh

export $(cat /django/app/.env | xargs) && rails c
python3 manage.py migrate --no-input
python3 manage.py collectstatic --no-input
