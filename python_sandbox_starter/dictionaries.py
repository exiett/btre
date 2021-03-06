# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

#Dicionário simples

person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30
}

#Usando constructor
persona = dict(
    first_name='John', last_name='Doe',age=30
)
#print(persona)

#Acessar valor:
print(person['first_name'])
print(person.get('last_name'))

#Adicionar chave/valor
person['phone'] = '555-555-555'

#Pegar a chave
print(person.keys())

#Pegar o valor
print(person.items())

#Fazer uma cópia
person2 = person.copy()
person2['city'] = 'Boston'
print(person2)

#Remover item
del(person['age'])
person.pop('phone')
print(person)

#Limpar o dicionário inteiro
person.clear()
print(person)

#Pegar o tamanho do dicionário
print(len(persona))
print(len(person))