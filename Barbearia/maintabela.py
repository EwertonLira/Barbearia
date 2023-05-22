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

barbeariaDB = Conexao("barbearia","localhost","5432","postgres","postgre")
agenda = Agendamentos()
cliente = Clientes()
item = Itens()
produto = Produtos()
venda = Vendas()

CriarTodasTabelas(barbeariaDB)
#_______________________ início do while _____________________

op = True
while op != "0":
    op = visualizarMenu()

    match op:
        case "1": 
            sqlCliente= cliente.inserirNovoCliente()
            resultadoC = barbeariaDB.manipularBanco(sqlCliente)
            mensagemDeConfirmacao(resultadoC)

        case "2":
            sqlAgenda = agenda.verAgenda()
            resultadoA = barbeariaDB.consultarBanco(sqlAgenda)
            listaHorasAgenda = agenda.ListaHorariosAgenda(resultadoA)
            mensagemMarcarHora(agenda,listaHorasAgenda)
            sqlCliente = cliente.verCliente()
            resultadoC = barbeariaDB.consultarBanco(sqlCliente)
            listaIdClientes = mensagemListaClientes(resultadoC)
            idCliente = mensagemAgendamento("fraseI")            
            sqlProduto = produto.verProduto()
            resultadoP = barbeariaDB.consultarBanco(sqlProduto)
            listaIdProdutos = mensagemListaProdutos(resultadoP)
            idServico = mensagemAgendamento("fraseII")
            sqlAgenda = agenda.inserirAgendamento(idCliente,idServico)
            resultadoA = barbeariaDB.manipularBanco(sqlAgenda)
            mensagemDeConfirmacao(resultadoA)
            
            # ao fazer o agendamento também se faz a venda automática
            venda.setVendaCliente(idCliente) 
            sqlVenda = venda.ExecutarVenda()
            barbeariaDB.manipularBanco(sqlVenda)
            sqlVenda = venda.verVenda()
            resultadoV = barbeariaDB.consultarBanco(sqlVenda)
            listaIdvendas = mensagemListaVendas(resultadoV,1,barbeariaDB)
            item.setVendaId(listaIdvendas)     
            item.setProdutoId(idServico)
            item.setQuantidade(1)
            sqlItem = item.criarItem()
            resultadoI = barbeariaDB.manipularBanco(sqlItem)

        case "3":
            sqlProduto = produto.inserirNovoProduto()
            resultadoP = barbeariaDB.manipularBanco(sqlProduto)
            mensagemDeConfirmacao(resultadoP)

        case "4":
            sqlCliente = cliente.verCliente()
            resultadoC = barbeariaDB.consultarBanco(sqlCliente)
            listaIdClientes = mensagemListaClientes(resultadoC) 
            idCliente = mensagemVenda("fraseV")
            venda.setVendaCliente(idCliente)
            sqlVenda = venda.ExecutarVenda()
            barbeariaDB.manipularBanco(sqlVenda)
            sqlVenda = venda.verVenda()
            resultadoV = barbeariaDB.consultarBanco(sqlVenda)
            listaIdvendas = mensagemListaVendas(resultadoV,1,barbeariaDB)
            item.setVendaId(listaIdvendas)
            opCase4 = "rodarWhile"
            while opCase4 != "0":
                mensagemVenda("fraseI")
                sqlProduto = produto.verProduto()
                resultadoP = barbeariaDB.consultarBanco(sqlProduto)
                listaIdProdutos = mensagemListaProdutos(resultadoP)
                idProduto = mensagemVenda("fraseII")
                qtdProdutos = mensagemVenda("fraseIII")           
                item.setProdutoId(idProduto)
                item.setQuantidade(qtdProdutos)
                sqlItem = item.criarItem()
                resultadoI = barbeariaDB.manipularBanco(sqlItem)
                opCase4 = mensagemVenda("fraseIV")
            mensagemDeConfirmacao(True)

        case "5":
            sqlCliente = cliente.verCliente()
            resultadoC = barbeariaDB.consultarBanco(sqlCliente)
            listaIdClientes = mensagemListaClientes(resultadoC)      
            delOrUP = mensagemEscolherDeletarOuAtualizarCliente()
            if delOrUP == "Atualizar":
                opcaoID = mensagemAtualizarCliente(listaIdClientes)
                if opcaoID:
                    sqlUpdate = cliente.atualizarCliente(opcaoID)
                    if sqlUpdate:
                        resultadoUP = barbeariaDB.manipularBanco(sqlUpdate)
                        mensagemDeConfirmacao(resultadoUP)
            elif delOrUP == "Deletar":
                opcaoID = mensagemDeletarCliente(listaIdClientes)
                if opcaoID:
                    sqlDelete = cliente.deletarCliente(opcaoID)
                    if sqlDelete:
                        resultadoDEL = barbeariaDB.manipularBanco(sqlDelete)
                        mensagemDeConfirmacao(resultadoDEL)
            else:
                pass

        case "6":
            sqlAgenda = agenda.verAgenda()
            resultadoA = barbeariaDB.consultarBanco(sqlAgenda)
            _ , listaIdAgenda = mensagemListaAgenda(resultadoA,barbeariaDB)          
            delOrUp = mensagemEscolherDeletarOuAtualizarAgenda()
            if delOrUp == "Atualizar":
                _ , _ = mensagemListaAgenda(resultadoA,barbeariaDB)
                opcaoID = mensagemAtualizarAgenda(listaIdAgenda)
                if opcaoID:
                    sqlUpdate = agenda.atualizarAgenda(opcaoID)
                    if sqlUpdate:
                        resultadoUP = barbeariaDB.manipularBanco(sqlUpdate)
                        mensagemDeConfirmacao(resultadoUP)
            elif delOrUp == "Deletar":
                _ , _ = mensagemListaAgenda(resultadoA,barbeariaDB)
                opcaoID = mensagemDeletarAgenda(listaIdAgenda)
                if opcaoID:
                    sqlDelete = agenda.deletarAgenda(opcaoID)
                    if sqlDelete:
                        resultadoDEL = barbeariaDB.manipularBanco(sqlDelete)
                        mensagemDeConfirmacao(resultadoDEL)
            else:
                pass

        case "7":
            sqlProduto = produto.verProduto()
            resultadoP = barbeariaDB.consultarBanco(sqlProduto)
            listaIdProdutos = mensagemListaProdutos(resultadoP)     
            delOrUP = mensagemEscolherDeletarOuAtualizarProduto() 
            if delOrUP == "Atualizar": 
                opcaoID = mensagemAtualizarProduto(listaIdProdutos)
                if opcaoID:
                    sqlUpdate = produto.atualizarProduto(opcaoID)
                    if sqlUpdate:
                        resultadoUP = barbeariaDB.manipularBanco(sqlUpdate)
                        mensagemDeConfirmacao(resultadoUP)
            elif delOrUP == "Deletar":
                opcaoID = mensagemDeletarProduto(listaIdClientes)
                if opcaoID:
                    sqlDelete = produto.deletarProduto(opcaoID)
                    if sqlDelete:
                        resultadoDEL = barbeariaDB.manipularBanco(sqlDelete)
                        mensagemDeConfirmacao(resultadoDEL)
            else:
                pass

        case "8":
            sqlVenda = venda.verVenda()
            resultadoV = barbeariaDB.consultarBanco(sqlVenda)
            _ = mensagemListaVendas(resultadoV,2,barbeariaDB)
            listaIdvendas = mensagemListaVendas(resultadoV,1,barbeariaDB) # essa gera a lista
            delOrUP = mensagemEscolherDeletarOuAtualizarVenda()
            if delOrUP == "Deletar":
                opcaoID = mensagemDeletarVenda(listaIdvendas)
                if opcaoID:
                    sqlDelete = venda.deletarVenda(opcaoID)
                    if sqlDelete:
                        resultadoDEL = barbeariaDB.manipularBanco(sqlDelete)
                        mensagemDeConfirmacao(resultadoDEL)
            else:
                pass

print("Obrigado por usar o sysBarber!")        








