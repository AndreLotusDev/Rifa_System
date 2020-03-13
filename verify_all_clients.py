from openpyxl import Workbook
import openpyxl as op

list_of_names = []
list_of_cpf = []
list_of_number_selected = []
def printLine():
    print("=======================================")

printLine()
print("\t Bem vindo a verificação de clientes")
printLine()
print("\t 1 - Lista com todos os clientes: ")
printLine()

def run_all_coluns():

    i = 0
    workbook = op.load_workbook('clientes_db.xlsx')
    woorksheet = workbook.get_sheet_by_name('DataBase_Clients')  # aqui é o nome da pasta dentro do excel

    ##Roda todas as colunas e mostra na tela
    for cell in woorksheet['A']:
        list_of_names.append(cell.value)
    for cell in woorksheet['B']:
        list_of_cpf.append(str(cell.value))
    for cell in woorksheet['C']:
        list_of_number_selected.append(str(cell.value))

    while (i < (len(list_of_names) - 1)): ##Garante que todas as colunas sejam lidas
                print("Nome: " + list_of_names[i+1] + " \t\tCPF: " + list_of_cpf[i+1] + " \t\tNumero Selecionado: " + list_of_number_selected[i+1])
                print("------------------------------------------------")
                i += 1

run_all_coluns()