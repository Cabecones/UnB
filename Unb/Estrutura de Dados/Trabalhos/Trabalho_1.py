class Deque:
    def __init__(self):
        self.__items = []

    def is_empty(self):
        return self.__items == []

    def add_front(self, item):
        self.__items.append(item)

    def add_rear(self, item):
        self.__items.insert(0, item)

    def remove_rear(self):
        return self.__items.pop(0)

    def remove_front(self):
        return self.__items.pop()

    def size(self):
        return len(self.__items)

    def __str__(self):
        sdeque = ''
        for i in self.__items:
            sdeque += i
        return sdeque

d = Deque()
texto_cifrado = 'ECUC'

def adicionar_alfabeto(deque, alfabeto):
    for char in alfabeto:
        deque.add_front(char)
def decifrar(deque, texto_cifrado, chave):
    texto_plano = ''
    for char in texto_cifrado:
        aux = ''
        temporario = 0
        while aux != char:
            aux = deque.remove_front()
            deque.add_rear(aux)
        while temporario <= chave - 1:
            aux = deque.remove_front()
            deque.add_rear(aux)
            temporario += 1
        texto_plano += aux
    return texto_plano


def selecionar_subconjunto_missoes():
    horas, mbinario, columindice, alfabeto, quantidade_posicoes, missoes_cifradas = int(input()), int(input()), int(input()), int(input()), int(input()), int(input())

    missoes = []

    for i in range(missoes_cifradas):
        missao = input()
        missao_limpa = i[1:len(i) - 1]
        missao = decifrar(d, missao_limpa, quantidade_posicoes)
        missoes.append(missao.split(','))

    erva_santa_maria = []

    for i in range(missoes_cifradas + 1):
        erva_santa_maria.append([])
        for j in range(horas + 1):
            if i == 0 or j == 0:
                erva_santa_maria[i].append(0)
            else:
                erva_santa_maria[i].append(-1)

    def mochila():
        if M[missoes_cifradas][horas] == -1:
            if W[missoes_cifradas] > horas:
                M[missoes_cifradas][horas] = mochila(missoes_cifradas - 1, v, w, horas)
            else:
                use = v[missoes_cifradas] + mochila(missoes_cifradas - 1, v, w, horas - w[missoes_cifradas])
                naouse = mochila(missoes_cifradas - 1, v, w, horas)
                M[missoes_cifradas][horas] = max{use, naouse}