def ehPrimo(numero):
    divisores = 0
    for divisor in range(1, numero):
        if numero % divisor == 0:
            divisores = divisores + 1
            if divisores > 1:
                break
    if divisores > 1:
        return 0
    else:
        return 1

def divisoresPrimos(a):
    divisores = []
    if a%2 == 0:
        divisores.append(1)
    if a%3 == 0:
        divisores.append(1)
    if a%5 == 0:
        divisores.append(1)
    if a%7 == 0:
        divisores.append(1)
    if a%11 == 0:
        divisores.append(1)
    if a%13 == 0:
        divisores.append(1)
    return sum(divisores)


