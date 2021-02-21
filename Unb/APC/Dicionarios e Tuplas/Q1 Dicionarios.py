def convert(l):
    return [dict([i]) for i in l]


l = [(3, 91), (4, 69), (1, 85), (1, 96), (1, 7), (4, 94)]
resposta = convert(l)
print(resposta)