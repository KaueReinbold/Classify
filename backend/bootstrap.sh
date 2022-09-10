#!/bin/sh
export FLASK_APP=./courses/index.py
VIRTUAL_ENV=$(pipenv --venv | sed 's.\\./.g')
echo "\$VIRTUAL_ENV:" $VIRTUAL_ENV
source $VIRTUAL_ENV/Scripts/activate
flask run -h 0.0.0.0