# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'Jill'
age = 37

#Concatenando
print('Hello, I am ' + name + ' and I am ' + str(age))

# String Formatting

#Argumentos por posição
print('{}, {}, {}'.format('a', 'b', 'c'))
print('{1}, {2}, {0}'.format('a', 'b', 'c'))

#Argumentos por nome
print('Meu nome é {name} e eu tenho {age} anos.'.format(name='Jill', age=29))


# F-Strings
print(f'Isso é uma f-string.')
print(f"Isso também é uma f-string")
print(f"Dá pra fazer argumento por posição também. Tipo a {name}. Ela tem {age} anos.")

# String Methods
s = 'hello there world.'

# Letra maíuscula
print(s.capitalize())

# Todas as letras maíusculas
print(s.upper())
# Todas as letras minúsculas
print(s.lower())

# Swapcase = Se a primeira for maíuscula, todas as outras são minúsculas. Vice-versa.
print(s.swapcase())

# Tamanho da string
print(len(s))

# Trocar algo na string
print(s.replace('world', 'everyone'))

# Contar quantas vezes tal caracter aparece
sub = "h"
print(s.count(sub))