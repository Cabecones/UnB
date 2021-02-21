contacao_dolar = float(input())
tam_lote = int(input())
qtd_lote = int(input())
f = float(tam_lote)
taxa = (tam_lote*contacao_dolar)*(2.5/100)
i = 0
num_lote = 1

while i < qtd_lote:
    lote = contacao_dolar*tam_lote+taxa
    print(f'Lote: {num_lote} - Total da venda: R$ {lote:.2f}')
    num_lote += 1
    i += 1
