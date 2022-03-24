def inverte(palavra):
    if len(palavra) == 0:
        return palavra
    else:
        return inverte(palavra[1:]) + palavra[0]

print(inverte('lamina'))