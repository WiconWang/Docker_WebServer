#!/bin/bash
nohup cron &
python manage.py migrate
python /app/manage.py runserver 0:9060
