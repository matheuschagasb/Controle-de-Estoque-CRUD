print ("PROGRAMA DE INSERÇÃO DE PRODUTO") 
  
try: 
    codigo_produto = int(input("Digite o código do produto: ")) 
    if codigo_produto <= 0: 
        print("Código do produto deve apresentar números inteiros maior que zero! ") 
    else: 
        nome_produto = input("Digite o nome do produto: ") 
        descricao_produto = input("Digite a descrição do produto: ") 
        custo_produto = float(input("Digite o custo do produto: "))
        if custo_produto <=0: 
            print("Custo inválido")     
        else:
            porcentagem_custo_fixo= float(input("Digite o custo fixo do produto (em porcentagem): "))
            if porcentagem_custo_fixo <=0: 
                print("Valor tem que ser maior que 0")
            else: 
                porcentagem_comissao = float(input("Informe o valor da comissão da venda (em porcentagem): "))
                if porcentagem_comissao <=0: 
                    print("Valor tem que ser maior que 0")
                else: 
                    porcentagem_impostos = float (input("Informe o imposto da venda (em porcentagem): "))
                    if porcentagem_impostos <=0: 
                        print("Valor tem que ser maior que 0")
                    else:
                        porcentagem_rentabilidade = float(input("Informe o valor da rentabilidade do produto (em porcentagem): "))                                          
except ValueError:  
    print("O código do produto deve ser informado em números")


#transformando as porcentagens lidas nos respectivos valores (se o custo do produto fosse 100 por cento do valor mas o preço da venda que é)
valor_custo_fixo_compra  = (custo_produto/100) * porcentagem_custo_fixo
valor_comissao_compra = (custo_produto/100) * porcentagem_comissao
valor_impostos_compra = (custo_produto/100) * porcentagem_impostos
valor_rentabilidade_compra = (custo_produto/100) * porcentagem_rentabilidade

'''
#caso a margem de lucro viesse automaticamente
valor_margem_lucro = custo_produto - valor_custo_fixo - valor_comissao - valor_impostos
porcentagem_margem_lucro = (valor_margem_lucro/custo_produto) * 100
'''
print()

##valores desejados com relação ao preço de compra
print (f"O valor do custo fixo será (em relação ao preço de compra): {valor_custo_fixo_compra:.2f}")
print (f"O valor da comissão será (em relação ao preço de compra): {valor_comissao_compra:.2f}")
print (f"O valor dos impostos será (em relação ao preço de compra): {valor_impostos_compra:.2f}")
print (f"O valor de margem de lucro será (em relação ao preço de compra): {valor_rentabilidade_compra:.2f}")


#calculo do preço de venda
preco_venda = custo_produto / (1 - ((porcentagem_custo_fixo + porcentagem_comissao + porcentagem_impostos + porcentagem_rentabilidade)/(100)))
porcentagem_preco_venda = 100

print ()
print (f"PREÇO DE VENDA: {preco_venda:.2f}")

#criação do que faltava para tabela
valor_custo_aquisicao = custo_produto
porcentagem_custo_aquisicao = porcentagem_preco_venda - porcentagem_custo_fixo - porcentagem_comissao - porcentagem_impostos - porcentagem_rentabilidade

valor_receita_bruta = preco_venda - custo_produto
porcentagem_receita_bruta = porcentagem_preco_venda - porcentagem_custo_aquisicao

#transformando as porcentagens lidas nos respectivos valores
valor_custo_fixo = (preco_venda/100) * porcentagem_custo_fixo
valor_comissao = (preco_venda/100) * porcentagem_comissao
valor_impostos = (preco_venda/100) * porcentagem_impostos 


# "outros custos" é na verdade a soma do custo fixo, comissao e impostos
valor_outros_custos = valor_custo_fixo + valor_comissao + valor_impostos
porcentagem_outros_custos = porcentagem_custo_fixo + porcentagem_comissao + porcentagem_impostos

valor_rentabilidade = valor_receita_bruta - valor_outros_custos # ou valor_rentabilidade = (preco_venda/100) * porcentagem_rentabilidade

print()

#valores desejados com relação ao preço de venda
print (f"O valor do custo fixo será (em relação ao preço de venda): {valor_custo_fixo:.2f}")
print (f"O valor da comissão será (em relação ao preço de venda): {valor_comissao:.2f}")
print (f"O valor dos impostos será (em relação ao preço de venda): {valor_impostos:.2f}")
print (f"O valor de margem de lucro será (em relação ao preço de venda): {valor_rentabilidade:.2f}")


#visualização da tabela
print()
print(f"{'-'*25} | {'-'*10} | {'-'*5}") 
print (f"{'Descrição':^25} | {'Valor':^10} | {'%':^5}")
print(f"{'-'*25} | {'-'*10} | {'-'*5}")

print (f"{'A. Preço de Venda':<25} | {f'{preco_venda:.2f}':^10} | {f'{porcentagem_preco_venda}%':>5}")
print (f"{'B. Custo de Aquisição':<25} | {f'{valor_custo_aquisicao:.2f}':^10} | {f'{porcentagem_custo_aquisicao:.0f}%':>5}")
print (f"{'C. Receita Bruta (A-B)':<25} | {f'{valor_receita_bruta:.2f}':^10} | {f'{porcentagem_receita_bruta:.0f}%':>5}")
print (f"{'D. Custo Fixo':<25} | {f'{valor_custo_fixo:.2f}':^10} | {f'{porcentagem_custo_fixo:.0f}%':>5}")
print (f"{'E. Comissão de Vendas':<25} | {f'{valor_comissao:.2f}':^10} | {f'{porcentagem_comissao:.0f}%':>5}")
print (f"{'F. Impostos':<25} | {f'{valor_impostos:.2f}':^10} | {f'{porcentagem_impostos:.0f}%':>5}")
print (f"{'G. Outros custos (D+E+F)':<25} | {f'{valor_outros_custos:.2f}':^10} | {f'{porcentagem_outros_custos:.0f}%':>5}")
print (f"{'H. Rentabilidade (C-G)':<25} | {f'{valor_rentabilidade:.2f}':^10} | {f'{porcentagem_rentabilidade:.0f}%':>5}")

print()

#imprimindo faixa de lucro com suas respectivas cores
#"\033[32m" +: exemplo de mudar de cor para verde & + "\033[0m": volta para cor padrão
print ("CLASSIFICAÇÃO DE LUCRO: ") 
if porcentagem_rentabilidade>20:
    print("\033[34m" + "Lucro Alto" + "\033[0m") #azul
elif porcentagem_rentabilidade >10 and porcentagem_rentabilidade<=20:
    print("\033[32m" + "Lucro Médio" + "\033[0m") #verde
elif porcentagem_rentabilidade >0 and porcentagem_rentabilidade<=10:
    print("\033[33m" + "Lucro Baixo" + "\033[0m") #amarelo
elif porcentagem_rentabilidade == 0:
    print("Equilíbrio")
else:
    print("\033[31m" + "Prejuízo" + "\033[0m") #vermelho

print ()

print ("PROGRAMA FINALIZADO")