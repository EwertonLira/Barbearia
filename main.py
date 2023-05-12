# sistema de gerenciamento de barbearia
from control.classConexao import *
from control.criarTabelas import *
from model.classCliente import *
from view.menu import *

#_______________________ instanciar classes _____________________

barbeariaDB = Conexao("barbearia","localhost","5432","postgres","postgre")
cliente = Clientes()


#_______________________ instanciar classes _____________________

#tabela cliente foi criada, foi colocada em comentário para não gerar um erro

resultado = barbeariaDB.manipularBanco(criarTabelaClientes())
if resultado:
    print("tabela cliente criada")
else:
    print("erro ao tentar criar a tabela cliente")

op = True
while op != "0":
    op = visualizarMenu()

    match op:
        case "1": 
            sqlCliente= cliente.inserirNovoCliente()
            resultado = barbeariaDB.manipularBanco(sqlCliente)
            mensagemDeconfirmacao(resultado)
        case "2":
            pass
        case "3":
            pass
        case "4":
            pass
        case "5":
            sqlCliente = cliente.verCliente()
            resultado = barbeariaDB.consultarBanco(sqlCliente)
            
            visualizarListaClientes(resultado)      
            opcaoID = input("Digite o ID do Cliente a ser atualizado: ")
            
            sqlUpdate = cliente.atualizarCliente(opcaoID)
            resultado = barbeariaDB.manipularBanco(sqlUpdate)
            mensagemDeconfirmacao(resultado)
        case "6":
            pass
        case "7":
            pass
        case "8":
            pass

print("Obrigado por usar o sysBarber!")        

        






