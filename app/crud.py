from models import ondeEsta, umTexto

def incluir(agd, cursor, conexao):
    while True:
        codigoCadastro = input('\nCódigo do Produto (ou 0 para cancelar): ')
        if codigoCadastro == '0':
            print('Inclusão cancelada. Voltando ao menu.')
            return

        resposta = ondeEsta(codigoCadastro, agd)
        achou = resposta[0]
        posicao = resposta[1]

        if achou:
            print('Produto já existente - Favor redigitar...')
        else:
            break

    nomeCadastro = input("Digite o nome do produto: ")
    descricaoCadastro = input("Digite a descricao do produto: ")
    custoProdCadastro = input("Digite o Custo do produto: ")
    custoFixoCadastro = input("Digite o Custo fixo do produto em porcentagem: ")
    comissaoCadastro = input("Digite a Comissão de venda em porcentagem: ")
    impostoCadastro = input("Digite o imposto em porcentagem: ")
    margem_lucroCadastro = input("Digite o Lucro em porcentagem: ")

    contato_cadastro = [
        codigoCadastro, nomeCadastro, descricaoCadastro, custoProdCadastro,
        custoFixoCadastro, comissaoCadastro, impostoCadastro, margem_lucroCadastro
    ]

    agd.insert(posicao, contato_cadastro)
    print('Cadastro realizado com sucesso!')

    comando = (
        f"insert into produtos (codigo, nome, descricao, custo_produto, custo_fixo, comissao, imposto, margem_lucro) values "
        f"('{codigoCadastro}', '{nomeCadastro}', '{descricaoCadastro}', '{custoProdCadastro}', "
        f"'{custoFixoCadastro}', '{comissaoCadastro}', '{impostoCadastro}', '{margem_lucroCadastro}');"
    )

    cursor.execute(comando)
    conexao.commit()


def atualizar(agd, cursor, conexao):
    print()
    if not agd:
        print('Não há produtos cadastrados!')
        return
    while True:
        codigoCadastro = input('Código do Produto (ou 0 para cancelar): ')
        if codigoCadastro == '0':
            print('Atualização cancelada. Voltando ao menu.')
            return

        resposta = ondeEsta(codigoCadastro, agd)
        achou = resposta[0]
        posicao = resposta[1]

        if not achou:
            print('Produto inexistente - Favor redigitar...')
        else:
            break

    while True:
        print("\n| 1) Nome do Produto       |")
        print("| 2) Descrição do Produto   |")
        print("| 3) Custo do Produto       |")
        print("| 4) Custo fixo do produto  |")
        print("| 5) Comissão de Vendas     |")
        print("| 6) Imposto                |")
        print("| 7) Margem de Lucro        |")
        print("| 0) Cancelar atualização   |\n")

        try:
            op_att = int(input("Qual Dado você quer alterar? (0 para cancelar) "))
        except ValueError:
            print("Digite um número válido entre 0 e 7.")
            continue

        if op_att == 0:
            print('Atualização cancelada. Voltando ao menu.')
            break

        if op_att < 1 or op_att > 7:
            print("Digite um número válido entre 1 e 7.")
            continue

        if op_att == 1:
            nomeCadastro = input('Nome do Produto: ')
            agd[posicao][1] = nomeCadastro
            comando = f"update produtos set nome  = '{nomeCadastro}' where codigo ='{codigoCadastro}';"
        elif op_att == 2:
            descricaoCadastro = input('Descrição do Produto: ')
            agd[posicao][2] = descricaoCadastro
            comando = f"update produtos set descricao  = '{descricaoCadastro}' where codigo ='{codigoCadastro}';"
        elif op_att == 3:
            custoProdCadastro = input('Custo do Produto: ')
            agd[posicao][3] = custoProdCadastro
            comando = f"update produtos set custo_produto  = '{custoProdCadastro}' where codigo ='{codigoCadastro}';"
        elif op_att == 4:
            custoFixoCadastro = input('Custo fixo do Produto: ')
            agd[posicao][4] = custoFixoCadastro
            comando = f"update produtos set custo_fixo  = '{custoFixoCadastro}' where codigo ='{codigoCadastro}';"
        elif op_att == 5:
            comissaoCadastro = input('Comissão de Vendas: ')
            agd[posicao][5] = comissaoCadastro
            comando = f"update produtos set comissao  = '{comissaoCadastro}' where codigo ='{codigoCadastro}';"
        elif op_att == 6:
            impostoCadastro = input('Imposto: ')
            agd[posicao][6] = impostoCadastro
            comando = f"update produtos set imposto  = '{impostoCadastro}' where codigo ='{codigoCadastro}';"
        elif op_att == 7:
            margem_lucroCadastro = input('Margem de Lucro: ')
            agd[posicao][7] = margem_lucroCadastro
            comando = f"update produtos set margem_lucro  = '{margem_lucroCadastro}' where codigo ='{codigoCadastro}';"

        cursor.execute(comando)
        conexao.commit()
        print('Alteração realizada com sucesso!')

        op_continuar = input("Deseja alterar outro dado deste produto? (S ou N): ")
        if op_continuar.lower() != 's':
            print('Voltando ao menu')
            break


def listar(agd, cursor):
    if not agd:
        print()
        print('Não há produtos cadastrados!')
    else:
        cursor.execute('select * from produtos;')
        registros = cursor.fetchall()
        print()
        print('Classificação de produtos Cadastrados')
        for dados in registros:
            codigo, nome, descricao, custo_produto, custo_fixo, comissao, imposto, margem_lucro = dados

            # Conversão para float
            custo_produto = float(custo_produto)
            custo_fixo = float(custo_fixo)
            comissao = float(comissao)
            imposto = float(imposto)
            margem_lucro = float(margem_lucro)

            valor_rentabilidade_compra = (custo_produto / 100) * margem_lucro
            print()
            print("-" * 120)
            print()
            print(f"Produto - {codigo}:")
            print(f"O valor de margem de lucro será (em relação ao preço de compra do {nome} {descricao}): {valor_rentabilidade_compra:.2f} "
                  f"e seu percentual é de {margem_lucro:.2f}%")
            preco_venda = custo_produto / (1 - ((custo_fixo + comissao + imposto + margem_lucro) / 100))
            print()
            print(f"PREÇO DE VENDA DO PRODUTO {codigo}: {preco_venda:.2f}")
            print()
            valor_receita_bruta = preco_venda - custo_produto
            valor_custo_fixo = (preco_venda / 100) * custo_fixo
            valor_comissao = (preco_venda / 100) * comissao
            valor_impostos = (preco_venda / 100) * imposto
            valor_outros_custos = valor_custo_fixo + valor_comissao + valor_impostos
            valor_rentabilidade = valor_receita_bruta - valor_outros_custos
            print(f"O valor de margem de lucro será (em relação ao preço de venda do {nome} {descricao}): {valor_rentabilidade:.2f} "
                  f"e seu percentual é de {margem_lucro:.2f}%")
            print()
            print("CLASSIFICAÇÃO DE LUCRO: ")
            if margem_lucro > 20:
                print("\033[34m" + "Lucro Alto" + "\033[0m")
            elif margem_lucro > 10 and margem_lucro <= 20:
                print("\033[32m" + "Lucro Médio" + "\033[0m")
            elif margem_lucro > 0 and margem_lucro <= 10:
                print("\033[33m" + "Lucro Baixo" + "\033[0m")
            elif margem_lucro == 0:
                print("Equilíbrio")
            else:
                print("\033[31m" + "Prejuízo" + "\033[0m")


def excluir(agd, cursor, conexao):
    print()
    if not agd:
        print('Não há produtos cadastrados!')
        return
    while True:
        codigoCadastro = input('Código do Produto (ou 0 para cancelar): ')
        if codigoCadastro == '0':
            print('Exclusão cancelada. Voltando ao menu.')
            return

        resposta = ondeEsta(codigoCadastro, agd)
        achou = resposta[0]
        posicao = resposta[1]
        if not achou:
            print('Produto inexistente - Favor redigitar...')
        else:
            break

    print('Nome do Produto:', agd[posicao][1])
    print('Descrição do Produto:', agd[posicao][2])
    print('Custo do Produto:', agd[posicao][3])
    print('Custo Fixo do Produto:', agd[posicao][4])
    print('Comissão de Vendas:', agd[posicao][5])
    print('Imposto:', agd[posicao][6])
    print('Margem de Lucro :', agd[posicao][7])
    print()
    resposta = umTexto('Deseja realmente excluir? (S ou N) ', 'Você deve digitar S ou N', ['s', 'S', 'n', 'N'])
    if resposta in ['s', 'S']:
        del agd[posicao]
        print('Remoção realizada com sucesso!')
        comando = f"delete from produtos where codigo ='{codigoCadastro}';"
        cursor.execute(comando)
        conexao.commit()
    elif resposta in ['n', 'N']:
        print('Remoção não realizada!')
    else:
        print('Digite N ou S')

