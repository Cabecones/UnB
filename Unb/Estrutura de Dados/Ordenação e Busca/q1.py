while True:
    nome = []
    decimal = []
    n = int(input())
    for i in range(n):
        a, b, c = input().split()
        nome.append(a)
        decimal.append(c)

    ordem = list(zip(nome, decimal))
    ordem.sort(key=lambda x: x[1])


    for j in range(n):
        if j < len(ordem)-1:
            print(f'{ordem[j][0]} <', end=' ')
        else:
            print(f'{ordem[j][0]}')

    if n == 0:
        break


ordem = list(zip(nome, decimal))

ordem.sort(key=lambda x: x[1])


