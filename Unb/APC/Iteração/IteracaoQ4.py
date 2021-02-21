num = input()
negativo = num.count('-')
inverse = num[::-1]

if negativo == 0:
    print(inverse)
else:
    num = num[1:]
    inverse = num[::-1]
    print(f'-{inverse}')