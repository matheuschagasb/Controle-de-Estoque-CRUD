from db import get_connection
from crud import incluir, atualizar, listar, excluir
from models import apresenteSe, opcaoEscolhida, finalizar, carregar_agenda_do_banco

def main():
    conexao = get_connection()
    if conexao.is_connected():
        print("\nConectado ao banco de dados com sucesso!")
        cursor = conexao.cursor()
    else:
        print("Erro ao conectar ao banco de dados.")
        return

    apresenteSe()

    agenda = carregar_agenda_do_banco(cursor)

    menu = [
        'Incluir Produto',
        'Atualizar Produto',
        'Listar Produtos',
        'Excluir Produtos',
        'Finalizar Programa'
    ]

    opcao = 666
    while opcao != 5:
        opcao = int(opcaoEscolhida(menu))
        match opcao:
            case 1:
                incluir(agenda, cursor, conexao)
            case 2:
                atualizar(agenda, cursor, conexao)
            case 3:
                listar(agenda, cursor)
            case 4:
                excluir(agenda, cursor, conexao)
            case 5:
                finalizar(cursor, conexao)
                break
            case _:
                print("Opção inválida")

    print('OBRIGADO POR USAR ESTE PROGRAMA!')
    cursor.close()
    conexao.close()

if __name__ == "__main__":
    main()
