#!/bin/sh

# entrypoint.sh

set -e

echo "Esperando a que MySQL inicie..."
while ! mysqladmin ping -h"$MYSQL_HOST" -u"$MYSQL_USER" -p"$MYSQL_PASSWORD" --silent; do
  sleep 2
done

echo "Applying migrations..."
python manage.py migrate --noinput

echo "Recollecting static files..."
python manage.py collectstatic --noinput

echo "Starting Daphne..."
exec daphne -b 0.0.0.0 -p 8000 todo_list.asgi:application


