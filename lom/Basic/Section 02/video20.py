nome = input('Digite o seu nome: ')
idade = int(input('Digite a sua idade: '))
peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))
ano_atual = 2021
ano_nascimento = ano_atual - idade
imc = peso / (altura ** 2)
print(f'Nome: {nome}')
print(f'Ano atual: {ano_atual}')
print(f'Idade: {idade}')
print(f'Ano de nascimento: {ano_nascimento}')
print(f'Peso: {peso}')
print(f'Altura: {altura:.2f}')
print(f'IMC: {imc:.2f}')
