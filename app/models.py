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

