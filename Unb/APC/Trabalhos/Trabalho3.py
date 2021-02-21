arquivo = open(input(), 'r')
linhas = arquivo.readlines()
seila = []
for linha in linhas:
    if '#' in linha:
        seila.append(linha.split('#')[0].split())
    else:
        seila.append(linha.split())
resultadinho = []
for linhasinha in seila:
    for coisinha in linhasinha:
        resultadinho.append(coisinha)
seila_num = 0
if resultadinho[0] == 'P1':
    for coisinha in resultadinho[3:]:
        seila_num += coisinha.count('1')
elif resultadinho[0] == 'P2':
    for coisinha in resultadinho[4:]:
        if int(coisinha) > int(resultadinho[3]) / 2:
            seila_num += 1
elif resultadinho[0] == 'P3':
    for i in range(4, len(resultadinho)-2, 3):
        if ((int(resultadinho[i]) + int(resultadinho[i+1]) + int(resultadinho[i+2]))/3) > (int(resultadinho[3]) / 2):
            seila_num += 1
print(seila_num)