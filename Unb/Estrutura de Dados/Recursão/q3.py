def mdc(a, b):
    while b != 0:
        resto = a % b
        a = b
        b = resto

    return a


n1, n2 = input().split()
n1 = int(n1)
n2 = int(n2)

print(mdc(n1, n2))
