#!/bin/sh
pip install -r requirements.txt

flask db migrate
flask db upgrade

python run.py