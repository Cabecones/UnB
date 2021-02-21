abrir = open('teste2.csv', 'r')

itens = list(abrir.read().split())
for frase in itens:
    print(frase.replace(',', ';'))
