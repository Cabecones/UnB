class No:

    def __init__(self, key, parent):
        self.root = None
        self.item = key
        self.children = []
        self.parent = parent

    def show(self, level=0):
        print(f'{"---" * level}{self.item}')
        for child in sorted(self.children, key=lambda x: x.item):
            child.show(level + 1)

    def mkdir(self, path):
        if len(path) == 0:
            return
        if '/' in path:
            return print('DIRETÓRIO JÁ EXISTE')
        nome = path.pop(0)
        for child in self.children:
            if child.item == nome:
                if len(path) == 0:
                    return print('DIRETÓRIO JÁ EXISTE')
                return child.mkdir(path)
        novo = No(nome, self)
        self.children.append(novo)
        novo.mkdir(path)

    def touch(self, path):
        contrario = list(reversed(path))
        if len(path) == 0:
            return

        nome = path.pop(0)
        for child in self.children:
            if child.item == nome:
                if len(path) == 0:
                    return print('ARQUIVO JÁ EXISTE')
                return child.touch(path)

        for child in self.children:
            if child.item in path and nome != contrario[0]:
                return self.touch(path)
            print('CAMINHO INVÁLIDO')
        novo = No(nome, self)
        self.children.append(novo)
        novo.touch(path)

    def rm(self, path):
        if len(path) == 1:
            for child in self.children:
                print(child.item)
                print(path[0])
                if child.item == path[0]:
                    print('teste')
                    child.item = None
                return
            return print('ARQUIVO ou DIRETÓRIO não existe')
        for child in self.children:
            if child.item == path[0]:
                path.pop(0)
                return self.rm(path)
        print('CAMINHO INVÁLIDO')

    def find(self, name, prefix='/'):
        ordenada = sorted(self.children, key=lambda x: x.item)
        lst = []
        for child in ordenada:
            if child.item == name[0]:
                lst.append(prefix + child.item)
            lst = lst + child.find(name, prefix + child.item + '/')
        return lst

    def mv(self, origem, destino):
        if len(origem) == 0:
            return
        for child in self.children:
            if child.item in origem and child.item in destino:
                print('teste')
                return
        print('CAMINHO INVÁLIDO')


    def cd(self, path):
        if len(path) == 0:
            return self
        atual = path.pop(0)
        if atual == '.':
            return self.cd(path)
        if atual == '..':
            return self.parent.cd(path)
        for child in self.children:
            if child.item == atual:
                return child.cd(path)
        print('CAMINHO INVÁLIDO')

    def pwd(self):
        return print(self.item)

curent = No('/', None)

while True:
    entrada = input()
    comando = ''
    caminho = []
    origem = []
    destino = []
    if entrada == 'end':
        break
    if entrada != 'show' and entrada != 'pwd':
        if 'mv' in entrada:
            comando, origem, destino = entrada.split()
            origem = origem.split('/')
            origem = list(filter(None, origem))
            destino = destino.split('/')
            destino = list(filter(None, destino))
        elif 'mkdir' in entrada:
            comando, caminho = entrada.split()
            if caminho != '/':
                caminho = caminho.split('/')
                caminho = list(filter(None, caminho))
            else:
                caminho = caminho.split()
        else:
            comando, caminho = entrada.split()
            caminho = caminho.split('/')
            caminho = list(filter(None, caminho))
    else:
        comando = entrada

    if comando == 'cd':
        curent.cd(caminho)
    if comando == 'pwd':
        curent.pwd()
    if comando == 'mkdir':
        curent.mkdir(caminho)
    if comando == 'mv':
        curent.mv(origem, destino)
    if comando == 'touch':
        curent.touch(caminho)
    if comando == 'rm':
        curent.rm(caminho)
    if comando == 'find':
        for item in curent.find(caminho):
            print(item)
    if comando == 'show':
        curent.show()