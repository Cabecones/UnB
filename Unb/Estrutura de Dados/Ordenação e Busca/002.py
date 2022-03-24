n = int(input())
lista = []

for i in range(n):
    entradas = float(input())
    lista.append(entradas)
    ordem = lista.sort(reverse=True)

#for j in lista:
 #   print(f'{j:.2f}')


def median(x):
    half = len(x) // 2
    x.sort()
    if not len(x) % 2:
        return (x[half - 1] + x[half]) / 2.0
    return x[half]

def pior_nota(x):
    ordenada = sorted(x)
    return ordenada[0]

def melhor_nota(x):
    ordenada = sorted(x, reverse=True)
    return ordenada[0]


print(f'{pior_nota(lista):.2f}')
print(f'{median(lista):.2f}')
print(f'{melhor_nota(lista):.2f}')