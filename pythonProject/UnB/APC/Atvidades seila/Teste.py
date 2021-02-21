def area(arg1, arg2, forma):
    if forma == 'losango':
        area = int((arg1*arg2)/2)
        print(f'O {forma} tem {area} de area')
    elif forma == 'retangulo':
        area = int((arg1*arg2))
        print(f'O {forma} tem {area} de area')
    elif forma == 'triangulo':
        area = int((arg1*arg2)/2)
    elif forma == 'circulo':
        area = int((arg1 ** 2) * arg2)
        print(f'O {forma} tem {area} de area')
