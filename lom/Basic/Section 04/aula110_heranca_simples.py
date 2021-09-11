from classes.heranca import Pessoa, Cliente, ClienteVip

print('Pessoa genérica')
pessoa1 = Pessoa('Homer', 45)
print(pessoa1.nome)

print('Pessoa física')
cliente = Cliente('Marge', 45, '12345678912')
print(cliente.nome, cliente.idade, cliente.cpf)
cliente.comprar()
print()
cliente_vip = ClienteVip('Bart', 12, '12345678965', 1234)
print(cliente_vip.nome)
cliente_vip.comprar()
