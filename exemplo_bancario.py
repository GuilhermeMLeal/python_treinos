agencia = '12ER1'
saldo=0
limite=500
extrato=""
LIMITE_SAQUES = 3
numero_saques = 0

menu = """Bem-vindo ao banco Martins. Aqui está sua agência {}. Digite a opção desejada:

[d] Depósito
[s] Saque
[e] Extrato
[q] Sair
""".format(agencia)

print(menu)

while True:
    opcao = input()

    if opcao == "d":
        print("Opção selecionada: Depósito")
       
    elif opcao == "s":
        print("Opção selecionada: Saque")
        
    elif opcao == "e":
        print("Opção selecionada: Extrato")
        
    elif opcao == "q":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")
        

        