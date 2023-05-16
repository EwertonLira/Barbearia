# sistema de gerenciamento de barbearia
from control.classConexao import *
from control.criarTabelas import *
from model.classAgenda import *
from model.classCliente import *
from model.classItem import *
from model.classProduto import *
from model.classVenda import *
from view.menu import *
#_______________________ instanciar classes _____________________

barbeariaDB = Conexao("barbearia","localhost","5432","postgres","postgres")
agenda = Agendamentos()
cliente = Clientes()
item = Itens()
produto = Produtos()
Venda = Vendas()

CriarTodasTabelas(barbeariaDB)
#_______________________ início do while _____________________

op = True
while op != "0":
    op = visualizarMenu()

    match op:
        case "1": 
            sqlCliente= cliente.inserirNovoCliente()
            resultado = barbeariaDB.manipularBanco(sqlCliente)
            mensagemDeConfirmacao(resultado)
        case "2":
            sqlAgenda = agenda.verAgenda()
            resultado = barbeariaDB.consultarBanco(sqlAgenda)
            listaHorasAgenda = agenda.ListaHorariosAgenda(resultado)
            sqlAgenda = agenda.marcarHora(listaHorasAgenda)
            resultado = barbeariaDB.manipularBanco(sqlAgenda)
            mensagemDeConfirmacao(resultado)
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
            delOrUP = mensagemEscolherDeletarOuAtualizarCliente()
            if delOrUP == "Atualizar":
                opcaoID = mensagemAtualizarCliente(listaIdClientes)
                if opcaoID:
                    sqlUpdate = cliente.atualizarCliente(opcaoID)
                    if sqlUpdate:
                        resultado = barbeariaDB.manipularBanco(sqlUpdate)
                        mensagemDeConfirmacao(resultado)
            elif delOrUP == "Deletar":
                opcaoID = mensagemDeletarCliente(listaIdClientes)
                if opcaoID:
                    sqlDelete = cliente.deletarCliente(opcaoID)
                    if sqlDelete:
                        resultado = barbeariaDB.manipularBanco(sqlDelete)
                        mensagemDeConfirmacao(resultado)
            else:
                pass
        case "6":
            sqlAgenda = agenda.verAgenda()
            resultado = barbeariaDB.consultarBanco(sqlAgenda)
            listaHoraAgenda = mensagemListaAgenda(resultado)
        case "7":
            sqlProduto = produto.verProduto()
            resultado = barbeariaDB.consultarBanco(sqlProduto)
            listaIdProdutos = mensagemListaProdutos(resultado)     
            delOrUP = mensagemEscolherDeletarOuAtualizarProduto() 
            if delOrUP == "Atualizar": 
                opcaoID = mensagemAtualizarProduto(listaIdProdutos)
                if opcaoID:
                    sqlUpdate = produto.atualizarProduto(opcaoID)
                    if sqlUpdate:
                        resultado = barbeariaDB.manipularBanco(sqlUpdate)
                        mensagemDeConfirmacao(resultado)
            elif delOrUP == "Deletar":
                opcaoID = mensagemDeletarProduto(listaIdClientes)
                if opcaoID:
                    sqlDelete = produto.deletarProduto(opcaoID)
                    if sqlDelete:
                        resultado = barbeariaDB.manipularBanco(sqlDelete)
                        mensagemDeConfirmacao(resultado)
            else:
                pass
        case "8":
            pass

print("Obrigado por usar o sysBarber!")        

        






