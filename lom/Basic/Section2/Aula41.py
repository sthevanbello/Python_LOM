# Enumerate

lista = [
    ['Edu', 'João', 'Luiz'],
    ['Maria', 'Aline', 'Joana'],
    ['Helena', 'Eduardo', 'Lu']
]

for valor in enumerate(lista, 53):
    valor_enumerado, minha_lista = valor
    nome1, nome2, nome3 = minha_lista
    print(nome2)
