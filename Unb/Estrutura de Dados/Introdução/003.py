def primo(n):
    not_prin = 0

    for count in range(2, n):
        if (n % count == 0):
            return('Não primo.')
            not_prin += 1

    if (not_prin == 0):
        return("Primo.")
    else:
        return('Não primo.')

print(primo(120))