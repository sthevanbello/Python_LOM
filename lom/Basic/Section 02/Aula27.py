numero1 = input('Digite um número: ')
numero2 = input('Digite outro número: ')

if numero1.isnumeric() and numero2.isnumeric():
    numero1 = int(numero1)
    numero2 = int(numero2)
    soma = numero1 + numero2
    print(f'A soma do número {numero1} com o número {numero2} é {soma}')
else:
    print('Digite apenas números inteiros')
