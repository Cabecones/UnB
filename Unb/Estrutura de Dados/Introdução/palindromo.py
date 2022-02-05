palavra = input()
palavra1 = []
palavra2 = list(reversed(palavra))
for letra in palavra:
    palavra1.append(letra)

for i in range(len(palavra)):
    if palavra1[i] != palavra2[i]:
        palavra2[i] = palavra1[i]
        print(True)
        break



lst_new = [str(a) for a in palavra2]
palavra3 = ("" . join(lst_new))

if str(palavra3) == str(palavra3)[::-1]:
    print("POSSÍVEL")
else:
    print("IMPOSSÍVEL")