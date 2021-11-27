m = int(input())

def fibonacci(n):
    if n == 0:
        fibonacci_list = []
    elif n == 1:
        fibonacci_list = [0]
    elif n == 2:
        fibonacci_list = [0, 1]
    elif n > 2:
        fibonacci_list = [0, 1]
        for i in range(n-2):
            fibonacci_list += [0]
            fibonacci_list[-1] = fibonacci_list[-2] + fibonacci_list[-3]
    return fibonacci_list

fibonaoti = []

for i in range(1, 10000):
    if i not in fibonacci(1000):
        fibonaoti.append(i)
    if len(fibonaoti) >= m:
        break

print(*fibonaoti, sep=', ')