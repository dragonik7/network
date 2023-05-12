#!/bin/sh

export $(cat /django/app/.env | xargs) && rails c
python3 manage.py migrate --no-input
python3 manage.py collectstatic --no-input
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('Shami', 'Shamil79797@gmail.com', 'KbPeShVkYp3s6v9y$B&E)H@McQfTjWnZ')" | python3 manage.py shell
