def em_lista(root):
    if root is None:
        return None

    if root.dir is not None:
        root = rotaciona_esquerda(root)
        return em_lista(root)

    if root.esq is not None:
        root.esq = em_lista(root.esq)
    return root