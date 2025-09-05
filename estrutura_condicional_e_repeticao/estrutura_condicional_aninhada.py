saldo = 2000
saque = 500
cheque_especial = 450

conta_normal = True  # Definindo como conta normal (para exemplo)
conta_universitaria = False  # Definindo como conta universitária (para exemplo)

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial")
    else:
        print("Saldo insuficiente para saque")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso")
    else:
        print("Saldo insuficiente para saque em conta universitária")

