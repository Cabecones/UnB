import os

imput = input().split()
try:
    tentar = open(os.path.abspath(imput[-1]), 'r')
    print('da pra abrir')
    tupla = tentar.read().split()
    num = []
    lens = int(len(tupla) / 2)
    num_int = []
    zero = 0
    for i in range(lens):
        num.append(sorted(tupla)[i])
    num_int.append(sorted(list(map(int, num)), reverse=True))
    for item in num_int[0]:
        nome = tupla[tupla.index(f'{item}') - 1]
        nume = tupla[tupla.index(f'{item}')]
        print(f"('{nome}', {nume})")
except:
    print('nao da pra abrir')