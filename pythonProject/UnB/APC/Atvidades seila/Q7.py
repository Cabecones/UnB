def mdc(a,b):
    while b != 0:
        resto = a % b
        a = b
        b = resto

    return a

print(mdc(105,60))