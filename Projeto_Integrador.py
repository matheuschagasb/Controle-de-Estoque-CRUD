print()
print()
print ("PROGRAMA DE CONEXÃO DE PRODUTOS") 

import mysql.connector #importando a biblioteca mysql

conexao = mysql.connector.connect( #Objeto de conexao
    host= 'localhost',
    database='ProjetoIntegrador',
    user= 'root',
    password= '')

if conexao.is_connected(): #Avaliar conexao com banco de dados
    print ("Conectado ao banco de dados com sucesso! ")
    cursor = conexao.cursor() #Executar comandos dentro do banco de dados
cursor.execute('select * from produtos;') #Mostrar todos os prdutos cadastradas
registros = cursor.fetchall() #recuperar todos os registros
'''for dados in registros:
    print (dados)
    
    codigo, nome, descricao, custo_produto, custo_fixo, comissao, imposto, margem_lucro = dados'''

'''
#mostrar todos os registros menos o primeiro
r=cursor.fetchone()
for r in cursor:
    print(r)'''
 
#cursor.close() #fechando a conexão, independente do resultado
#conexao.close()

print()
print()


'''
#caso a margem de lucro viesse automaticamente
valor_margem_lucro = custo_produto - valor_custo_fixo - valor_comissao - valor_impostos
porcentagem_margem_lucro = (valor_margem_lucro/custo_produto) * 100
'''

for dados in registros:
  
    #transformando em variáveis python as variáveis do mysql
    codigo, nome, descricao, custo_produto, custo_fixo, comissao, imposto, margem_lucro = dados

    #transformando as porcentagens lidas nos respectivos valores (se o custo do produto fosse 100 por cento do valor mas o preço da venda que é)
    valor_custo_fixo_compra  = (custo_produto/100) * custo_fixo
    valor_comissao_compra = (custo_produto/100) * comissao
    valor_impostos_compra = (custo_produto/100) * imposto
    valor_rentabilidade_compra = (custo_produto/100) * margem_lucro

    #valores desejados com relação ao preço de compra
    #print (f"O valor do custo fixo será (em relação ao preço de compra do {nome}): {valor_custo_fixo_compra:.2f}")
    #print (f"O valor da comissão será (em relação ao preço de compra do {nome}): {valor_comissao_compra:.2f}")
    #print (f"O valor dos impostos será (em relação ao preço de compra do {nome}): {valor_impostos_compra:.2f}")
    print (f"O valor de margem de lucro será (em relação ao preço de compra do {nome} {descricao}): {valor_rentabilidade_compra:.2f} \
e seu percentual é de {margem_lucro:.2f}%")

    #calculo do preço de venda
    preco_venda = custo_produto / (1 - ((custo_fixo + comissao + imposto + margem_lucro)/(100)))
    porcentagem_preco_venda = 100

    print()
    print (f"PREÇO DE VENDA DO {nome}: {preco_venda:.2f}")
    print()

    #criação do que faltava para tabela
    valor_custo_aquisicao = custo_produto
    porcentagem_custo_aquisicao = porcentagem_preco_venda - custo_fixo - comissao - imposto - margem_lucro

    valor_receita_bruta = preco_venda - custo_produto
    porcentagem_receita_bruta = porcentagem_preco_venda - porcentagem_custo_aquisicao

    #transformando as porcentagens lidas nos respectivos valores
    valor_custo_fixo = (preco_venda/100) * custo_fixo
    valor_comissao = (preco_venda/100) * comissao
    valor_impostos = (preco_venda/100) * imposto 


    # "outros custos" é na verdade a soma do custo fixo, comissao e impostos
    valor_outros_custos = valor_custo_fixo + valor_comissao + valor_impostos
    porcentagem_outros_custos = custo_fixo + comissao + imposto

    valor_rentabilidade = valor_receita_bruta - valor_outros_custos # ou valor_rentabilidade = (preco_venda/100) * margem_lucro

    #valores desejados com relação ao preço de venda
    #print (f"O valor do custo fixo será (em relação ao preço de venda do {nome}): {valor_custo_fixo:.2f}")
    #print (f"O valor da comissão será (em relação ao preço de venda do {nome}): {valor_comissao:.2f}")
    #print (f"O valor dos impostos será (em relação ao preço de venda do {nome}): {valor_impostos:.2f}")
    print (f"O valor de margem de lucro será (em relação ao preço de venda do {nome} {descricao}): {valor_rentabilidade:.2f} \
e seu percentual é de {margem_lucro:.2f}%")

    #visualização da tabela
    print(f"    {codigo} {nome}     {descricao}")
    print(f"{'-'*25} | {'-'*10} | {'-'*5}") 
    print (f"{'Descrição':^25} | {'Valor':^10} | {'%':^5}")
    print(f"{'-'*25} | {'-'*10} | {'-'*5}")

    print (f"{'A. Preço de Venda':<25} | {f'{preco_venda:.2f}':^10} | {f'{porcentagem_preco_venda}%':>5}")
    print (f"{'B. Custo de Aquisição':<25} | {f'{valor_custo_aquisicao:.2f}':^10} | {f'{porcentagem_custo_aquisicao:.0f}%':>5}")
    print (f"{'C. Receita Bruta (A-B)':<25} | {f'{valor_receita_bruta:.2f}':^10} | {f'{porcentagem_receita_bruta:.0f}%':>5}")
    print (f"{'D. Custo Fixo':<25} | {f'{valor_custo_fixo:.2f}':^10} | {f'{custo_fixo:.0f}%':>5}")
    print (f"{'E. Comissão de Vendas':<25} | {f'{valor_comissao:.2f}':^10} | {f'{comissao:.0f}%':>5}")
    print (f"{'F. Impostos':<25} | {f'{valor_impostos:.2f}':^10} | {f'{imposto:.0f}%':>5}")
    print (f"{'G. Outros custos (D+E+F)':<25} | {f'{valor_outros_custos:.2f}':^10} | {f'{porcentagem_outros_custos:.0f}%':>5}")
    print (f"{'H. Rentabilidade (C-G)':<25} | {f'{valor_rentabilidade:.2f}':^10} | {f'{margem_lucro:.0f}%':>5}")

    print()

    #imprimindo faixa de lucro com suas respectivas cores
    #"\033[32m" +: exemplo de mudar de cor para verde & + "\033[0m": volta para cor padrão
    print ("CLASSIFICAÇÃO DE LUCRO: ") 
    if margem_lucro>20:
        print("\033[34m" + "Lucro Alto" + "\033[0m") #azul
    elif margem_lucro >10 and margem_lucro<=20:
        print("\033[32m" + "Lucro Médio" + "\033[0m") #verde
    elif margem_lucro >0 and margem_lucro<=10:
        print("\033[33m" + "Lucro Baixo" + "\033[0m") #amarelo
    elif margem_lucro == 0:
        print("Equilíbrio")
    else:
        print("\033[31m" + "Prejuízo" + "\033[0m") #vermelho

    print ()
    cursor.close() #fechando a conexão, independente do resultado
    conexao.close()

print ("PROGRAMA FINALIZADO")