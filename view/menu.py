
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
    if op in "1|2|3|4|5|6|7|8|0":
        pass
    else:
        print("comando inválido, tente novamente")
        input("aperte [Enter↵] para continuar")
    
    return op

def mensagemDeConfirmacao(resultado):
    if resultado:
        print("Registro efetuado!")
        input("aperte [Enter↵] para continuar")
    else:
        print("O registro falhou")
        input("aperte [Enter↵] para continuar")


# ______________________ trechos de código relacionados a clientes _______________
def mensagemListaClientes(resultado):
    listaIdClientes = []
    print("id | nome | telefone | email")
    for cliente in resultado:
        print(f"{cliente[0]} | {cliente[1]} | {cliente[2]} | {cliente[3]}")
        listaIdClientes.append(cliente[0])
    
    return listaIdClientes

def mensagemEscolherDeletarOuAtualizarCliente():
    
    op = "rodarWhile"
    while not(op in "1|2|0"): 
        
        print("""
Deseja fazer alguma alteração na lista cliente?
Digite [1]Atualizar, [2]Deletar ou [0]sair.
    
    [1] Atualizar Cliente
    [2] Deletar Cliente
    [0] sair
    """)
        op = input(": ")
        match op:
            case "1":
                opEscolhida = "Atualizar"
            case "2":
                opEscolhida = "Deletar"
            case "0":
                opEscolhida = False
            case _:
                    print("comando inválido, tente novamente")
                    input("aperte [Enter↵] para continuar")
        
    return opEscolhida

def mensagemAtualizarCliente(listaIdClientes):
    
    op = "rodarWhile"
    while not(op in "1|0"):
        print("""
confirme atualização do cliente? Digite [1]Sim ou [0]Não.

[1] Sim
[0] Não
""")
        op = input(": ")
        match op:
            case "1":
                opcao = 0
                while not(opcao in listaIdClientes):
                    print("Digite o ID do Cliente a ser atualizado:")          
                    try:
                        opcao = int(input(": "))                
                        if opcao in listaIdClientes:
                            pass
                        else:
                            print("ID do Cliente não existe")
                            print("Voltando ao menu principal")
                            input("aperte [Enter↵] para continuar")
                            opcao = False
                            break
                    except:
                        print("comando invalido. Tente novamente")
            case "0":
                opcao = False
            case _:
                print("comando inválido, tente novamente")
                input("aperte [Enter↵] para continuar")
                op = "rodarWhile"
        
    return opcao

def mensagemDeletarCliente(listaIdClientes):
    
    op = "rodarWhile"
    while not(op in "1|0"):
        print("""
confirma deletar algum cliente? Digite [1]Sim ou [0]Não.

[1] Sim
[0] Não
""")
        op = input(": ")
        match op:
            case "1":
                opcao = 0
                while not(opcao in listaIdClientes):
                    print("Digite o ID do Cliente a ser deletado:")          
                    try:
                        opcao = int(input(": "))                
                        if opcao in listaIdClientes:
                            pass
                        else:
                            print("ID do Cliente não existe")
                            print("Voltando ao menu principal")
                            input("aperte [Enter↵] para continuar")
                            opcao = False
                            break
                    except:
                        print("comando invalido. Tente novamente")
            case "0":
                opcao = False
            case _:
                print("comando inválido, tente novamente")
                input("aperte [Enter↵] para continuar")
                op = "rodarWhile"
        
    return opcao

#______________________ trechos de código relacionados a Produto ___________________
def mensagemListaProdutos(resultado):
    listaIdProdutos = []
    print("id | nome | preço | quantidade")
    for produto in resultado:
        print(f"{produto[0]} | {produto[1]} | {produto[2]} | {produto[3]}")
        listaIdProdutos.append(produto[0])
    
    return listaIdProdutos

def mensagemEscolherDeletarOuAtualizarProduto():
    
    op = "rodarWhile"
    while not(op in "1|2|0"): 
        
        print("""
Deseja fazer alguma alteração na lista de Produtos e serviços?
Digite [1]Atualizar, [2]Deletar ou [0]sair.
    
    [1] Atualizar produtos/serviços
    [2] Deletar produtos/serviços
    [0] sair
    """)
        op = input(": ")
        match op:
            case "1":
                opEscolhida = "Atualizar"
            case "2":
                opEscolhida = "Deletar"
            case "0":
                opEscolhida = False
            case _:
                    print("comando inválido, tente novamente")
                    input("aperte [Enter↵] para continuar")
        
    return opEscolhida

def mensagemAtualizarProduto(listaIdProdutos):
    
    op = "rodarWhile"
    while not(op in "1|0"):
        print("""
Deseja atualizar algum Produto? Digite [1]Sim ou [0]Não.

[1] Sim
[0] Não
""")
        op = input(": ")
        match op:
            case "1":
                opcao = 0
                while not(opcao in listaIdProdutos):
                    print("Digite o ID do produto a ser atualizado:")          
                    try:
                        opcao = int(input(": "))                
                        if opcao in listaIdProdutos:
                            pass
                        else:
                            print("ID do produto não existe")
                            print("Voltando ao menu principal")
                            input("aperte [Enter↵] para continuar")
                            opcao = False
                            break
                    except:
                        print("comando invalido. Tente novamente")
            case "0":
                opcao = False
            case _:
                print("comando inválido, tente novamente")
                input("aperte [Enter↵] para continuar")
                op = "rodarWhile"
        
    return opcao

def mensagemDeletarProduto(listaIdClientes):
    
    op = "rodarWhile"
    while not(op in "1|0"):
        print("""
Deseja deletar algum Produto? Digite [1]Sim ou [0]Não.

[1] Sim
[0] Não
""")
        op = input(": ")
        match op:
            case "1":
                opcao = 0
                while not(opcao in listaIdClientes):
                    print("Digite o ID do Produto a ser apagado:")          
                    try:
                        opcao = int(input(": "))                
                        if opcao in listaIdClientes:
                            pass
                        else:
                            print("ID do Cliente não existe")
                            print("Voltando ao menu principal")
                            input("aperte [Enter↵] para continuar")
                            opcao = False
                            break
                    except:
                        print("comando invalido. Tente novamente")
            case "0":
                opcao = False
            case _:
                print("comando inválido, tente novamente")
                input("aperte [Enter↵] para continuar")
                op = "rodarWhile"
        
    return opcao

# __________________________ trecho de códigos da agenda ______________________

def mensagemListaAgenda(resultado):
    listaHorasAgenda = []
    print("id |IDCliente| IDServiço | horário ")
    for agendamento in resultado:
        print(f"{agendamento[0]} | {agendamento[1]} | {agendamento[2]} | {agendamento[3]}")
        listaHorasAgenda.append(agendamento[3])
    
    if listaHorasAgenda:
        pass
    else:
        print("Todos os horários estão diponíveis")

    return listaHorasAgenda


