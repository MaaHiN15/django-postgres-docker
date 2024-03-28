#!/bin/ash
echo "Apply database migrations"
sleep 3
python manage.py migrate
exec $@