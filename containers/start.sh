#!/bin/bash

service postgresql start
sudo -u postgres bash -c "psql -c \"CREATE USER django WITH PASSWORD 'django';\""
sudo -u postgres bash -c "createdb development"
cd application
python manage.py migrate
python manage.py loaddata development
python manage.py runserver
bash