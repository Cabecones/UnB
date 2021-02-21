moradores = int(input())
i = 0
subs = []

while i < moradores:
    num = int(input())
    if num < 1000:
        dinheiro = 1000-num
        subs.append(dinheiro)
    else:
        dinheiro = 0
        subs.append(dinheiro)
    i += 1

print(f'{sum(subs)}')