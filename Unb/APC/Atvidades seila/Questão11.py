def sonho():
    n = int(input('Digite o numero'))
    resto = n%2
    zero = 1
    while resto != 0:
        zero = zero + 1
        print(zero+1)
        zero = zero
        if resto == 0:
            return zero

sonho()
