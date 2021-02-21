def is_imperfect(n):
    soma = 0
    for divisor in range(1, n):
        if n % divisor == 0:
            soma += divisor

    if n == soma:
        return 'True'
    else:
        return 'False'


print(is_imperfect(6))
