# !usr/bin/env bash
# exit on error
set -o errexit
pip install -r requirements.txt
cd myproject

python manage.py makemigrations
python manage.py migrate
# python manage.py collectstatic --noinput
