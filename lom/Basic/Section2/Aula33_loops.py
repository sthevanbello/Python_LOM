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
contador = 0
while contador < tamanho_texto:
    print(f'{contador} - {texto[contador]}')
    contador += 1
