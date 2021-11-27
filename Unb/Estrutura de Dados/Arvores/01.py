def mostra(raiz):
    def vazio(node):
        if node == None:
            return '()'
        else:
            return f'({node.dado} {vazio(node.esq)} {vazio(node.dir)})'

    print(vazio(raiz))