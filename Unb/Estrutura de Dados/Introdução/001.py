def imc(altura, peso):
    resultado = peso/altura**2
    if resultado < 18.6:
        return(f'Abaixo do peso, IMC = {resultado:.2f}')
    elif 18.6 <= resultado <= 24.9:
        return(f'Peso normal, IMC = {resultado:.2f}')
    elif 25 <= resultado <= 29.9:
        return(f'Sobrepeso, IMC = {resultado:.2f}')
    else:
        return(f'Obesidade, IMC = {resultado:.2f}')


print(imc(1.72, 66.00))