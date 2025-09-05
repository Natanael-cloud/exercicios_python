saldo = 1000  # Definido globalmente para ser acessado pelas funções

def sacar(valor):
    global saldo  # Usando a variável global
    if saldo >= valor:
        saldo -= valor  # Deduz o valor do saldo
        print(f"Valor de R${valor} sacado com sucesso. Saldo atual: R${saldo}")
    else:
        print("Saldo insuficiente para o saque.")

def depositar(valor):
    global saldo  # Usando a variável global
    saldo += valor  # Adiciona o valor ao saldo
    print(f"Valor de R${valor} depositado com sucesso. Saldo atual: R${saldo}")

# Testando as funções
sacar(200)
depositar(500)
sacar(1500)
# Exemplo de identação correta em blocos condicionais e de repetição
