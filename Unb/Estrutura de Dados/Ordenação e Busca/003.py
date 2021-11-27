n = int(input())

lista = []

lista = input().split()

repeats = []
not_repeats = []

for i in lista:
    if i not in not_repeats:
        not_repeats.append(i)
    else:
        repeats.append(i)

print(len(repeats))

