print()
print()
print ("PROGRAMA DE CONTROLE DE ESTOQUE DE PRODUTOS") 

import mysql.connector #importando a biblioteca mysql

conexao = mysql.connector.connect( #Objeto de conexao
    host= '',
    database='',
    user= '',
    password= '')

if conexao.is_connected(): #Avaliar conexao com banco de dados
    print ("Conectado ao banco de dados com sucesso! ")
    cursor = conexao.cursor() #Executar comandos dentro do banco de dados
#cursor.execute('select * from produtos;') #executando o comando para mostrar todos os prdutos cadastradas
#registros = cursor.fetchall() #recuperar/ler todos os registros

def apresenteSe ():
    print('+-------------------------------------------------------------+')
    print('|                                                             |')
    print('| CONTROLE DE ESTOQUE                                         |')
    print('|                                                             |')
    print('+-------------------------------------------------------------+')

def umTexto (solicitacao, mensagem, valido):
    digitouDireito=False
    while not digitouDireito:
        txt=input(solicitacao)

        if txt not in valido:
            print(mensagem,'- Favor redigitar...')
        else:
            digitouDireito=True

    return txt

def opcaoEscolhida (mnu):
    print ()

    opcoesValidas=[]
    posicao=0
    while posicao<len(mnu):
        print (posicao+1,') ',mnu[posicao],sep='')
        opcoesValidas.append(str(posicao+1))
        posicao+=1

    print()
    return umTexto('Qual é a sua opção? ', 'Opção inválida', opcoesValidas)

'''
procura nom em agd e, se achou, retorna:
uma lista contendo True e a posicao onde achou;
MAS, se não achou, retorna:
uma lista contendo False e a posição onde inserir,
aquilo que foi buscado, mas nao foi encontrado,
mantendo a ordenação da lista.
'''

def ondeEsta (nom,agd):
    inicio=0
    final =len(agd)-1
    
    while inicio<=final:
        meio=(inicio+final)//2
        
        if nom.upper()==agd[meio][0].upper():
            return [True,meio]
        elif nom.upper()<agd[meio][0].upper():
            final=meio-1
        else: # nom.upper()>agd[meio][0].upper()
            inicio=meio+1
            
    return [False,inicio]

def incluir (agd):
    digitouDireito=False
    while not digitouDireito:
        codigoCadastro=input('\nCódigo do Produto: ')

        resposta=ondeEsta(codigoCadastro,agd)
        achou   = resposta[0]
        posicao = resposta[1]

        if achou:
            print ('Produto já existente - Favor redigitar...')
        else:
            digitouDireito=True
            
    nomeCadastro = input("Digite o nome do produto: ")
    descricaoCadastro = input("Digite a descricao do produto: ")
    custoProdCadastro = input("Digite o Custo do produto: ")
    custoFixoCadastro = input("Digite o Custo fixo do produto em porcentagem: ")
    comissaoCadastro = input("Digite a Comissão de venda em porcentagem: ")
    impostoCadastro = input("Digite o imposto em porcentagem: ")
    margem_lucroCadastro = input("Digite o Lucro em porcentagem: ")

    contato_cadastro = [codigoCadastro, nomeCadastro, descricaoCadastro, custoProdCadastro, custoFixoCadastro, comissaoCadastro, impostoCadastro, margem_lucroCadastro]

    agd.insert(posicao,contato_cadastro)
    #fazer um check pra ver se tem o mesmo id
    print('Cadastro realizado com sucesso!')

    comando = f"""insert into produtos (codigo, nome, descricao, custo_produto, custo_fixo, comissao, imposto, margem_lucro) values 
    ('{codigoCadastro}', '{nomeCadastro}', '{descricaoCadastro}', '{custoProdCadastro}', '{custoFixoCadastro}', '{comissaoCadastro}', '{impostoCadastro}', '{margem_lucroCadastro}');"""

    cursor.execute(comando) #executa o comando
    conexao.commit() #edita o banco de dados

def atualizar (agd):

    print()
    digitouDireito=False
    while not digitouDireito:
        codigoCadastro=input('Código do Produto: ')
        
        resposta=ondeEsta(codigoCadastro,agd)
        achou   = resposta[0]
        posicao = resposta[1]
        
        if not achou:
            print ('Produto inexistente - Favor redigitar...')
        else:
            digitouDireito=True

    escolhavalida = False

    print("\n| 1) Nome do Produto      |")
    print("| 2) Descrição do Produto   |")
    print("| 3) Custo do Produto       |")
    print("| 4) Custo fixo do produto  |")
    print("| 5) Comissão de Vendas     |")
    print("| 6) Imposto                |")
    print("| 7) Margem de Lucro        | \n")

    #contato_cadastro = [codigoCadastro, nomeCadastro, descricaoCadastro, custoProdCadastro, custoFixoCadastro, comissaoCadastro, impostoCadastro, margem_lucroCadastro]

    

    while not escolhavalida:        
        
        op_att = int(input("Qual Dado você quer alterar? "))
         
        if op_att == 1:

            nomeCadastro = input('Nome do Produto: ')
            agd[posicao][1] = nomeCadastro
            
            comando = f"""update produtos set nome  = '{nomeCadastro}' where codigo ='{codigoCadastro}'; """

            cursor.execute(comando) #executa o comando
            conexao.commit() #edita o banco de dados

            
        elif op_att == 2:
             
            descricaoCadastro =input('Descrição do Produto: ')
            agd[posicao][2] = descricaoCadastro
        
            comando = f"""update produtos set descricao  = '{descricaoCadastro}' where codigo ='{codigoCadastro}'; 
            """

            cursor.execute(comando) #executa o comando
            conexao.commit() #edita o banco de dados

          
        elif op_att == 3:

            custoProdCadastro = input('Custo do Produto: ')
            agd[posicao][3] = custoProdCadastro

            comando = f"""update produtos set custo_produto  = '{custoProdCadastro}' where codigo ='{codigoCadastro}';
            """

            cursor.execute(comando) #executa o comando
            conexao.commit() #edita o banco de dados


        elif op_att == 4:
            custoFixoCadastro = input('Custo fixo do Produto: ')
            agd[posicao][4] = custoFixoCadastro
            
            comando = f"""update produtos set custo_fixo  = '{custoFixoCadastro}' where codigo ='{codigoCadastro}';
            """

            cursor.execute(comando) #executa o comando
            conexao.commit() #edita o banco de dados


        elif op_att == 5:
            comissaoCadastro = input('Comissão de Vendas: ')
            agd[posicao][5] = comissaoCadastro

            comando = f"""update produtos set comissao  = '{comissaoCadastro}' where codigo ='{codigoCadastro}';
            """

            cursor.execute(comando) #executa o comando
            conexao.commit() #edita o banco de dados


        elif op_att == 6:
            impostoCadastro = input('Imposto: ')
            agd[posicao][6] = impostoCadastro

            comando = f"""update produtos set comissao  = '{impostoCadastro}' where codigo ='{codigoCadastro}';
            """

            cursor.execute(comando) #executa o comando
            conexao.commit() #edita o banco de dados


        elif op_att == 7:
            margem_lucroCadastro = input('Margem de Lucro: ')
            agd[posicao][7] = margem_lucroCadastro

            comando = f"""update produtos set comissao  = '{margem_lucroCadastro}' where codigo ='{codigoCadastro}';
            """  

            cursor.execute(comando) #executa o comando
            conexao.commit() #edita o banco de dados


        else:
            print("digitar um numero valido")
    
        op_continuar = input("Deseja alterar novamente? (S ou N)")
    
        if op_continuar in ['s','S']:
            atualizar(agd)
            print('Escolheu continuar \n')
        elif op_continuar in ['n','N']:
            print('Voltando ao menu')
            escolhavalida = True
        else:
            print('Digite N ou S')


def listar (agd):
    
    if not agd:
        print()
        print('Não há produtos cadastrados!')
  
    else:
        cursor = conexao.cursor() #Executar comandos dentro do banco de dados
        cursor.execute('select * from produtos;') #executando o comando para mostrar todos os prdutos cadastradas
        registros = cursor.fetchall() #recuperar/ler todos os registros
        print()
        print('Classificação de produtos Cadastrados')
        for dados in registros:

            #transformando em variáveis python as variáveis do mysql
            codigo, nome, descricao, custo_produto, custo_fixo, comissao, imposto, margem_lucro = dados

            #transformando as porcentagens lidas nos respectivos valores (se o custo do produto fosse 100 por cento do valor mas o preço da venda que é)
            valor_rentabilidade_compra = (custo_produto/100) * margem_lucro
            print()
            print("-"*120)
            print()
            print (f"Produto - {codigo}:")
            print (f"O valor de margem de lucro será (em relação ao preço de compra do {nome} {descricao}): {valor_rentabilidade_compra:.2f} \
e seu percentual é de {margem_lucro:.2f}%")

            #calculo do preço de venda
            preco_venda = custo_produto / (1 - ((custo_fixo + comissao + imposto + margem_lucro)/(100)))
            print()
            print (f"PREÇO DE VENDA DO PRODUTO {codigo}: {preco_venda:.2f}")
            print()

            valor_receita_bruta = preco_venda - custo_produto

            #transformando as porcentagens lidas nos respectivos valores
            valor_custo_fixo = (preco_venda/100) * custo_fixo
            valor_comissao = (preco_venda/100) * comissao
            valor_impostos = (preco_venda/100) * imposto 

            # "outros custos" é na verdade a soma do custo fixo, comissao e impostos
            valor_outros_custos = valor_custo_fixo + valor_comissao + valor_impostos

            valor_rentabilidade = valor_receita_bruta - valor_outros_custos # ou valor_rentabilidade = (preco_venda/100) * margem_lucro

            #valores desejados com relação ao preço de venda
            #print (f"O valor do custo fixo será (em relação ao preço de venda do {nome}): {valor_custo_fixo:.2f}")
            #print (f"O valor da comissão será (em relação ao preço de venda do {nome}): {valor_comissao:.2f}")
            #print (f"O valor dos impostos será (em relação ao preço de venda do {nome}): {valor_impostos:.2f}")
            print (f"O valor de margem de lucro será (em relação ao preço de venda do {nome} {descricao}): {valor_rentabilidade:.2f} \
e seu percentual é de {margem_lucro:.2f}%")
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



def excluir (agd):
    print()
    
    digitouDireito=False
    while not digitouDireito:
        codigoCadastro=input('Código do Produto: ')
        
        resposta=ondeEsta(codigoCadastro,agd)
        achou   = resposta[0]
        posicao = resposta[1]
        
        if not achou:
            print ('Produto inexistente - Favor redigitar...')
        else:
            digitouDireito=True

    print('Nome do Produto:',agd[posicao][1])
    print('Descrição do Produto:',agd[posicao][2])
    print('Custo do Produto:',agd[posicao][3])
    print('Custo Fixo do Produto:',agd[posicao][4])
    print('Comissão de Vendas:',agd[posicao][5])
    print('Imposto:',agd[posicao][6])
    print('Margem de Lucro :',agd[posicao][7])

    print()
    resposta=umTexto('Deseja realmente excluir? (S ou N) ','Você deve digitar S ou N',['s','S','n','N'])
    
    if resposta in ['s','S']:
        del agd[posicao]
        print('Remoção realizada com sucesso!')
        comando = f"""delete from produtos where codigo ='{codigoCadastro}';
            """
        
        cursor.execute(comando) #executa o comando
        conexao.commit() #edita o banco de dados

    elif resposta in ['n','N']:
        print('Remoção não realizada!')
    else:
        print('Digite N ou S')



apresenteSe()

agenda=[]

menu=['Incluir Produto',\
      'Atualizar Produto',\
      'Classificação de Lucro',\
      'Excluir Produtos',\
      'Finalizar Programa']


opcao=666
while opcao!=5:
    opcao = int(opcaoEscolhida(menu))

    if opcao==1:
        incluir(agenda)
    elif opcao==2:
        atualizar(agenda)
    elif opcao==3:
        listar(agenda)
    elif opcao==4:
        excluir(agenda)

print('OBRIGADO POR USAR ESTE PROGRAMA!')

cursor.close() #fechando a conexão, independente do resultado
conexao.close()
