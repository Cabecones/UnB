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
        if len(path) == 0:
            return
        if len(path) == 1:
            nome1 = path.pop(0)
            print(nome1)
            for child in self.children:
                if child.item == nome1:
                    print('ARQUIVO JÁ EXISTE')
                    return
            return self.children.append(No(nome1, self))
        nome = path.pop(0)
        for child in self.children:
            if child.item != nome:
                print('CAMINHO INVÁLIDO')
                return

    def rm(self, path):
        print(path)
        if len(path) == 1:
            for child in self.children:
                if child.item == path[0]:
                    child.item = None
                return
            return print('ARQUIVO ou DIRETÓRIO não existe')
        for child in self.children:
            if child.item == path[0]:
                path.pop(0)
                return self.rm(path)
        print('CAMINHO INVÁLIDO')

    def find(self, name, prefix='/'):
        self.children.sort(key=lambda x: x.item)
        lst = []
        for child in self.children:
            if child.item == name:
                lst.append(prefix + child.item)
            lst = lst + child.find(name, prefix + child.item + '/')
        return lst

    def mv(self, origem, destino, curent):
        if curent != '/':
            if len(origem) == 1:
                for child in self.children:
                    if child.item == origem[0]:
                        if child.item != destino[0]:
                            mover = child.item.pop()
                            No.mkdir(mover)
                        return
                return print('ARQUIVO ou DIRETÓRIO não existe')
            print('CAMINHO INVÁLIDO')
        else:
            return

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
        curent.mv(origem, destino, curent)
    if comando == 'touch':
        curent.touch(caminho)
    if comando == 'rm':
        curent.rm(caminho)
    if comando == 'find':
        print(curent.find(caminho))
    if comando == 'show':
        curent.show()