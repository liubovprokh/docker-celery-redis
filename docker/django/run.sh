#!/usr/bin/env bash

python /app/src/manage.py check --deploy --fail-level "WARNING"
python /app/src/manage.py migrate --noinput
python /app/src/manage.py collectstatic --noinput
# python manage.py compilemessages -v 0

# Start gunicorn with 4 workers:

/usr/local/bin/gunicorn --chdir=/app/src server.wsgi -w 4 --timeout 1200 -b 0.0.0.0:8000
