#!/bin/bash
echo "$HOST_HOSTNAME"
echo "Running docker-entrypoint.sh:"

echo "DEV environment.";
echo "Checking new requirements"
pip3 install -r requirements.txt
echo "Checking new local requirements"
pip3 install -r requirements-local.txt
echo "Applying database migrations"
python3 manage.py migrate
echo "Starting django dev server"
python3 manage.py runserver 0.0.0.0:8000

echo "Done entrypoint" && /bin/bash