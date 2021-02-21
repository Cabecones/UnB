import math

def inverter_matriz(xtrain):
    new_Xtrain = []
    for i in range(22):
        atributo = []
        for j in range(len(xtrain)):
            atributo.append(xtrain[j][i])
        new_Xtrain.append(atributo)
    return new_Xtrain


def desvio_padrao(newtrain):
    resultado_desvio = []
    for caracteristica in newtrain:
        media = sum(caracteristica) / len(caracteristica)
        media_list = []
        media_list.append(media)
        soma = 0
        for item in caracteristica:
            soma += (item - media) ** 2
        desvio = math.sqrt(soma / len(caracteristica))
        media_list.append(desvio)
        resultado_desvio.append(media_list)
    return resultado_desvio


def passo_7(xtrain, desvio):
    for i in range(len(xtrain)):
        for j in range(22):
            if desvio[j][1] != 0:
                xtrain[i][j] = (xtrain[i][j] - desvio[j][0]) / desvio[j][1]
            else:
                xtrain[i][j] = 0
    return xtrain


def dis_euclidiana(xtrain, xtest, ytrain, k):
    for vetor_xtest in xtest:
        distancia = []
        for vetor_xtrain in xtrain:
            soma = 0
            for i in range(22):
                soma += (math.pow(vetor_xtest[i] - vetor_xtrain[i], 2))
            distancia.append(math.sqrt(soma))
        temp = sorted([[distancia[i], ytrain[i]]for i in range(len(distancia))], key=lambda x: x[0])[:k]
        troca = {'p': 1, 'e': 0}
        temp = sum([troca[kermit[1]] for kermit in temp])
        if temp > k/2:
            print('p')
        else:
            print('e')



k = int(input())
Ntrain, Ntest = map(int, input().split())
Xtrain = []
for i in range(Ntrain):
    Xtrain.append(input().split())
Ytrain = []
for j in range(Ntrain):
    Ytrain.append(input())
Xtest = []
for l in range(Ntest):
    Xtest.append(input().split())


atributos = [{'b': 0, 'c': 1, 'x': 2, 'f': 3, 'k': 4, 's': 5},
             {'f': 0, 'g': 1, 'y': 2, 's': 3},
             {'n': 0, 'b': 1, 'c': 2, 'g': 3, 'r': 4, 'p': 5, 'u': 6, 'e': 7, 'w': 8, 'y': 9},
             {'t': 0, 'f': 1},
             {'a': 0, 'l': 1, 'c': 2, 'y': 3, 'f': 4, 'm': 5, 'n': 6, 'p': 7, 's': 8},
             {'a': 0, 'd': 1, 'f': 2, 'n': 3},
             {'c': 0, 'w': 1, 'd': 2},
             {'b': 0, 'n': 1},
             {'k': 0, 'n': 1, 'b': 2, 'h': 3, 'g': 4, 'r': 5, 'o': 6, 'p': 7, 'u': 8, 'e': 9, 'w': 10, 'y': 11},
             {'e': 0, 't': 1},
             {'b': 0, 'c': 1, 'u': 2, 'e': 3, 'z': 4, 'r': 5, '?': 6},
             {'f': 0, 'y': 1, 'k': 2, 's': 3},
             {'f': 0, 'y': 1, 'k': 2, 's': 3},
             {'n': 0, 'b': 1, 'c': 2, 'g': 3, 'o': 4, 'p': 5, 'e': 6, 'w': 7, 'y': 8},
             {'n': 0, 'b': 1, 'c': 2, 'g': 3, 'o': 4, 'p': 5, 'e': 6, 'w': 7, 'y': 8},
             {'p': 0, 'u': 1},
             {'n': 0, 'o': 1, 'w': 2, 'y': 3},
             {'n': 0, 'o': 1, 't': 2},
             {'c': 0, 'e': 1, 'f': 2, 'l': 3, 'n': 4, 'p': 5, 's': 6, 'z': 7},
             {'k': 0, 'n': 1, 'b': 2, 'h': 3, 'r': 4, 'o': 5, 'u': 6, 'w': 7, 'y': 8},
             {'a': 0, 'c': 1, 'n': 2, 's': 3, 'v': 4, 'y': 5},
             {'g': 0, 'l': 1, 'm': 2, 'p': 3, 'u': 4, 'w': 5, 'd': 6}]


for i in range(Ntrain):
    for j in range(22):
        Xtrain[i][j] = atributos[j][Xtrain[i][j]]
for i in range(Ntest):
    for j in range(22):
        Xtest[i][j] = atributos[j][Xtest[i][j]]

disviu = desvio_padrao(inverter_matriz(Xtrain))
Xtrem, Xtesti = passo_7(Xtrain, disviu), passo_7(Xtest, disviu)

dis_euclidiana(Xtrem, Xtesti, Ytrain, k)
