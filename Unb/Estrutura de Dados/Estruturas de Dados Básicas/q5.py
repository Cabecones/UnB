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

itens = []
atividade = []
prioridade = []
dicionario = {}
ordenado = {}
ordenado2 = {}
value1 = {}
value2 = {}

itens.append(input().split())
feitos = int(input())

for i in itens[0]:
    if i == '1' or i == '2' or i == '3' or i == '4' or i == '5' or i == '6' or i == '7' or i == '8' or i == '9' or i == '10':
        prioridade.append(i)
    else:
        atividade.append(i)

j = 0

for i in range(len(atividade)):
    dicionario[atividade[j]] = prioridade[j]
    j += 1

for i in sorted(dicionario, key=dicionario.get):
    value2[dicionario[i]] = i

for i in sorted(dicionario, key=dicionario.get):
    ordenado2[i] = dicionario[i]

for i in sorted(dicionario, key=dicionario.get):
    ordenado[i] = dicionario[i]
    value1[dicionario[i]] = i

for i, j in zip(ordenado2, range(feitos)):
    del ordenado[i]

for i, j in zip(value2, range(feitos)):
    del value1[f'{i}']

print(f'Tamanho da fila: {len(value1)}')

for i, j in zip(value1, ordenado):
    print(f'Atividade: {value1[i]}, Prioridade: #{ordenado[j]}')