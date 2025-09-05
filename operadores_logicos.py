saldo = 1000
saque = 200
limite = 150

saldo >= saque and saque <= limite  # True
saldo >= saque and saque > limite   # False
saldo >= saque or saque > limite    # True
saldo < saque or saque > limite     # False
not saldo >= saque  # False
not saque > limite  # True


(saldo >= saque and saque <= limite) or (not saque > limite)  # True
# Verifica se o saldo é maior ou igual ao saque e se o saque é menor ou igual ao limite
# Ou verifica se o saque não é maior que o limite

