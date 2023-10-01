#!/usr/bin/env bash
# yari/deploy/build.sh
# exit on error
set -o errexit

export DJANGO_SETTINGS_MODULE=aapo.settings_production

echo "Installing python dependencies"
pip install -U pip
pip install -r requirements.txt

echo "Collecting staticfiles"
python manage.py collectstatic --noinput

echo "Running database migrations"
python manage.py migrate
