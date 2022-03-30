import itertools

def crypto(chamada):
    lixo, valor = chamada.split()
    inp_list = []
    for i in range(1, len(valor) + 2):
        inp_list.append(i)
    permutations = list(itertools.permutations(inp_list))

    crypt = []
    for i in valor:
        crypt.append(i)
    result = []

    for combi in permutations:
        condition = 0
        num = 0
        for sin in crypt:
            num_ant = combi[num]
            if sin == '-':
                if num_ant > combi[num + 1]:
                    condition = 1
                    num += 1
                else:
                    condition = 0
                    break
            elif sin == '+':
                if num_ant < combi[num + 1]:
                    condition = 1
                    num += 1
                else:
                    condition = 0
                    break
        if condition == 1:
            for i in combi:
                print(i, end='')
            break

def deYodafy(chamada):
    frase = list(chamada.split())
    frase.remove('deYodafy')  # retirar o yodafy na função de cima, pois ele será um comando

    for palavra in frase:
        points = '!@#$?.'
        for char in palavra:
            if char in points:
                frase.append(palavra.replace(char, ''))
                frase.remove(palavra)
                frase.insert(0, frase[0].replace(frase[0], frase[0] + char))
                frase.remove(frase[1])
                frase = frase[::-1]

    for palavra in frase:
        print(palavra, end=' ')

def merge(chamada):
    cordenada = chamada.split(' ', 1)
    comando = []
    comando.append(cordenada[0])
    cordenada.remove('merge')
    cordenada = cordenada[0].split('] ')
    cordenada = sorted(cordenada)
    cordenadas = []

    for palavra in cordenada:
        points = '['
        for char in palavra:
            if char in points:
                cordenadas.append(palavra.replace(char, ''))

    for palavra in cordenadas:
        points = ']'
        for char in palavra:
            if char in points:
                cordenadas.append(palavra.replace(char, ''))
                cordenadas.remove(palavra)

    for num in range(3):
        for palavra in cordenadas:
            points = ','
            for char in palavra:
                if char in points:
                    cordenadas.append(palavra.replace(char, ''))
                    cordenadas.remove(palavra)

    cordenadas = sorted(cordenadas)
    x = []
    y = []

    for l in cordenadas:
        a, b = l.split()
        x.append(a)
        y.append(b)

    i = 0
    j = 1

    result = []
    for cord in range(len(cordenadas) // 2):
        result.append(f'[{x[i]}, {y[j]}]')
        i += 2
        j += 2
    for i in result:
        print(i, end=' ')
    #verificar se o y do primeiro é == ao x do segundo

all_func = []

while True:
    func = []
    entrada = input()
    if entrada == 'halt':
        break
    else:
        if entrada != 'process' and 'halt':
            comando, n = entrada.split()
            for i in range(int(n)):
                a = input()
                func.append(a)
        elif entrada == 'process':
            if len(all_func) != 0:
                all_func = list(filter(None, all_func))
                chamada = all_func[0].pop(0)
                all_func.append(all_func.pop(0))
                if 'crypto' in chamada:
                    crypto(chamada)
                    print('')
                elif 'deYodafy' in chamada:
                    deYodafy(chamada)
                    print('')
                elif 'merge' in chamada:
                    merge(chamada)
                    print('')
    all_func.append(func)
all_func = list(filter(None, all_func))

processos = len(all_func)
somar = []
for i in all_func:
    somar.append(len(i))
comandos = sum(somar)
print(f'{processos} processo(s) e {comandos} comando(s) órfão(s).')