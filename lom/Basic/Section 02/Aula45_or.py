# Operador condicional OR

nome = input('Digite um nome: ')

if nome:
    print(nome)
else:
    print('Não digitou nome - Print dentro do if/else')

print(nome or 'Não digitou nome - Print com or')

# Seleciona o primeiro valor que for verdadeiro
a = 0
b = None
c = False
d = []
e = {}
# Valor verdadeiro
f = 22
g = "Sthevan"
variavel = a or b or c or d or e or f or g

print(variavel)
