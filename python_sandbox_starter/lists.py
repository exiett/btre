# A List is a collection which is ordered and changeable. Allows duplicate members.

#Criando uma lista normal:
numbers = [1,2,3,4,5]

#Criando usando um constructor
numbers = list((1,2,3,4,5))
print(type(numbers))


fruits = ['Apples', 'Oranges', 'Grapes', 'Pears', 12]

#Pegando valor:
print(fruits[1])

#Pegando o tamanho (quantas coisas tem) da lista
print(len(fruits))

#Inserindo com Append
fruits.append('Mangos')
print(fruits)

#Removendo
fruits.remove('Grapes')
print(fruits)

#Inserindo em determinada posição:
fruits.insert(2, 'Strawberries')
print(fruits)

#Removendo em determinada posição:
fruits.pop(4)
print(fruits)

#Inverter lista
fruits.reverse()
print(fruits)

#Ordenar - não funciona se tiver outro tipo de dado na lista
fruits.sort()
print(fruits)

#Ordenar de trás pra frente
fruits.sort(reverse=True)
print(fruits)