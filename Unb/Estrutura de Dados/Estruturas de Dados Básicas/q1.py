class Stack:
    def __init__(self):
        self.items = list()

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

s = Stack()


for letra in input():
    if letra != "*":
        s.push(letra)
    else:
       print(s.pop(), end="")
