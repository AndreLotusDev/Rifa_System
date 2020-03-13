import newClient
import verify_all_clients

def printLine():
    print("=======================================")

##variaveis
option = 0
def clientFunc():



    printLine()
    print("\t Bem vindo a aba clientes")
    printLine()
    print("1 - Cadastrar Novo cliente")
    print("2 - Deletar cliente ")
    print("3 - Verificar todos os clientes")
    printLine()

    option = int(input("\t Digite a opcao desejada: "))

    if(option == 1): ## Entra na aba de cadastro de clientes
        newClient()
        printLine()
    if (option == 2):  ## Entra na aba de verificar todos os clientes
        verify_all_clients()
        printLine()