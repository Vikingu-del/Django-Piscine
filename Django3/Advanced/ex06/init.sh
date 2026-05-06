#!/usr/bin/env bash

if [ -d "~/.django_env" ]; then
    rm -rf ~/.django_env
fi
python3 -m venv ~/.django_env
source ~/.django_env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

sudo apt-get update
sudo apt-get install gettext

# sudo -u postgres psql
# ALTER USER djangouser CREATEDB;
# \q
