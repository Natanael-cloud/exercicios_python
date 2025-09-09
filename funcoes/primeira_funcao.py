def exibir_mensagem():
    print("Olá, esta é a minha primeira função em Python!")


def exibir_mensagem_2(nome):
    print(f"Seja bem-vindo(a), {nome}!")


def exibir_mensagem_3(nome = "Anonimo"):
    print(f"Seja bem-vindo(a), {nome}!")

# Chamando a função
exibir_mensagem()
exibir_mensagem_2("Maria")
exibir_mensagem_3()

"""saida das funcoes:
Olá, esta é a minha primeira função em Python!
Seja bem-vindo(a), Maria!
Seja bem-vindo(a), Anonimo!"""
