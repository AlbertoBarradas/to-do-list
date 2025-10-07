#!/bin/sh

echo "Applying migrations..."
python manage.py migrate --noinput

echo "Recollecting static files..."
python manage.py collectstatic --noinput

echo "Starting Daphne..."
exec daphne -b 0.0.0.0 -p 8000 todo_list.asgi:application