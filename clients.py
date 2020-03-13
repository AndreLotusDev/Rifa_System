def printLine():
    print("=======================================")

def clientFunc():
    printLine()
    print("\t bem vindo a aba clientes")
    printLine()
    print("1 - Cadastrar novo cliente")
    print("2 - Deletar cliente ")
    print("3 - Verificar todos os clientes")
    printLine()

    option = int(input("\t Digite a opcao desejada: "))

    if(option == 1):
        print("\tVoce vai cadastrar cliente novo")
        printLine()