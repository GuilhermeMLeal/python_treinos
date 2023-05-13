sacar=-1
while sacar!=0:
    opcao=int(input("Selecione a opção a seguir \n [1] Sacar 50$$ \n [2] Sacar 100$$")) 
    if  opcao ==1:
         sacar+=50
         print(sacar)
    elif opcao==2:
        sacar+=101
        break
        
print(sacar)

exemplo = ['aEioU', 'UMDoIS']

for letra in exemplo:
    if letra.upper() in exemplo :
        print(letra, end=" \n")
        print()
    else:
        print("Não é maiuscula")
        print()


for numeros in range(0,101,1):
    print(numeros,end=" ")


