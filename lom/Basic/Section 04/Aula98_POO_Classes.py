from pessoa import Pessoa

# pessoa1 = Pessoa('Sthevan', 35)
pessoa1 = Pessoa.por_ano_nascimento('Sthevan', 1986)

print(f'Nome: {pessoa1.nome}')
print(f'Idade: {pessoa1.idade} anos')
print(f'Ano de nascimento: {pessoa1.get_ano_nascimento(2021)}')
