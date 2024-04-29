create database ProjetoIntegrador;

use ProjetoIntegrador;

create table produtos(
codigo int not null,
nome varchar (50) not null, 
descricao varchar(50) not null, 
custo_produto decimal (10,2) not null,
custo_fixo decimal (5,2) not null,
comissao decimal (5,2) not null,
imposto decimal (5,2) not null, 
margem_lucro decimal (5,2) not null,
primary key (codigo)
);

#drop table produtos;

insert into produtos values 
('1', 'Caneta', 'Caneta profissional', '36', '15', '5', '12', '20'),
('2', 'Lapis', 'Preto B2', '1', '1', '1', '1', '1'),
('3', 'Caderno', 'Palmeiras', '10', '10', '10', '10', '50'),
('4', 'Caderno', 'São Paulo', '10', '10', '10', '10', '0'),
('5', 'Caderno', 'Corinthians', '10', '10', '10', '10', '-20'),
('6', 'Caderno', 'Ponte Preta', '10', '30', '20', '20', '29.99');

#delete from produtos where codigo='111';

#update produtos set custo_produto = '5000' where codigo = '222';

#truncate produtos;

#select * from produtos;