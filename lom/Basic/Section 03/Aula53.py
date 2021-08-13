# Funções
# def


def saudacao(tipo, nome):
    print(f'{tipo}, {nome}')


def soma(a, b, c):
    return a + b + c


def porcentagem(numero, percentual):
    return numero + (numero * percentual / 100)


def fizz_buzz(numero):
    valor = ''
    if numero % 3 == 0:
        valor += 'Fizz'
    if numero % 5 == 0:
        valor += 'Buzz'
    if numero % 3 != 0 and numero % 5 != 0:
        return numero
    return valor


saudacao('Olá', 'Sthevan')
saudacao('Oi', 'Natália')
saudacao('Tudo bem', 'Léo?')
print(soma(1, 2, 3))
print(porcentagem(50, 10))
print(porcentagem(150, 10))
print(fizz_buzz(15))
