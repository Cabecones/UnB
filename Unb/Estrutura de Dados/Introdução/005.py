def primo(num):
    return all(num % i != 0 for i in range(2, num))

def primos_gemeos(n):
    resultados = []
    j = 1
    while len(resultados) < n:
        j += 2
        if(primo(j) and primo(j + 2)):
            resultados.append((j, j + 2))
    return resultados

print(primos_gemeos(2))