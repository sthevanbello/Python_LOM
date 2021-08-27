try:
    a = 10/0
    print(a)
except NameError as error:
    print('Erro: ', error)
except ZeroDivisionError as error:
    print(f'Erro: {error}')
else:
    print('Código executado')
finally:
    print('Finally Sempre é executado')
