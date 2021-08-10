lista = ['Sthevan', 'Bruce', 'Tina', 'Léo', 'Bolão', 'Pretinha']

for nome in lista:
    print(nome)
    if nome.lower().startswith('h'):
        print('Fim com startswith e break')
        break
else:
    print('Fim com else do for')
