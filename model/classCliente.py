class Clientes:
    def __init__(self):
        self._id = "id"
        self._nome = "nome"
        self._telefone = "telefone"
        self._email = "email" # ideia! mudar email para endereço eletronico qualquer, como instagram, facebook e etc

    def _inputCliente(self):
        
        self._nome = input("Insira o nome do cliente: ")
        self._telefone = input("Insira o número de telefone do cliente: ")
        self._email = input("Insira o email do cliente: ")
    
    def verCliente(self):
        # ideia! talvez mudar o ordenamento da lista por nome(ordem alfabética) do que por ID
        sql = f'''
        SELECT * FROM "clientes"
        ORDER BY "cliente_nome" ASC
        '''
        return sql

    def inserirNovoCliente(self):
        print("Insira os dados do Cliente")
        
        self._inputCliente()

        sql = f'''
        INSERT INTO "clientes"
        Values(default, '{self._nome}', '{self._telefone}', '{self._email}')
        '''
        return sql

    def atualizarCliente(self, clienteID):   
        
        self._inputCliente()
        
        sql = f'''
        UPDATE "clientes"
        SET "cliente_nome" = '{self._nome}',
            "cliente_telefone" = '{self._telefone}',
            "cliente_email" = '{self._email}'
        WHERE "cliente_id" = '{clienteID}';
        '''
        return sql


        















class Produtos:
    def __init__(self, id, nome, preco, quantidade):
        self._id = id
        self._nome = nome
        self._preco = preco
        self._quantidade = quantidade

class Servicos:
    def __init__(self, id, nome, preco, tempoExecucao):
        self._id = id
        self._nome = nome
        self._preco = preco
        self._tempoExecucao = tempoExecucao

class Vendas:
    def __init__(self, id, clienteID, produtoID, servicoID, nome, preco, tempoExecucao):
        self._id = id
        self._clienteID = clienteID
        self._produtoID = produtoID
        self._servicoID = servicoID
        self._nome = nome
        self._preco = preco
        self._tempoExecucao = tempoExecucao

class Itens:
    def __init__(self, id, vendaID, descricao, quantidade):
        self._id = id
        self._vendaId = vendaID
        self._descricao = descricao
        self._quantidade = quantidade

class Agendamentos:
    def __init__(self, id, clienteID, servicoID, horario):
        self._id = id
        self._clienteID = clienteID
        self._servicoID = servicoID
        self._horario = horario