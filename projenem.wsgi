# vim: syntax=python
import sys
# Na linha abaixo basta  informar o caminho completo para o arquivo bin/activate_this.py dentro da pasta do virtual env
activate_this = '/home/ftrajano/apps_wsgi/projenem.wsgi'
with open(activate_this) as file_:
        exec(file_.read(), dict(__file__=activate_this))
sys.path.append('/home/ftrajano/apps_wsgi/projenem')
from run import app as application