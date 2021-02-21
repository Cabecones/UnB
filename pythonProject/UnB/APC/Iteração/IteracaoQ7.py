n = int(input())
print('1 elefante incomoda muita gente...')
print('2 elefantes incomodam, incomodam muito mais...')
a = 1
i = 1
b = 2

while i < n:
    c = b + 1
    d = c - 1
    print(f'{b} elefantes incomodam muita gente...')
    b += 1
    print(f'{c} elefantes '+'incomodam, '*d+'incomodam '+'muito mais...')
    i += 1
