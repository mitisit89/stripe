#!/bin/sh


python core/manage.py migrate&&
python core/manage.py makemigrations api &&
python core/manage.py init_admin_user 
