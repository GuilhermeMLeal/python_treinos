saldo = 500.00
print(float(saldo))
#Estruturas condicionais
saque = float(input("Digite o valor do saque"))
if saque<=saldo:
    saldo-=saque
    print("Saque realizado e seu saldo é de ",saldo)
elif saque> saldo:
     print("Você não tem dinheiro suficiente") 
else:
    print("Saque não efetuado")

extrato = 1000.00
consulta ="Domingo"
opcoes = int(input("Ver o extrato [1]\n Consulta medica[2]"))

if opcoes==1:
    print("Seu extrato é: ",extrato)
elif opcoes==2:
    print("Consulta realizada: ",consulta)
    status= input("Qual é o dia da semana")
    
    if status in["domingo","sabado","segunda"]:
        print("Consulta efetuada")
    else: print("consulta não efetuada")
else:
    print("Selecione uma informação pertinente")

