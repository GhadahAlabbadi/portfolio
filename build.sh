#!/usr/bin/env bash
# Render build command: installs packages and collects static files.
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
