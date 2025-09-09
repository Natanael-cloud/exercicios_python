def calcular_total(numeros):
    return sum(numeros)


def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1
    return antecessor, sucessor


def func_3():
    print("Ola mundo")

# Chamando a função
print(calcular_total([10, 20, 30, 40]))  # Saída: 100
print(retorna_antecessor_e_sucessor(10))  # Saída: (9, 11)
func_3()  # Saída: Olá, mundo!