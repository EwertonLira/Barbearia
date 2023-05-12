# arquivo python que gera arquivos de texto SQL para criar tabelas
# essas funções devem ser usado com a conexão banco.

def criarTabelaClientes():
    sql ='''CREATE TABLE "clientes" (
    "cliente_id" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "cliente_nome" varchar(255) NOT NULL,
    "cliente_telefone" varchar(255) NOT NULL DEFAULT 'não informado',
    "cliente_email" varchar(255) NOT NULL DEFAULT 'não informado'
    );
    '''
    return sql

def criarTabelaProdutos():
    sql = '''CREATE TABLE "produtos" (
    "produto_id" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "produto_nome" varchar(255) NOT NULL,
    "produto_preco" numeric(6,2), NOT NULL,
    "produto_quantidade" int NOT NULL
    );
    '''
    return sql

def criarTabelaServicos():
    sql = '''CREATE TABLE "servicos" (
    "servico_id" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "servico_nome" varchar(255) NOT NULL,
    "servico_preco" numeric(6,2), NOT NULL,
    "servico_tempo_execucao" time NOT NULL
    );
    '''
    return sql

def criarTabelaVendas():
    sql = '''CREATE TABLE "vendas" (
    "venda_id" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "cliente_id" int NOT NULL,
    "produto_id" int ,
    "servico_id" int ,
    "venda_horario" timestamp DEFAULT CURRENT_TIMESTAMP(0)
    CONSTRAINT fk_cliente
        FOREIGN KEY ("cliente_id")
        REFERENCES "clientes"("cliente_id"),
    
    CONSTRAINT fk_produto
        FOREIGN KEY ("produto_id")
        REFERENCES "produtos"("produto_id")
    
    CONSTRAINT fk_servico
        FOREIGN KEY ("servico_id")
        REFERENCES "servicos"("servico_id")
    );
    '''
    return sql

# criarTabelavendaserviço caso a tabelavenda não de certo por causas das duas chaves estrangeiras.
def criarTabelaVendasServico():
    sql = '''CREATE TABLE "vendas" (
    "venda_id" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "cliente_id" int NOT NULL,
    "servico_id" int ,
    "venda_horario" timestamp DEFAULT CURRENT_TIMESTAMP(0)
    CONSTRAINT fk_cliente
        FOREIGN KEY ("cliente_id")
        REFERENCES "clientes"("cliente_id"),
    
    CONSTRAINT fk_servico
        FOREIGN KEY ("servico_id")
        REFERENCES "servicos"("servico_id")
    );
    '''
    return sql

# criartabelaVendasProduto foi feita caso a criartabelaVendas com duas chaves estrangeiras
# então será criada duas outras tabelas vendas: criartabelavendasProduto e criartabelavendasServiços 
def criarTabelaVendasProduto():
    sql = '''CREATE TABLE "vendas" (
    "venda_id" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "cliente_id" int NOT NULL,
    "produto_id" int ,
    "venda_horario" timestamp DEFAULT CURRENT_TIMESTAMP(0)
    CONSTRAINT fk_cliente
        FOREIGN KEY ("cliente_id")
        REFERENCES "clientes"("cliente_id"),
    
    CONSTRAINT fk_produto
        FOREIGN KEY ("produto_id")
        REFERENCES "produtos"("produto_id")
    
    );
    '''
    return sql

def criarTabelaItens():
    sql = '''CREATE TABLE "itens" (
    "item_id" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "venda_id" int,
    "item_descricao" varchar(255),
    "item_quantidade" varchar(255)
    CONSTRAINT fk_vendas
        FOREIGN KEY ("venda_id")
        REFERENCES "vendas"("venda_id")
    );
    '''
    return sql

def criarTabelaAgendamentos():
    sql ='''CREATE TABLE "agendamentos" (
    "agendamento_id" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    "cliente_id" int NOT NULL,
    "servico_id" int NOT NULL,
    "agendamento_horario" timestamp DEFAULT CURRENT_TIMESTAMP(0)
    
    CONSTRAINT fk_cliente
        FOREIGN KEY ("cliente_id")
        REFERENCES "clientes"("cliente_id"),
    
    CONSTRAINT fk_servico
        FOREIGN KEY ("servico_id")
        REFERENCES "servicos"("servico_id")
    );
    '''
    return sql