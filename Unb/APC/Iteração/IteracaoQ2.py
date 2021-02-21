nota = int(input())
notas = []

while nota != -1:
    notas.append(nota)
    nota = int(input())

media = sum(notas) / len(notas)

print(f'{int(media)}')