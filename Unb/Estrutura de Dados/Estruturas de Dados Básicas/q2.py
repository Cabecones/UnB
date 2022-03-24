class Deque:
    def __init__(self):
        self.__items = []

    def is_empty(self):
        return self.__items == []

    def F(self, item):
        self.__items.append(item)

    def I(self, item):
        self.__items.insert(0, item)

    def D(self):
        return self.__items.pop(0)

    def P(self):
        return self.__items.pop()

    def size(self):
        return len(self.__items)

deque = Deque()

list = []
a = ''

while a != "X":
    a = input()
    list.append(a)

for i in list:
    if len(i) != 1:
        comando = i.split()[0]
        numero = i.split()[1]
        if comando == 'I':
            deque.I(numero)
        elif comando == 'F':
            deque.F(numero)

    else:
        comando = i
        if comando == 'P':
            print(deque.P())
        elif comando == 'D':
            print(deque.D())

for j in range(deque.size()):
    print(deque.D())



