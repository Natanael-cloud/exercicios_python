salario = 3000


def salario_bonus(bonus):
    global salario

    lista_aux = lista.copy()
    lista_aux.append(2)
    print(f"lista_aux: {lista_aux}")

    salario += bonus
    return salario


salario_com_bonus = salario_bonus(500)
print(salario_com_bonus)  # Saída: 3500


lista = [1]
salario_com_bonus = salario_bonus(500, lista)
print(salario_com_bonus)  # Saída: 4000
print(lista)  # Saída: [1]

