#!/usr/bin/env bash
# yari/deploy/start.sh
# exit on error
set -o errexit

# Start the Gunicorn server
gunicorn --bind 0.0.0.0:$PORT --workers 1 --threads 8 --timeout 0 aapo.wsgi:application