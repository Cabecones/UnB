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

def exibe_candidatos(deque, pos, ordem):
    if ordem == "direta" and deque.is_empty() != True:
        for i in range(pos):
            deque.remove_front()
        for j in range(deque.size()):
            print(deque.remove_front())
    elif ordem == "inversa" and deque.is_empty() != True:
        for i in range(deque.size() - pos - 1):
            deque.remove_rear()
        for j in range(deque.size()):
            print(deque.remove_rear())

deque.add_rear('Obi-Wan Kenobi')
deque.add_rear('Leia Skywalker')
deque.add_rear('Chewbacca')
deque.add_rear('Boba Fett')
deque.add_rear('Yoda')
deque.add_rear('Anakin Skywalker')
deque.add_rear('Darth Vader')
deque.add_rear('Ben Solo')
deque.add_rear('Kylo Ren')
deque.add_rear('Luke Skywalker')
deque.add_rear('Leia Organa')
deque.add_rear('R2-D2')
deque.add_rear('C-3PO')
deque.add_rear('BB-8')
deque.add_rear('Han Solo')
deque.add_rear('Padmé Amidala')
deque.add_rear('Mace Windu')
deque.add_rear('Qui-Gon Jinn')
deque.add_rear('Vice Almirante Holdo')
deque.add_rear('Rose Tico')
deque.add_rear('Poe Dameron')
deque.add_rear('Lando Calrissian')
deque.add_rear('Darth Maul')
deque.add_rear('Red Boba Fett')
deque.add_rear('Jabba, the Hutt')
deque.add_rear('Jango Fett')
deque.add_rear('Conde Dooku')
deque.add_rear('Darth Tyranus')
deque.add_rear('General Grievous')
deque.add_rear('Sheev Palpatine')
deque.add_rear('Darth Sidious')
deque.add_rear('Finn')
deque.add_rear('Maz Kanata')
deque.add_rear('Rey Palpatine')
deque.add_rear('Rey Skywalker')
deque.add_rear('Ben Solo')
deque.add_rear('Kylo Ren')
deque.add_rear('Líder Supremo Snoke')
exibe_candidatos( deque, 2, 'inversa' )