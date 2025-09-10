def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)


# Chamando a função
exibir_poema(
    "27 de abril de 2024",
    "No meio do caminho tinha uma pedra",
    "Era uma pedra muito grande",
    autor="Carlos Drummond de Andrade",
    ano=1945
)  

# Saída:
# 27 de abril de 2024
# No meio do caminho tinha uma pedra
# Era uma pedra muito grande
# autor: Carlos Drummond de Andrade
# ano: 1945

