numero = int(input('Digite um número: '))
nome = 'Sthevan Bello Alves'
print(f'{numero:06.2f}')

print(f'{numero:0>10.2f}')  # Coloca zeros à esquerda
print(f'{numero:0>10}')     # Coloca zeros à esquerda
print(f'{numero:0<10.2f}')  # Coloca zeros à direita
print(f'{numero:0<10}')     # Coloca zeros à direita
print(f'{numero:0^10.2f}')  # Coloca o número no centro
print(f'{numero:0^10}')     # Coloca o número no centro
print(f'{nome:#>25}')       # Coloca caracteres à esquerda
print(f'{nome:#<25}')       # Coloca caracteres à direita
print(f'{nome:#^25}')
# Coloca caracteres nos dois lados e a string no centro
print(f'{nome[-6:-1]}')
print(f'{nome[1::2]}')
