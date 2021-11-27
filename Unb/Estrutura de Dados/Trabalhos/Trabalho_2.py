class No:
    def __init__(self, key, dir, esq):
        self.root = key
        self.dir = dir
        self.esq = esq

class Tree:
    def __init__(self):
        self.root = No(None, None, None)
        self.root = None

    def inserir(self, v, r):
        novo = No(v, None, None)  # cria um novo Nó
        if self.root == None:
            self.root = novo
        else:  # se nao for a raiz
            atual = self.root
        while True:
            anterior = atual
            if r == ".":  # ir para esquerda
                atual = atual.esq
                if atual == None:
                    anterior.esq = novo
                    return
            # fim da condição ir a esquerda
            else:  # ir para direita
                atual = atual.dir
                if atual == None:
                    anterior.dir = novo
                    return
                # fim da condição ir a direita

    def buscar(self, chave):
        if self.root == None:
            return None  # se arvore vazia
        atual = self.root  # começa a procurar desde raiz
        while atual.item != chave:  # enquanto nao encontrou
            if chave < atual.item:
                atual = atual.esq  # caminha para esquerda
            else:
                atual = atual.dir  # caminha para direita
            if atual == None:
                return None  # encontrou uma folha -> sai
        return atual  # terminou o laço while e chegou aqui é pq encontrou item

entradas = []

arv = Tree()

entrada = int(input())

for i in range(entrada):
    entradas.append(input().split())

print(entradas)

for j in entradas:
    arv.inserir(j[0], j[1])

print(arv)
