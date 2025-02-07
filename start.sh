#!/bin/bash

python mysite/manage.py createsuperuser --noinput
python mysite/manage.py runserver 0.0.0.0:$PORT