opcao = -1
while opcao != 0:
    opcao = int(input("[1] Sacar\n[2] Depositar\n[0] Sair\n"))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Depositando...")
    elif opcao == 0:
        print("Saindo...")
else:
    print("Obrigado por usar nosso sistema bancário, até breve!")

#run: [1] Sacar
#run: Sacando...
#run: [2] Depositar
#run: Depositando...
#run: [0] Sair
#run: Saindo...