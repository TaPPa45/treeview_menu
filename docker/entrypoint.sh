#!/bin/bash

echo "Применение миграций..."
python manage.py migrate --noinput

echo "Сбор статики..."
python manage.py collectstatic --noinput

echo "Запуск сервера..."
exec python manage.py runserver 0.0.0.0:8000