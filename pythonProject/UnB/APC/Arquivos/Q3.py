cript = open(input(), 'r').read().split('\n')

for i in range(0, len(cript), 2):
    if cript[i] != '':
        dimin = int(cript[i])
        x = []
        for letra in cript[i+1]:
            x.append(ord(letra)-dimin)
        for numerozinho in x:
            print(chr(numerozinho), end='')
        print()