def anobissexto(a):
    if a%400 == 0:
        return('Sim')
    elif a%100 == 0:
        return('Nao')
    elif a%4 == 0:
        return('Sim')
    else:
        return('Nao')

print(anobissexto(2100))