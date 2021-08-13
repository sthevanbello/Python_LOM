# Operador ternário

logged_user = True

if logged_user:
    mensagem = "usuário logado"
else:
    mensagem = "Precisa logar"

print(mensagem)

mensagem = "Usuário logado" if logged_user else "Precisa logar"
print(mensagem)

idade = 18
e_maior_idade = (idade >= 18)

mensagem_idade = "Pode acessar" if e_maior_idade else "Não pode acessar"

print(mensagem_idade)
