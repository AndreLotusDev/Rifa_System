import re  ##para dividir as linhas do arquivo
import excel_function  ##funcoes do banco de dados feito em excel
import string
from openpyxl import Workbook
import openpyxl as op
import clients

##Lista de Variaveis
list_of_clients = []
client_info = []  ##informações de cada linha do for sobre os clientes
cpf_temp = ''
name_temp = ''
number_selected = ''


##Fim da lista de variaveis

# lista de funcoes

def printLine():
    print("=======================================")


def print_point_line():
    print("-------------------------")


def cpfcall():  ##Verifica se o cpf é um numero

    global cpf_temp
    cpf_temp = input("\tDigite o cpf do cliente: ")
    try:
        int(cpf_temp)
    except:
        print("Digite um numero valido!!")
        print_point_line()
        cpf_temp = ''
        cpfcall()

    def run_all_coluns():

        workbook = op.load_workbook('clientes_db.xlsx')
        woorksheet = workbook.get_sheet_by_name('DataBase_Clients')  # aqui é o nome da pasta dentro do excel

        ##Implementação de verificar se o excel possui um CPF igual
        for cell in woorksheet['B']:
            if (cpf_temp == cell.value):

                printLine()
                print("Este numero ja foi cadastrado!")
                printLine()
                print("Vc deseja atrelar mais uma rifa ao cliente? S/N")
                printLine()
                chose_inscribe_or_not = input("S/N? ->")
                printLine()

                if (chose_inscribe_or_not == 'N' or chose_inscribe_or_not == 'n'):
                    cpfcall()

    run_all_coluns()
    cpf_temp.translate({ord(c): None for c in string.whitespace})  # deleta os espaços em branco


def namecall():
    global name_temp
    name_temp = input("\tDigite o nome do cliente: ")

    try:
        for s in name_temp:
            if s != str:
                return True

    except:
        print("Nao é um nome correto")
        print_point_line()
        name_temp = ''
        namecall()


def numbercall():
    global number_selected
    number_selected = input("\tDigite o numero selecionado: ")

    try:
        int(number_selected)
    except:
        print("Nao é um numero válido !")
        print_point_line()
        number_selected = ''
        numbercall()

    number_selected.translate({ord(c): None for c in string.whitespace})  # deleta os espaços em branco
    print_point_line()


def add_client_info(Nome, CPF, NumberSelected):  ## Insere as informações no Excel
    workbook = op.load_workbook('clientes_db.xlsx')
    woorksheet = workbook.get_sheet_by_name('DataBase_Clients')  # aqui é o nome da pasta dentro do excel
    woorksheet.append([Nome, CPF, NumberSelected])
    workbook.save('clientes_db.xlsx')
    workbook.close()


##Fim da lista de funcoes

printLine()
print("\tBem vindo ao cadastro de cliente")
printLine()


def all_client_info_function():
    cpfcall()  # Chama a funcao do cadastro de CPF
    namecall()  # Chama a funcao do cadastro de nome
    numbercall()  # chama a funcao do cadastro do numero de sorteio

    add_client_info(name_temp, cpf_temp, number_selected)  ##chama o arquivo excel juntamente com a funcao


all_client_info_function()


def recursive_add_new_cliente():
    choices = input("\tDeseja cadastrar novamente? S/N ->")
    print_point_line()

    if (choices == 'S' or choices == 's'):
        all_client_info_function()
        recursive_add_new_cliente()
    if (choices == 'N' or choices == 'n'):
        clients.clientFunc()


recursive_add_new_cliente()
