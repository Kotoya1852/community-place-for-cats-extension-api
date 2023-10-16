#! /bin/sh
pipenv run gunicorn --bind=0.0.0.0:8000 --access-logfile - config.wsgi:application