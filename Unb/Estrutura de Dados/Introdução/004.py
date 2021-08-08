import math

linhas = int(input())
codigos = []
for i in range(linhas+2):
    codigo = input().split()
    codigos.append(codigo)

new = [[float(j) for j in i] for i in codigos]

coelho = new[0]
raposa = new[1]
del(new[0:2])
win = []
lose = []
buraco_certo = []

for i in new:
    buraco = i
    foge = math.dist(coelho, buraco)
    not_foge = math.dist(raposa, buraco)/2
    if foge < not_foge:
        win.append(buraco)
        buraco_certo.append(i)
    else:
        lose.append(buraco)

if len(win) == 0:
    print('O coelho nao pode escapar.')
else:
    print(f'O coelho pode escapar pelo buraco ({buraco_certo[0][0]:.3f}, {buraco_certo[0][1]:.3f}).')