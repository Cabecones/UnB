def imprimeTermos (n):
    n = -n
    while n <= 0:
        print(n)
        n = n+2
        if n == -1:
            print(-1)
            n = n+1

imprimeTermos(635)