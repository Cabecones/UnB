n = int(input())
m = int(input())
figurinhas = list()

for i in range(0, m):
    figurinhas.append(input())

repetidas = len(set(figurinhas))

restante = n - repetidas

print(restante)
