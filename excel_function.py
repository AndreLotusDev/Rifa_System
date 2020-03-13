from openpyxl import Workbook
import openpyxl as op
import newClient

def createExcel(): ##cria a planilha banco de dados
    clients_db = Workbook()

    planilha1 = clients_db.active
    planilha1.title = "DataBase_Clients"

    valores = [
        ("Nome", "CPF", "Numero Selecionado"),

    ]
    for linha in valores:
        planilha1.append(linha)

    clients_db.save("clientes_db.xlsx")



