n = int(input())
lista = []
ordenado = sorted(lista)
divisoes = []

for i in range(n):
    a, b = map(int, input().split())
    divisao = int(b/a)
    divisoes.append(divisao)
    j = f'{divisao:.0f} / {a}'
    lista.append(j)

print(lista)