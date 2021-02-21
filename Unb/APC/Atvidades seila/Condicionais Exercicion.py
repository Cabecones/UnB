def classificador(a, b, c):
    if a * b > c and b * c > a and a * c > b:
        forma = 'triangulo'
        print('triangulo')
    else:
        print('gondim sendo gondim')
        return

    if forma == 'triangulo' and a != b and a != c and b != c:
        print('escaleno')

    if forma == 'triangulo' and a == b or a == c or b == c:
        print('isosceles')

    if forma == 'triangulo' and a == b and a == c and b == c:
        print('equilatero')


#    if forma == 'triangulo' and
#        print('retangulo')


classificador(3, 3, 3)
