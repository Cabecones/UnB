num = []
def soma_aninhada(a):
    for item in a:
        soma = sum(item)
        num.append(soma)
        if item == int:
            num.append(item)
    return num


print(soma_aninhada([[1,1,1,1,1],[1,1,1]]))
