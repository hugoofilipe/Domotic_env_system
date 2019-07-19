# Domotic_env_system
Home Automation System - Smart home control

Languages: Python

Style standart code: pep8 (https://www.python.org/dev/peps/pep-0008/)

Api server: Build with Flask (https://pypi.org/project/Flask/)

packages contribution: pypi (https://pypi.org/)

To creates and manages a virtual enviroment: **venv** (https://docs.python.org/3/library/venv.html) or **pipenv** (https://github.com/pypa/pipenv)

---------
Check service port: sudo netstat -nlp | grep 8080
https://stackoverflow.com/questions/34457981/trying-to-run-flask-app-gives-address-already-in-use 

frontdend style: Bootstrap 3

First time setup
----------------
**start Enviroment**
- On windowns we need to start an enviromnent for run flask:
```
 . venv/Scripts/activate
```
ps: to exit just write *deactivate*
- Create and start environment on linux:
(need to had information about that

***Start web api on linux***
```
. env FLASK_APP=teste.py flask run --host=0.0.0.0 --port=80
```
or:
```
$export FLASK_APP=teste.py 
$flask run --host=0.0.0.0 --port=80
```
on Windows (pycharm):
```
$set FLASK_APP=teste.py
$flask run --host=0.0.0.0 --port=80
```
