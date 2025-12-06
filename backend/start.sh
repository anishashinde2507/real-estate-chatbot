#!/bin/bash
set -e

echo "Running migrations..."
python manage.py migrate --noinput

echo "Collecting static files..."
python manage.py collectstatic --noinput --clear

echo "Starting Gunicorn..."
gunicorn realestate_api.wsgi:application \
    --bind 0.0.0.0:${PORT:-8000} \
    --workers 3 \
    --worker-class sync \
    --timeout 60 \
    --access-logfile - \
    --error-logfile -
