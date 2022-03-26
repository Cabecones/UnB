import itertools
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

deque = Deque()
'''''
while True:
    deque1 = Deque()
    entrada = input()
    if entrada == 'halt':
        break
    else:
        if entrada != 'process' and 'halt':
            comando, n = entrada.split()
            for i in range(int(n)):
                a = input()
                deque1.add_rear(a)
                #fazer tudo aqui antes de ir para outra fila
        elif entrada == 'process':
            print(deque.remove_front())
    deque.add_rear(deque1)
'''''

def deyodafy():
    frase = list(input().split())
    frase.remove('deYodafy') #retirar o yodafy na função de cima, pois ele será um comando

    for palavra in frase:
        points = '!@#$.'
        for char in palavra:
            if char in points:
                frase.append(palavra.replace(char, ''))
                frase.remove(palavra)
                frase.insert(0, frase[0].replace(frase[0], frase[0]+char))
                frase.remove(frase[1])
                frase = frase[::-1]

    for palavra in frase:
        print(palavra, end=' ')

#cordenada = input().split()
#print(cordenada)

inp_list = [1, 2, 3, 4]
permutations = list(itertools.permutations(inp_list))

crypt = ['-', '-', '-']

for combi in permutations:
    condition = 0
    num = 0
    for sin in crypt:
        num_ant = combi[num]
        if sin == '-':
            if num_ant > combi[num + 1]:
                condition = 1
                num += 1
            else:
                condition = 0
                break
        elif sin == '+':
            if num_ant < combi[num + 1]:
                condition = 1
                num += 1
            else:
                condition = 0
                break
    if condition == 1:
        for i in combi:
            print(i, end='')
        break




