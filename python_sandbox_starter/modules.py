# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

#Módulos core:
import datetime               # Aqui eu importo todo o módulo. Pra acessar, eu uso datetime.módulo.método()
today = datetime.date.today() # Uso importando todo o módulo
#print(today)

from datetime import date     # Aqui eu só importo um módulo. Pra acessar, eu uso date.método()
today2 = date.today()         # Uso importando só o método que eu quero
#print(today2)

import time
timestamp = time.time()
#print(timestamp)

from time import time
timestamp2 = time()
#print(timestamp2)

# Pip Module:
import camelcase

camelo = camelcase.CamelCase()
text   = 'hello there world'
print(camelo.hump(text))

# Importando de outro arquivo:
# Presta atenção que ali tem um arquivo chamado validator, dentro dele tem o método de validar e-mail usando regex.
# Posso importar ele inteiro:
import validator

email = 'teste@teste.com'

if validator.validate_email(email):
    print('Email is valid.')
else:
    print('Not an valid email.')

# Ou posso importar só o método específico que eu quero usar.
from validator import validate_email
if validate_email(email):
    print('Email is valid.')
else:
    print('Not an valid email.')
