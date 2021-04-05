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
    horas, mbinario, columindice, alfabeto, quantidade_posicoes, missoes_cifradas = int(input()), int(input()), int(input()), input(), int(input()), int(input())

    d = Deque()
    missoes = []
    adicionar_alfabeto(d, alfabeto)

    for i in range(missoes_cifradas):
        missao = input()
        missao_limpa = missao[1:len(missao) - 1]
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

    desconhecido, atividades = [atividade[2] for atividade in missoes], [atividade[1] for atividade in missoes]

    def mochila(missoes_cifradas, desconhecido, atividades, horas):
        if erva_santa_maria[missoes_cifradas][horas] == - 1:
            if int(atividades[missoes_cifradas - 1]) > horas:
                erva_santa_maria[missoes_cifradas][horas] = mochila(missoes_cifradas - 1, desconhecido, atividades, horas)
            else:
                use = int(desconhecido[missoes_cifradas - 1]) + mochila(missoes_cifradas - 1, desconhecido, atividades, horas - int(atividades[missoes_cifradas - 1]))
                naouse = mochila(missoes_cifradas - 1, desconhecido, atividades, horas)
                erva_santa_maria[missoes_cifradas][horas] = max(use, naouse)
        return erva_santa_maria[missoes_cifradas][horas]

    def solucao(erva, missoes, horas):
        solucao = []
        for i in range(len(erva) - 1, 0, -1):
            if erva[i][horas] == erva[i - 1][horas - int(missoes[i - 1][1])] + int(missoes[i - 1][2]):
                solucao.append(missoes[i - 1])
                horas -= int(solucao[-1][1])
        return solucao

    def impressora(S, horas, columindice, mbinario):
        tempo_restante= horas - sum([int(missao[1]) for missao in S])
        valor = sum([int(missao[2]) for missao in S])
        S = [[str(num) for num in missao] for missao in S]
        algum_num = [algum for algum in range(4) if algum != columindice]
        S = sorted(S, key=lambda x: (x[columindice], x[algum_num[0]], x[algum_num[1]], x[algum_num[2]]))
        if mbinario: [print(', '.join(missao)) for missao in S]
        print(f'Tempo restante: {tempo_restante}')
        print(f'Valor: {valor}')

    mochila(missoes_cifradas, desconhecido, atividades, horas)
    solussao = solucao(erva_santa_maria, missoes, horas)
    impressora(solussao, horas, columindice, mbinario)

