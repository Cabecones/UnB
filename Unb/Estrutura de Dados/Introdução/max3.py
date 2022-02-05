def max3(a, b, c):
    lista = []
    lista.append(a)
    lista.append(b)
    lista.append(c)
    ordenada = sorted(lista)
    return ordenada[2]

print(max3(3, 2, 1))