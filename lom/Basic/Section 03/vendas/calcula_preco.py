from vendas.formata.preco import formata_real


def aumento(valor, porcentagem, formata=False):
    valor_atualizado = valor + (valor * porcentagem / 100)
    if formata:
        return formata_real(valor_atualizado)
    else:
        return valor_atualizado


def reducao(valor, porcentagem, formata=False):
    valor_atualizado = valor - (valor * porcentagem / 100)
    if formata:
        return formata_real(valor_atualizado)
    else:
        return valor_atualizado
