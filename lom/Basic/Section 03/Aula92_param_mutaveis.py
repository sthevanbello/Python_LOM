from dados import lista_pessoas, lista


def lista_de_cientes(clientes_iteravel, lista=None):
    if lista is None:
        lista = []
    lista.extend(clientes_iteravel)
    return lista


clientes = lista_de_cientes(lista_pessoas)
clientes2 = lista_de_cientes(lista)

print('\n' + '=' * 150 + '\n')

print(clientes)
print(clientes2)
