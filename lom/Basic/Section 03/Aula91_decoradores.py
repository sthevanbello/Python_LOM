from time import time
from time import sleep


# def fala_oi():
#     print('Oi')

# variavel = fala_oi

# variavel()

# def master(funcao):
#     def slave(*args, **kwargs):
#         print('Decorada')
#         funcao(*args, **kwargs)

#     return slave

# @master
# def fala_oi():
#     print('oi, função fala_oi')

# # fala_oi = master(fala_oi)

# @master
# def outra_funcao(msg):
#     print(msg)

# # fala_oi()

# outra_funcao('Teste com outra função decorada')


def velocidade(funcao):
    def interna(*args, **kwargs):
        start_time = time()
        resultado = funcao(*args, **kwargs)
        end_time = time()
        tempo = (end_time - start_time)
        print(f'A função {funcao.__name__} levou {tempo}ms para executar')
        return resultado
    return interna


@velocidade
def demora():
    for i in range(1, 6):
        sleep(1)
        print(i)


demora()
