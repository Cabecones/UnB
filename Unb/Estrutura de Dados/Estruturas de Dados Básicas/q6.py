produto = []
preco = []
dicionario = {}
ordenado = {}

while produto != 'fim':
    if len(produto) > 3:
        produto, preco = input().split()
    print(produto)

print(produto, preco)

for i, j in zip(produto, preco):
    dicionario[i] = j

for i in sorted(dicionario, key=dicionario.get):
    ordenado[dicionario[i]] = i

print(ordenado)



