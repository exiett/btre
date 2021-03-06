# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

#Criando classe!
class User:
    #Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
    
    def greeting(self):
        return f'My name is {self.name} and I am {self.age}.'

    def is_birthday(self):
        self.age += 1

class Customer(User):
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance

    def 


#Inicializando o objeto User
brad = User('Brad Traversy', 'brad@mail.com', 37)
jill = User('Jill Valentine', 'jill@mail.com', 46)
print(brad.name)

# Editando as propriedades de um objeto dentro da classe
brad.age += 1
print(brad.age)
brad.age = 39
print(brad.age)

# Editando propriedade de um objeto com um método dentro do próprio objeto:
brad.is_birthday()
print(brad.age)

# Chamando um método:
print(jill.greeting())

# Iniciando um customer:
john = Customer('John Doe', 'joe@mail.com', 40)
print(john.name)
print(john.balance)
john.set_balance(500)
print(john.balance)