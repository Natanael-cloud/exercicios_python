texto = input("Digite um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:  # Verificando se a letra é uma vogal
        print(letra, end=" ")

else:
    print()
    print("Executa no final do laço")

comente o run no codigo acima e veja o que acontece
# run: Digite um texto: Python é demais!
# run: o a e a is