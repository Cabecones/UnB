qtd_jogadores = int(input())
qtd_reservas = qtd_jogadores-11
jogadores = list(map(int, input().split()))
jogadores = sorted(jogadores, reverse=True)
reservas = []
zero = 0

while zero < qtd_reservas:
    reservas.append(jogadores[qtd_jogadores-1])
    qtd_jogadores -= 1
    zero += 1
    jogadores.pop()

if len(reservas) > 11:
    reservas = sorted(reservas, reverse=True)
    del(reservas[11:])

print(reservas)
print(jogadores)
print(sum(jogadores)-sum(reservas))