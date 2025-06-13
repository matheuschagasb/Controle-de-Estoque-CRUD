CREATE DATABASE IF NOT EXISTS controleEstoque
  DEFAULT CHARACTER SET utf8mb4
  DEFAULT COLLATE utf8mb4_unicode_ci;

USE controleEstoque;

CREATE TABLE IF NOT EXISTS produtos (
  codigo INT NOT NULL AUTO_INCREMENT,
  nome VARCHAR(50) NOT NULL,
  descricao VARCHAR(100) NOT NULL,
  custo_produto DECIMAL(10,2) NOT NULL CHECK (custo_produto >= 0),
  custo_fixo DECIMAL(5,2) NOT NULL CHECK (custo_fixo >= 0),
  comissao DECIMAL(5,2) NOT NULL CHECK (comissao >= 0),
  imposto DECIMAL(5,2) NOT NULL CHECK (imposto >= 0),
  margem_lucro DECIMAL(5,2) NOT NULL,
  PRIMARY KEY (codigo)
);

#INSERT INTO produtos (nome, descricao, custo_produto, custo_fixo, comissao, imposto, margem_lucro) VALUES
#('Caneta', 'Caneta profissional', 36, 15, 5, 12, 20),
#('Lapis', 'Preto B2', 1, 1, 1, 1, 1),
#('Caderno', 'Palmeiras', 10, 10, 10, 10, 50),
#('Caderno', 'São Paulo', 10, 10, 10, 10, 0),
#('Caderno', 'Corinthians', 10, 10, 10, 10, -20),
#('Caderno', 'Ponte Preta', 10, 30, 20, 20, 29.99);

#delete from produtos where codigo='111';

#update produtos set custo_produto = '5000' where codigo = '222';

#truncate produtos;

#select * from produtos;
