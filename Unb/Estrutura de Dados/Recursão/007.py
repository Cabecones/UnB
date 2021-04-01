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

print(fibonacci(10))