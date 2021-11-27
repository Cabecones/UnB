def add(lista, musica):
    lista.append(musica)
    return


def nextMusic(lista, musica, indice):
    if musica != lista[0] and musica in lista:
        indice.append(lista.index(musica))
        lista.remove(musica)
        if play == True:
            lista.insert(1, musica)
        else:
            lista.insert(0, musica)
    return


def delMusic(lista, musica, indice, play):
    if musica in lista:
        indice.append(lista.index(musica))
        lista.remove(musica)
    return


def listMusic(lista):
    if lista != []:
        print(','.join(lista))
    else:
        print('[vazia]')
    return


def current(lista, indice):
    if len(lista) > 0:
        return fila[indice]
    else:
        return 'Toque! Toque, Dijê!'


def undo(dic, funcao, lista, indice):
    if funcao == "add":
        lista.pop()
    elif funcao == "play":
        play = False
    elif funcao == "del":
        lista.insert(indice[-1], dic[funcao][-1])
        dic[funcao].pop()
    elif funcao == "next":
        musica = lista.pop(1)
        lista.insert(indice[-1], musica)
    return


# codigo principal

fila = []
dic = {'del': [], 'next': [], 'play': []}
funcoes = []
indexDel = []
indexNext = []
atual = 0
play = False

entrada = input()

while entrada != "fight":

    if " " in entrada and "*" not in entrada:
        funcao, musica = entrada.split()
    else:
        funcao = entrada

    # chamando function
    if funcao == "add":
        add(fila, musica)
        funcoes.append(funcao)

    if funcao == "list":
        listMusic(fila)

    if funcao == "current":
        print(current(fila, atual))

    if funcao == "del":
        if musica in fila:
            if not (play == True and fila.index(current(fila, atual)) == fila.index(musica)):
                delMusic(fila, musica, indexDel, play)
                dic[funcao].append(musica)
                funcoes.append(funcao)

                if atual >= len(fila):
                    atual = 0

    if funcao == "play":
        play = True
        dic[funcao].append(True)
        funcoes.append(funcao)

    if funcao == "next" and fila != []:
        nextMusic(fila, musica, indexNext)
        dic[funcao].append(musica)
        funcoes.append(funcao)

    if funcao == "ended":
        if play == True:
            if len(fila) - 1 != atual:
                atual += 1
            else:
                atual = 0
            dic = {'del': [], 'next': [], 'play': []}
            indexDel = []
            indexNext = []
            funcoes = []

    if funcao == "stop":
        play = False

    if funcao == "undo" and funcoes != []:
        if funcoes[-1] == "del":
            undo(dic, funcoes[-1], fila, indexDel)
            if indexDel[-1] <= atual and play == True:
                atual += 1
        elif funcoes[-1] == "next":
            undo(dic, funcoes[-1], fila, indexNext)
            if indexNext[-1] <= atual and play == True:
                atual += 1
        else:
            undo(dic, funcoes[-1], fila, indexDel)
        funcoes.pop()

    if funcao == "undo *":
        while (funcoes != []):
            if funcoes[-1] == "del":
                undo(dic, funcoes[-1], fila, indexDel)
                if indexDel[-1] <= atual and play == True:
                    atual += 1
            elif funcoes[-1] == "next":
                undo(dic, funcoes[-1], fila, indexNext)
                if indexNext[-1] <= atual and play == True:
                    atual += 1
            else:
                undo(dic, funcoes[-1], fila, indexDel)

            funcoes.pop()

    entrada = input()

print('Jedi Wagner, assuma o comando!')