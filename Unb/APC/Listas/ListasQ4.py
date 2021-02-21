n = int(input())
a = list(map(int, input().split()))
b = sorted(a)
reservas = n - 11
if n > 22:
    sum_reservas = sum(b[reservas-11:reservas])
else:
    sum_reservas = sum(b[:reservas])
sum_titulares = sum(b[reservas:])
sub = sum_titulares - sum_reservas

print(sub)
