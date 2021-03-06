# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary
import json

# JSON exemplo. Esse arquivo geralmente viria de uma API após uma request (resposta)
userJSON = '{"first_name": "John", "last_name": "Doe", "age": 30}'

# Parse JSON -> dicionário
user = json.loads(userJSON)
print(user)               # Acessando todo o JSON
print(user['first_name']) # Acessando um valor dentro do JSON

# Fazer um dicionário virar JSON
car = {'make': 'Ford', 'model': 'Mustang', 'year': 1970}
carJSON = json.dumps(car)
print(carJSON)