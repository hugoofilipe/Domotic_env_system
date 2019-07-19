# Domotic_env_system
Home Automation System - Smart home control

Languages: Python

Style standart code: pep8 (https://www.python.org/dev/peps/pep-0008/)

Api server: Build with Flask (https://pypi.org/project/Flask/)

packages contribution: pypi (https://pypi.org/)

To creates and manages a virtualenv: pipenv (https://github.com/pypa/pipenv)

---------
Check service port: sudo netstat -nlp | grep 8080
https://stackoverflow.com/questions/34457981/trying-to-run-flask-app-gives-address-already-in-use 

example for GPIOS: https://randomnerdtutorials.com/raspberry-pi-web-server-using-flask-to-control-gpios/


First time setup
----------------

Create and start environment on linux:

On windows:

Start web api on linux

. env FLASK_APP=teste.py flask run --host=0.0.0.0 --port=80

or:

$export FLASK_APP=teste.py 

$flask run --host=0.0.0.0 --port=80

on Windows (pycharm):

$set FLASK_APP=teste.py

$flask run --host=0.0.0.0 --port=80

