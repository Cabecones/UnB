import json

abrir = open(input(), 'r')
convert_json = json.load(abrir)
print()

#user = "username"
#likes = "edge_media_preview_like"[count]
publicacoes = convert_json['GraphImages']
num = 1
for publi in publicacoes:
    print(f'Publicacao numero {num}\n'
          f'{publi["username"]}\n'
          f'{publi["edge_media_preview_like"]["count"]}')
    num += 1

