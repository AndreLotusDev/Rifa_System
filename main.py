import clients

def printLine():
    print("=======================================")

print("Sistema de Rifas")
print("")

printLine()
print("1 - Área de cadastro de clientes")
print("2 - Área de cadastro de produtos")
print("3 - Realizar a Rifa !!!!")
printLine()

option = int(input("Digite a opcao selecionada: ")) ##Entra em uma das telas

printLine()
if(option == 1):
    print("vc entrou na area clientes")
    clients.clientFunc()