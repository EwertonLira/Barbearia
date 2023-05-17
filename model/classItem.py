class Itens:
    def __init__(self):
        self._id = "id"
        self._produtoId= "produtoId"
        self._vendaId = "vendaID"
        self._quantidade = "quantidade"
    
    def setQuantidade(self,quantidade):
        self._quantidade = quantidade

    def criarItem(self,):
        sql = f'''
        INSERT INTO "vendas"
        Values(default, '{self._produtoId}', '{self._vendaId}', '{self._quantidade}')
        '''
        return sql