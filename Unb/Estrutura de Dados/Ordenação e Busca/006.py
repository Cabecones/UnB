n = input()

lista = input().split()

numeros = []

for i in lista:
    numeros.append(int(i))

tamanho = int(len(numeros)/2)
soma = sum(numeros[0:tamanho])-sum(numeros[tamanho:])
positivo = abs(soma)

    
print(positivo)