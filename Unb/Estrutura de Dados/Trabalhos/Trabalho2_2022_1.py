class No:

    def __init__(self, key, parent):
        self.root = None
        self.item = key
        self.children = []
        self.parent = parent

    def mkdir(self, path):
        if path.length == 0:
            return
        nome = path.pop(0)
        for child in self.children:
            if child.item == nome:
                if path.length == 0:
                    return print('DIRETÓRIO JÁ EXISTE')
                return child.mkdir(path)
        novo = No(nome, self)
        self.children.append(novo)
        novo.mkdir(path)

    def touch(self, path):
        if path.length == 0:
            return
        if path.length == 1:
            nome1 = path.pop(0)
            for child in self.children:
                if child.item == nome1:
                    print('ARQUIVO JÁ EXISTE')
                    break
        nome = path.pop(0)
        for child in self.children:
            if child.item != nome:
                print('CAMINHO INVÁLIDO')
                break

    def rm(self, path):
        if path.length == 0:
            return
        path = list(reversed(path))
        nome = path.pop(0)
        i = 1
        for child in self.children:
            if child.item == nome:
                child.item = None
                i = 0
        if i == 1:
            print('CAMINHO INVÁLIDO')
        #ADICIONAR ISSO (Se o diretório corrente for removido (pwd), o novo diretório corrente será o "/".)

    def find(self, path):
        if self.root == None:
            return None  # se arvore vazia
        atual = self.root  # começa a procurar desde o pwd
        while atual.item != path:  # enquanto nao encontrou
            if atual == None:
                return None  # encontrou uma folha -> sai
        return atual  # terminou o laço while e chegou aqui é pq encontrou item

def cd(caminho):
    curent = caminho
    return

def ponto(curent):
    return curent

while True:
    curent = '/'
    entrada = input()
    if entrada == 'end':
        break
    if entrada != 'show' and entrada != 'pwd':
        if 'mv' in entrada:
            comando, origem, destino = entrada.split()
            print(comando, origem, destino)
        elif 'cd' in entrada:
            comando, caminho = entrada.split()
            print(caminho)
        else:
            comando, caminho = entrada.split()
            caminho = caminho.split('/')
            caminho = list(filter(None, caminho))
            print(caminho)