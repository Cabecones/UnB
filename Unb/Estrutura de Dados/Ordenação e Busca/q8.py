nome = []
sobrenome = []
altura = []
peso = []


n = int(input())

for i in range(n):
    a, b, c, d = input().split()
    nome.append(a)
    sobrenome.append(b)
    altura.append(abs(int(c)-180))
    peso.append(abs(int(d)-75))

pretendentes = list(zip(nome, sobrenome, altura, peso))
pretendentes.sort(key=lambda x: x[1])
pretendentes.sort(key=lambda x: x[0])
pretendentes.sort(key=lambda x: x[2])
pretendentes.sort(key=lambda x: x[3])
print(pretendentes)

for i in pretendentes:
    print(f'{i[1]}, {i[0]}')

