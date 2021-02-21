def fibonacci(n):
    a = 0
    b = 1
    print(f'{a} {b} ', end='')
    num = 3
    while num <= n:
        c = a + b
        print(f'{c} ',end='')
        a = b
        b = c
        num += 1

fibonacci(10)