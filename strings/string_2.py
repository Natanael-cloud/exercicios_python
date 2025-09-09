nome = "Natanael"
idade = 30
profissao = "Desenvolvedor"
linguagem = "Python"

print("Me chamo{nome}, tenho {idade} anos, sou {profissao} e estou aprendendo {linguagem}.".format(
    nome=nome, idade=idade, profissao=profissao, linguagem=linguagem
))



# Usando f-strings (Python 3.6+)
mensagem = f"Olá, meu nome é {nome}, tenho {idade} anos, sou {profissao} e estou aprendendo {linguagem}."
print(mensagem)

# Usando o método format()
mensagem_format = "Olá, meu nome é {}, tenho {} anos, sou {} e estou aprendendo {}.".format(
    nome, idade, profissao, linguagem
)
print(mensagem_format)

