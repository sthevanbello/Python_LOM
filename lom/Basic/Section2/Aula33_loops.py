x = 0
while x < 10:
    print(x)
    x += 1
    if x == 2:
        continue
else:
    print('Bloco else')
print('Fim')

x = 0
while x < 10:
    print(x)
    x += 1
    if x == 2:
        break
else:
    print('Bloco else')
print('Fim')

texto = 'O rato roeu a roupa do rei de roma'
tamanho_texto = len(texto)
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
lista_nova = list(range(10))
contador = 0
while contador < tamanho_texto:
    print(f'{contador} - {texto[contador]}')
    contador += 1

for letra in range(len(texto)):
    print(letra)

for letra in texto:
    print(letra)

for letra in range(len(texto)):
    print(f'{letra} - {texto[letra]}')

# del(lista[3:8])
# print(lista)

print(f'Range - {lista_nova}')

# lista.insert(5, 'banana')

print(*lista)

print(max(lista))
print(min(lista))
