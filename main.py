# sistema de gerenciamento de barbearia
from control.classConexao import *
from control.criarTabelas import *
from model.classCliente import *
from model.classProduto import *
from view.menu import *
import json
#_______________________ instanciar classes _____________________

barbeariaDB = Conexao("barbearia","localhost","5432","postgres","postgres")
cliente = Clientes()
produto = Produtos()

#_______________________ instanciar classes _____________________
def CriarTabelas():
    with open("control\statusTabelas.json", 'r') as arquivoJson:
        chave = json.load(arquivoJson)
    
    if chave[0]["status"] == "criada":
        print("chave lida")
        pass
    else:
        resultadoCliente = barbeariaDB.manipularBanco(criarTabelaClientes())
        resultadoProduto = barbeariaDB.manipularBanco(criarTabelaProdutos())
        resultadoAgendamento = barbeariaDB.manipularBanco(criarTabelaAgendamentos())
        resultadoVendas = barbeariaDB.manipularBanco(criarTabelaVendas())
        resultadoItens = barbeariaDB.manipularBanco(criarTabelaItens())

        resultados = bool(resultadoCliente) and bool(resultadoProduto) and bool(resultadoAgendamento) and bool(resultadoVendas) and bool(resultadoItens)

        if resultados:
            print("tabelas criada")
            statusTabela = { "status" : "criada" }
            with open("control\statusTabelas.json", 'w') as arquivoJson:
                json.dump(statusTabela , arquivoJson, indent=2)

        else:
            print("erro ao tentar criar a tabelas")

CriarTabelas()

op = True
while op != "0":
    op = visualizarMenu()

    match op:
        case "1": 
            sqlCliente= cliente.inserirNovoCliente()
            resultado = barbeariaDB.manipularBanco(sqlCliente)
            mensagemDeConfirmacao(resultado)
        case "2":
            pass
        case "3":
            sqlProduto = produto.inserirNovoProduto()
            resultado = barbeariaDB.manipularBanco(sqlProduto)
            mensagemDeConfirmacao(resultado)
        case "4":
            pass
        case "5":
            sqlCliente = cliente.verCliente()
            resultado = barbeariaDB.consultarBanco(sqlCliente)
            listaIdClientes = mensagemListaClientes(resultado)      
            opcaoID = mensagemAtualizarCliente(listaIdClientes)
            if opcaoID:
                sqlUpdate = cliente.atualizarCliente(opcaoID)
                if sqlUpdate:
                    resultado = barbeariaDB.manipularBanco(sqlUpdate)
                    mensagemDeConfirmacao(resultado)
        case "6":
            pass
        case "7":
            sqlProduto = produto.verProduto()
            resultado = barbeariaDB.consultarBanco(sqlProduto)
            listaIdProdutos = mensagemListaProdutos(resultado)     
            opcaoID = mensagemAtualizarProduto(listaIdProdutos)
            if opcaoID:
                sqlUpdate = produto.atualizarProduto(opcaoID)
                if sqlUpdate:
                    resultado = barbeariaDB.manipularBanco(sqlUpdate)
                    mensagemDeConfirmacao(resultado)
        case "8":
            pass

print("Obrigado por usar o sysBarber!")        

        






