
def visualizarMenu():
    print('''
        💈💇‍♂️🪒 sys Barber ✂️💇‍♀️💈

Sistema de gerenciamento de barbearia na palma da mão:
Escolha uma das opções[] abaixo e tecle [Enter↵]

[1] 📝👪 Cadastrar clientes
[2] 📝🗓️ Agendamento de serviço
[3] 📝📦 Cadastrar produto
[4] 📝💰 Efetuar venda
[5] 👀👪 Visualizar lista de clientes
[6] 👀🗓️️ Visualizar lista de agendamentos
[7] 👀📦 Visualizar lista de produtos
[8] 👀💰 Visualiazar lista de  venda
[0] 🚪 Sair
    ''')

    op = input(": ")
    if op in "123456780":
        pass
    else:
        print("comando inválido, tente novamente")
        input("aperte qualquer tecla para continuar")
    
    return op

def mensagemDeconfirmacao(resultado):
    if resultado:
        print("Registro efetuado!")
    else:
        print("O registro falhou")

def visualizarListaClientes(resultado):
    print("id | nome | telefone | email")
    for cliente in resultado:
        print(f"{cliente[0]} | {cliente[1]} | {cliente[2]} | {cliente[3]}")