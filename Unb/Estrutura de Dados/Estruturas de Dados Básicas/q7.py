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

deque = Deque()
lista = []

lista.append(input().split())

for i in lista[0]:
    deque.add_front(i)

fila = int(input())

for i in range(fila):
    deque.add_front(deque.remove_rear())

print(f'Pessoa da frente: {deque.remove_rear()}')
print(f'Pessoa do fim: {deque.remove_front()}')
