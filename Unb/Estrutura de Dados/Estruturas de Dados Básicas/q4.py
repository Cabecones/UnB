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


d_tipo = Deque()
d_cor = Deque()
minutos = []

qntd_entradas = int(input())
lista = []

for i in range(qntd_entradas):
    lista.append(input())

for i in lista:
    tipo = i.split()[0]
    cor = i.split()[1]
    minutes = int(i.split()[2])

    d_tipo.add_front(tipo)
    d_cor.add_front(cor)
    minutos.append(minutes)

for i in range(qntd_entradas):
    print(f'Tipo: {d_tipo.remove_front()}, Cor: {d_cor.remove_front()}')

print(f'Total de roupas: {qntd_entradas}')
print(f'Total de tempo: {sum(minutos)}')
