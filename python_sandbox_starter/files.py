# Python has functions for creating, reading, updating, and deleting files.

# Abrir um file (cria se não existir)
# Flag W é de write pra escrever nele.


myFile = open('myfile.txt', 'w')

# Pegar informação
print('Name: ', myFile.name)        # Nome do arquivo
print('Is Closed: ', myFile.closed) # Arquivo está fechado?
print('Mode: ', myFile.mode)        # Qual o modo do arquivo? Dá para escrever nele?

# Escrever no arquivo:
myFile.write('I love Python')
myFile.write(' and Javascript')
myFile.close()

# Appending no arquivo:
# Flag A é de append.
# Append vs Write: Write vai sobrescrever um arquivo que já tem conteúdo dentro. Append vai adicionar.
myFile = open('myfile.txt', 'a')
myFile.write(' and I also like PHP.')
myFile.close()

# Ler de um arquivo:
myFile = open('myfile.txt', 'r+')
text = myFile.read(13)              # Vai ler os 13 primeiros caracteres do arquivo.
print(text)