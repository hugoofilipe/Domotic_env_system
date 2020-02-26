# Smart Home Control - Home automation system 
Tag tech: Python, postgres, 

Description:
 - 
 
Goals and objectives:
-
This application was born to live inside a specific enviroment, containarized by docker. The idea is to deploy this application in diferent enviroments (development and production enviroment). It will speak with a database postgres and REDIS, who will lives in same server, but outside of his enviroment.  

Requirements:
 - 

Road map:
-
 - Instalar o HA - Home assistance
 - Instalar git
 - instalar docker
 - Criar cron job
 - Instalar base de dados: Database postgres
 - Criar 2 ambientes e instalar as aplicaçes (Container DEV e container PROD-RaspPi)
 - Testar com dispositivos em produção (RaspPi)
 - Instalar o openhab
 - Comprar:
     -um display
     -sensor para aquecedores
 - instalar jenkins (para fazer build e deploy em ambiente de produção;
 - instalar ansible (para conter todas as configurações;
 - instalar nsq
 - criar workers
 - criar event brockers
 - lançar Api orientada ao estado do serviço 
 - integraçao com telegram

Docs:
-
 - **Style standart** code: pep8 (https://www.python.org/dev/peps/pep-0008/)
 - **Api server**: Build with **Flask** (https://pypi.org/project/Flask/)
 - **Packages contribution**: pypi (https://pypi.org/)
 - **To Creates and Manages a virtual ENVIRONMENT**: **venv** (https://docs.python.org/3/library/venv.html) or **pipenv** (https://github.com/pypa/pipenv)

Troubleshooting:
-
 - **Check service port**: sudo netstat -nlp | grep 8080 ->https://stackoverflow.com/questions/34457981/trying-to-run-flask-app-gives-address-already-in-use 

----------------
First time setup
-
**Start Enviroment**
- On windowns we need to start an enviromnent for run flask:
```
 . venv/Scripts/activate
```
ps: to exit just write *deactivate*
- Create and start environment on linux:
(need to had information about that

***Start webapi on linux***
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
$set FLASK_APP=venv/api.py
$flask run --host=0.0.0.0 --port=80
```
