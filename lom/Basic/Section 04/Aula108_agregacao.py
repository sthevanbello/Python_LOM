from classes.carrinho import CarrinhoDeCompras, Produto

carrinho = CarrinhoDeCompras()

produto_1 = Produto('Televisão', 2500.49)
produto_2 = Produto('Playstation 5', 4619.99)
produto_3 = Produto('God of War', 349.49)

carrinho.inserir_produto(produto_1)
carrinho.inserir_produto(produto_2)
carrinho.inserir_produto(produto_3)

carrinho.lista_produtos()

print(f'Total: {carrinho.soma_total():.2f}')