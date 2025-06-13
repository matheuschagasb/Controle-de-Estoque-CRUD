def carregar_agenda_do_banco(cursor):
    cursor.execute('SELECT * FROM produtos;')
    registros = cursor.fetchall()
    agenda = []
    for dados in registros:
        
        agenda.append([str(d) for d in dados])
    return agenda


def ondeEsta(nom, agd):
    inicio = 0
    final = len(agd) - 1
    while inicio <= final:
        meio = (inicio + final) // 2
        if nom.upper() == agd[meio][0].upper():
            return [True, meio]
        elif nom.upper() < agd[meio][0].upper():
            final = meio - 1
        else:
            inicio = meio + 1
    return [False, inicio]


def apresenteSe():
    print('+-------------------------------------------------------------+')
    print('|                                                             |')
    print('| CONTROLE DE ESTOQUE                                         |')
    print('|                                                             |')
    print('+-------------------------------------------------------------+')


def umTexto(solicitacao, mensagem, valido):
    digitouDireito = False
    while not digitouDireito:
        txt = input(solicitacao)
        if txt not in valido:
            print(mensagem, '- Favor redigitar...')
        else:
            digitouDireito = True
    return txt


def opcaoEscolhida(mnu):
    print()
    opcoesValidas = []
    posicao = 0
    while posicao < len(mnu):
        print(posicao + 1, ') ', mnu[posicao], sep='')
        opcoesValidas.append(str(posicao + 1))
        posicao += 1
    print()
    return umTexto('Qual é a sua opção? ', 'Opção inválida', opcoesValidas)


def finalizar(cursor, conexao):
    cursor.execute("TRUNCATE TABLE produtos;")
    conexao.commit()
    print("Tabela de produtos limpa. Programa finalizado.")
