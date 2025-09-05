MAIOR_IDADE = 18
IDADE_ESPECIAL = 12

idade = int(input("Digite sua idade: "))

if idade >= MAIOR_IDADE:
    print("Você é maior de idade. Pode tirar a CNH.")
elif idade >= IDADE_ESPECIAL:
    print("Pode fazer as aulas teóricas, mas não as aulas práticas.")
else:
    print("Ainda não pode tirar a CNH.")

# Exemplo de execução
# Digite sua idade: 20
# Você é maior de idade. Pode tirar a CNH.

# Digite sua idade: 15
# Pode fazer as aulas teóricas, mas não as aulas práticas.

# Digite sua idade: 10
# Ainda não pode tirar a CNH.
