a = list(map(int, input().split()))
len_a = len(a)
sem_repetidos = set(a)
len_b = len(sem_repetidos)

if len_b < len_a:
    print(True)
else:
    print(False)