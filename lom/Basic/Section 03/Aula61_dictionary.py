import copy

d1 = {'chave': 'valor'}

print(d1, type(d1))

d2 = dict(chave1='valor da chave 1 do d2', chave2='Valor da chave 2 do d2')

print(d2)

print(d2.get('chave2'))
print(d2.get('chave3'))

d1.update({'nova_chave': 'Valor da nova chave'})
print(d1)

del d1['chave']
print(d1)

if 'chave2' in d2:
    print('Contém chave 2 em d2')

if 'Valor da chave 2' in d2.values():
    print('Existe o valor')

for key in d2:
    print(key)

for value in d2.values():
    print(value)

for k in d2.items():
    print(*k)

for k, v in d2.items():
    print(k, v)

# Copia rasa. Não copia totalmente. Só a referência
d1_copy = d1.copy()
d1_copy['nova_chave'] = 'Novo valor copy'
print(d1_copy)
print(d1)

# Cópia profunda / Cópia de verdade
d1_deep = copy.deepcopy(d1)
print(d1_deep)

d1.update(d2)
print(d1)
