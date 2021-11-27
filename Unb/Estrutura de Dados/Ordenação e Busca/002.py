n = int(input())
lista = []

for i in range(n):
    entradas = float(input())
    lista.append(entradas)
    ordem = lista.sort(reverse=True)

for j in lista:
    print(f'{j:.2f}')

print(lista)