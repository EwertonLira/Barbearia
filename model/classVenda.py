from datetime import *

class Vendas:
    def __init__(self):
        self._id = "id"
        self._clienteID = "clienteID"
        self._horaVenda = datetime.today()
    
    def setVendaCliente(self, IdCliente):
        self._clienteID = IdCliente

    def ExecutarVenda(self): 
        
        sql = f'''
        INSERT INTO "vendas"
        Values(default, '{self._clienteID}', '{self._horaVenda}')
        '''
        return sql

    def verVenda(self):
        sql = f'''
        SELECT * FROM "vendas"
        ORDER BY "venda_id" ASC
        '''
        return sql
