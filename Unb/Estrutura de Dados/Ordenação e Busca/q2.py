def piloto():
    nome = input()
    parciais = [float(item) for item in input().split()]
    total = round(sum(parciais), 3)
    return [nome, total]

def converter(time):
    minute = time // 60
    segundo = time % 60
    return f"{int(minute)}:{segundo:06.3f}"

num_pilotos = int(input())

info_piloto = [piloto() for i in range(num_pilotos)]

for i in range(len(info_piloto)):
    info_piloto[i][1] = converter(info_piloto[i][1])
x = sorted(info_piloto, key=lambda x: x[1])

[print(f"{i + 1}. {x[i][0]} ({x[i][1]})") for i in range(len(x))]