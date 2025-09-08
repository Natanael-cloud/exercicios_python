texto = input("Digite um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:  # Verificando se a letra é uma vogal
        print(letra, end=" ")

else:
    print()
    print("Executa no final do laço")


# run: Digite um texto: Python é demais!
# run: o a e a is


#exemplo com range
for numero in range(0,51, 5): #inicio, fim, passo
    print(numero, end=" ")
#run:
# 0 5 10 15 20 25 30 35 40 45 50
