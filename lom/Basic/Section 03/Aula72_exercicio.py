carrinho = []

carrinho.append(('Produto1', 30))
carrinho.append(('Produto2', 20))
carrinho.append(('Produto3', 50))
carrinho.append(('Produto4', 80))

valores = sum([float(y) for x, y in carrinho])
# soma = sum(valores)
# print(soma)

print(valores)
