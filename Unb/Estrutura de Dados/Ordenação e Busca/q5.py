n = int(input())
pretendentes = []
tamanho_repetidos = []
tamanho = []

for i in range(n):
    pretendentes.append(input())

for i in pretendentes:
    tamanho_repetidos.append(len(i))

for i in tamanho_repetidos:
    if tamanho_repetidos.count(i) == 1:
        tamanho.append(i)


if len(tamanho) > 0:
    index = tamanho_repetidos.index(max(tamanho))
    print(pretendentes[index])
else:
    print('Que mala suerte!')