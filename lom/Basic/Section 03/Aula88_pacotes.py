# import vendas.calcula_preco
# from vendas import calcula_preco
from vendas.calcula_preco import aumento, reducao

preco = 100
porcentagem = 50

# preco_com_aumento = vendas.calcula_preco.aumento(valor = preco, porcentagem = porcentagem)
# print(preco_com_aumento)

# preco_atualizado = calcula_preco.aumento(preco, porcentagem)
preco_atualizado = aumento(preco, porcentagem, False)
preco_atualizado2 = reducao(preco, porcentagem, True)

print(preco_atualizado)
print(preco_atualizado2)
