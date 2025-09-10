def somar(a, b):
    return a + b


def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação {a} + {b} é: {resultado}")


# Chamando a função
exibir_resultado(5, 3, somar)
# Saída: O resultado da operação 5 + 3 é: 8