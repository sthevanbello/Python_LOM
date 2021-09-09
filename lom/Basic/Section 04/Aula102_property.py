from produto import Produto

produto1 = Produto('Camiseta', 50)
produto2 = Produto('Caneca', 0)

# Acessando o atributo através do setter
produto2.preco = 100

print(f'\n{produto1.nome:_^50}')
print(produto1.preco)
print(produto1.desconto(10))
print(produto1.nome)

print(f'\n{produto2.nome:_^50}')

print(produto2.preco)
print(produto2.desconto(10))
print(produto2.nome)
