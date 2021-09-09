from classes.carrinho import CarrinhoDeCompras, Produto

carrinho = CarrinhoDeCompras()

produto_1 = Produto('sabonete', 1.99)
produto_2 = Produto('Shampoo', 19.99)
produto_3 = Produto('Leite', 4.49)

carrinho.inserir_produto(produto_1)
carrinho.inserir_produto(produto_2)
carrinho.inserir_produto(produto_3)

carrinho.lista_produtos()