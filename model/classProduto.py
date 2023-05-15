class Produtos:
    def __init__(self):
        self._id = "id"
        self._nome = "nome"
        self._preco = 0
        self._quantidade = 0

    def _inputProduto(self):
        
        self._nome = input("Insira o nome do produto: ")
        self._preco = input("Insira o preço do produto: ")
        self._quantidade = input("Insira a quantidade do produto: ")
    
    def _verificadorDeSeparadorNumerico(valorInserido):
        valorInserido
        
    def verProduto(self):
        sql = f'''
        SELECT * FROM "produtos"
        ORDER BY "produto_nome" ASC
        '''
        return sql

    def inserirNovoProduto(self):
        print("Insira os dados do Produto")
        
        self._inputProduto()

        sql = f'''
        INSERT INTO "produtos"
        Values(default, '{self._nome}', '{self._preco}', '{self._quantidade}')
        '''
        return sql

    def atualizarProduto(self, produtoID):   
        opCampo = "a"
        while not(opCampo in "1|2|3|4|0"):
            print('''qual campo deseja atualizar do produto?
            [1] 🔤 Nome
            [2] 🏷️ Preço
            [3] 🧮 Quantidade
            [4] Todos
            [0] ↩️ Voltar ao menu principal
            ''')
            opCampo = input(": ")
            match opCampo:
                case "1":
                    self._nome = input("Insira o nome do produto: ")
                    sql = f'''
                        UPDATE "produtos"
                        SET "produto_nome" = '{self._nome}'
                        WHERE "produto_id" = '{produtoID}';
                        '''
                case "2":
                    self._telefone = input("Insira o preço do produto: ")
                    sql = f'''
                        UPDATE "produtos"
                        "produto_preco" = '{self._preco}'
                        WHERE "produto_id" = '{produtoID}';
                        '''
                case "3":
                    self._email = input("Insira a quantidade do produto: ")
                    sql = f'''
                        UPDATE "produtos"
                        "produto_quantidade" = '{self._quantidade}
                        WHERE "produto_id" = '{produtoID}';
                        '''
                case "4":
                    self._inputProduto()
                    sql = f'''
                    UPDATE "produtos"
                    SET "produto_nome" = '{self._nome}',
                        "produto_preco" = '{self._preco}',
                        "produto_quantidade" = '{self._quantidade}'
                    WHERE "produto_id" = '{produtoID}';
                    '''
                case "0":
                    sql = None
                case _:
                    print("comando inválido Tente novamente")
                    input("aperte [Enter↵] para continuar")

            return sql
