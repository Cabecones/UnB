SS = []
MS = []
MM = []
MI = []
II = []
SR = []

notas = []
nomes = []
sobrenomes = []
num = []


n = int(input())

for i in range(n):
    a, b, c = input().split()
    notas.append(a)
    nomes.append(b)
    sobrenomes.append(c)
    if 'SS' == a:
        num.append(10)
    elif 'MS' == a:
        num.append(8)
    elif 'MM' == a:
        num.append(6)
    elif 'MI' == a:
        num.append(4)
    elif 'II' == a:
        num.append(2)
    elif 'SR' == a:
        num.append(0)

alunos = list(zip(notas, nomes, sobrenomes, num))

alunos.sort(key=lambda x: x[3])
alunos.sort(reverse=True)
notas, nomes, sobrenomes, num = zip(*alunos)

alunos_ordenado = list(zip(notas, nomes, sobrenomes))

for i in alunos_ordenado:
    if 'SS' in i:
        SS.append(i)
    elif 'MS' in i:
        MS.append(i)
    elif 'MM' in i:
        MM.append(i)
    elif 'MI' in i:
        MI.append(i)
    elif 'II' in i:
        II.append(i)
    elif 'SR' in i:
        SR.append(i)

#for i in range(len(SS)):
    #contador = SS.count()
SS.sort(key=lambda x: x[2])
MS.sort(key=lambda x: x[2])
MM.sort(key=lambda x: x[2])
MI.sort(key=lambda x: x[2])
II.sort(key=lambda x: x[2])
SR.sort(key=lambda x: x[2])

SS.sort(key=lambda x: x[1])
MS.sort(key=lambda x: x[1])
MM.sort(key=lambda x: x[1])
MI.sort(key=lambda x: x[1])
II.sort(key=lambda x: x[1])
SR.sort(key=lambda x: x[1])

print(MI)

for i in SS:
    print(f'{i[0]} {i[1]} {i[2]}')
for i in MS:
    print(f'{i[0]} {i[1]} {i[2]}')
for i in MM:
    print(f'{i[0]} {i[1]} {i[2]}')
for i in MI:
    print(f'{i[0]} {i[1]} {i[2]}')
for i in II:
    print(f'{i[0]} {i[1]} {i[2]}')
for i in SR:
    print(f'{i[0]} {i[1]} {i[2]}')