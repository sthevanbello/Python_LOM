import os
from dados import pessoas
import json

path = 'D://Developer//Python//udemy//lom//Basic//Section 03//'

# file = open(f'{path}abc.txt', 'w+')
# file.write('Linha 1\n')
# file.write('Linha 2\n')
# file.write('Linha 3\n')

# # função seek volta para o começo do arquivo com 0, 0
# file.seek(0, 0)

# print('Read Lines: ')
# print(file.read())

# print('=' * 100)
# file.seek(0, 0)

# print(file.readline(), end='')
# print(file.readline(), end='')
# print(file.readline(), end='')

# print('=' * 100)
# file.seek(0, 0)

# print(file.readlines())

# file.seek(0, 0)
# print('=' * 100)
# for linha in file:
#     print(linha, end='')

# try:
#     file = open(f'{path}abc.txt', 'w+')
#     file.write('Linha 1\n')
#     file.write('Linha 2\n')
#     file.write('Linha 3\n')
#     file.seek(0, 0)
#     print(file.read())
# finally:
# file.close()
# file = open(f'{path}abc.txt', 'w+')
# file.close()

# apaga tudo com w+
# with open(f'{path}abc.txt', 'w+') as file:
#     file.write('Linha 1\n')
#     file.write('Linha 2\n')
#     file.write('Linha 3\n')
#     file.write('Linha 4\n')
#     file.seek(0, 0)
#     print(file.read())

# Leitura do arquivo com r
# with open(f'{path}abc.txt', 'r') as file:
#     print(file.read())

# Faz um append nas próximas linhas
# with open(f'{path}abc.txt', 'a+') as file:
#     file.write('Linha nova\n')
#     file.seek(0, 0)
#     print(file.read())

# os.remove(f'{path}abc.txt')

# pessoas_json = json.dumps(pessoas, indent=True)

# with open(f'{path}abc.json', 'w+') as file:
#     file.write(pessoas_json)
#     file.seek(0, 0)
#     print(file.read())
# print(pessoas_json)
# print(pessoas)
with open(f'{path}abc.json', 'r') as file:
    pessoas_json = file.read()
    file.seek(0, 0)
print(pessoas_json)
