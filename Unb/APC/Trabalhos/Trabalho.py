import datetime


def atividade_1(a, b):
    cursando = a.count(2)
    formados = a.count(6)
    cursando_formados = cursando+formados
    mcursando_formados = cursando_formados/b
    porcentagem1 = mcursando_formados*100
    porcentagem2 = (1-mcursando_formados)*100
    print(f'matriculados ou formados:{porcentagem1:5.1f}\nalunos em outras situacoes:{porcentagem2:5.1f}')


def atividade_2(a, b):
    feminino = a.count(2)
    masculino = a.count(6)
    soma = feminino+masculino
    media = soma/b
    porcentagem1 = media*100
    porcentagem2 = (1-media)*100
    print(f'sexo masculino:{porcentagem1:5.1f}\nsexo feminino:{porcentagem2:5.1f}')


def atividade_3(a, b):
    i = 0
    anos = []
    while i < b:
        anos.append(2019-a[i])
        i += 1
    len_anos = len(anos)
    media = sum(anos)/len_anos
    print(f'media de anos desde ingresso:{media:5.1f}')


#Qual atividade realizar
t = int(input())

#Quantidade de linhas de entrada
ns = int(input())

ni = 0

students = []

for i in range(ns):
    nu_ano_ingresso, nu_dia_nascimento, nu_mes_nascimento, nu_ano_nascimento, tp_sexo, tp_situacao = map(int, input().split())
    temp = {
       'nu_ano_ingresso': nu_ano_ingresso,
       'nu_dia_nascimento': nu_dia_nascimento,
       'nu_mes_nascimento': nu_mes_nascimento,
       'nu_ano_nascimento': nu_ano_nascimento,
       'tp_sexo': tp_sexo,
       'tp_situacao': tp_situacao,
    }
    students.append(temp)


#atividade 1
if t == 1:
    tp_situacao = []
    for student in students:
        tp_situacao.append(student['tp_situacao'])
    len_situacao = len(tp_situacao)
    atividade_1(tp_situacao, len_situacao)


#atividade_2
if t == 2:
    tp_sexo = []
    for student in students:
        tp_sexo.append(student['tp_sexo'])
    len_sexo = len(tp_sexo)
    atividade_2(tp_sexo, len_sexo)


#atividade_3
if t == 3:
    nu_ano_ingresso = []
    for student in students:
        nu_ano_ingresso.append(student['nu_ano_ingresso'])
    len_ingresso = len(nu_ano_ingresso)
    atividade_3(nu_ano_ingresso, len_ingresso)

#atividade_4
if t == 4:
    nu_dia_nascimento = []
    for student in students:
        nu_dia_nascimento.append(student['nu_dia_nascimento'])

    nu_mes_nascimento = []
    for student in students:
        nu_mes_nascimento.append(student['nu_mes_nascimento'])

    nu_ano_nascimento = []
    for student in students:
        nu_ano_nascimento.append(student['nu_ano_nascimento'])

    DIAS = [
        'Segunda-feira',
        'Terca-feira',
        'Quarta-feira',
        'Quinta-feira',
        'Sexta-feira',
        'Sabado',
        'Domingo'
    ]

    dias_semana = []

    for y in range(ns):
        data = datetime.date(year=nu_ano_nascimento[y], month=nu_mes_nascimento[y], day=nu_dia_nascimento[y])

        indice_da_semana = data.weekday()

        dia_semana = DIAS[indice_da_semana]

        dias_semana.append(dia_semana)


    len_semana = len(dias_semana)
    domingo = dias_semana.count('Domingo')
    media_domingo = (domingo/len_semana)*100
    segunda = dias_semana.count('Segunda-feira')
    media_segunda = (segunda/len_semana)*100
    terca = dias_semana.count('Terca-feira')
    media_ter = (terca/len_semana)*100
    quarta = dias_semana.count('Quarta-feira')
    media_qua = (quarta/len_semana)*100
    quinta = dias_semana.count('Quinta-feira')
    media_qui = (quinta/len_semana)*100
    sexta = dias_semana.count('Sexta-feira')
    media_sex = (sexta/len_semana)*100
    sabado = dias_semana.count('Sabado')
    media_sabado = (sabado/len_semana)*100

    print(f'domingo:{media_domingo:5.1f}\n'
          f'segunda:{media_segunda:5.1f}\n'
          f'terca:{media_ter:5.1f}\n'
          f'quarta:{media_qua:5.1f}\n'
          f'quinta:{media_qui:5.1f}\n'
          f'sexta:{media_sex:5.1f}\n'
          f'sabado:{media_sabado:5.1f}')

#atividade5
if t == 5:
    masculino = []
    feminino = []
    for student in students:
        if student['tp_sexo'] == 2:
            masculino.append(student)
        else:
            feminino.append(student)
    len_masculino = len(masculino)
    len_feminino = len(feminino)

    alunos_regulares_masculino = []
    alunos_irregulares_masculino = []
    for student in masculino:
        if student['tp_situacao'] == 2 or student['tp_situacao'] == 6:
            alunos_regulares_masculino.append(student)
        else:
            alunos_irregulares_masculino.append(student)

    alunos_regulares_feminino = []
    alunos_irregulares_feminino = []
    for student in feminino:
        if student['tp_situacao'] == 2 or student['tp_situacao'] == 6:
            alunos_regulares_feminino.append(student)
        else:
            alunos_irregulares_feminino.append(student)

    len_regulares_m = len(alunos_regulares_masculino)
    len_irregulares_m = len(alunos_irregulares_masculino)
    len_regulares_f = len(alunos_regulares_feminino)
    len_irregulares_f = len(alunos_irregulares_feminino)
    sum_masculinos = len_regulares_m + len_irregulares_m
    sum_femininos = len_regulares_f + len_irregulares_f

    media_masculino_r = (len_regulares_m / sum_masculinos)*100
    media_feminino_r = (len_regulares_f / sum_femininos)*100
    media_masculino_i = (len_irregulares_m / sum_masculinos)*100
    media_feminino_i = (len_irregulares_f / sum_femininos)*100

    print(f'dentre masculinos:\n'
          f'matriculados ou formados:{media_masculino_r:5.1f}\n'
          f'alunos em outras situacoes:{media_masculino_i:5.1f}\n'
          f'dentre femininos:\n'
          f'matriculados ou formados:{media_feminino_r:5.1f}\n'
          f'alunos em outras situacoes:{media_feminino_i:5.1f}')


#atividade6
if t == 6:
    anos_regulares = []
    anos_irregulares = []

    for student in students:
        if student['tp_situacao'] == 2 or student['tp_situacao'] == 6:
            anos_regulares.append(student['nu_ano_ingresso'])
        else:
            anos_irregulares.append(student['nu_ano_ingresso'])
    print(f'dentre matriculados ou formados:')
    atividade_3(anos_regulares, len(anos_regulares))
    print(f'dentre alunos em outras situacoes:')
    atividade_3(anos_irregulares, len(anos_irregulares))


#atividade7
if t == 7:
    masculino = []
    feminino = []
    for student in students:
        if student['tp_sexo'] == 2:
            masculino.append(student)
        else:
            feminino.append(student)
    len_masculino = len(masculino)
    len_feminino = len(feminino)

    nu_dia_nascimento = []
    for student in masculino:
        nu_dia_nascimento.append(student['nu_dia_nascimento'])

    nu_mes_nascimento = []
    for student in masculino:
        nu_mes_nascimento.append(student['nu_mes_nascimento'])

    nu_ano_nascimento = []
    for student in masculino:
        nu_ano_nascimento.append(student['nu_ano_nascimento'])

    DIAS = [
        'Segunda-feira',
        'Terca-feira',
        'Quarta-feira',
        'Quinta-feira',
        'Sexta-feira',
        'Sabado',
        'Domingo'
    ]

    dias_semana = []

    for y in range(len_masculino):
        data = datetime.date(year=nu_ano_nascimento[y], month=nu_mes_nascimento[y], day=nu_dia_nascimento[y])

        indice_da_semana = data.weekday()

        dia_semana = DIAS[indice_da_semana]

        dias_semana.append(dia_semana)

    len_semana = len(dias_semana)
    domingo = dias_semana.count('Domingo')
    media_domingo = (domingo / len_semana) * 100
    segunda = dias_semana.count('Segunda-feira')
    media_segunda = (segunda / len_semana) * 100
    terca = dias_semana.count('Terca-feira')
    media_ter = (terca / len_semana) * 100
    quarta = dias_semana.count('Quarta-feira')
    media_qua = (quarta / len_semana) * 100
    quinta = dias_semana.count('Quinta-feira')
    media_qui = (quinta / len_semana) * 100
    sexta = dias_semana.count('Sexta-feira')
    media_sex = (sexta / len_semana) * 100
    sabado = dias_semana.count('Sabado')
    media_sabado = (sabado / len_semana) * 100

    print(f'dentre masculinos:')

    print(f'domingo:{media_domingo:5.1f}\n'
          f'segunda:{media_segunda:5.1f}\n'
          f'terca:{media_ter:5.1f}\n'
          f'quarta:{media_qua:5.1f}\n'
          f'quinta:{media_qui:5.1f}\n'
          f'sexta:{media_sex:5.1f}\n'
          f'sabado:{media_sabado:5.1f}')

    print(f'dentre femininos:')

    nu_dia_nascimento = []
    for student in feminino:
        nu_dia_nascimento.append(student['nu_dia_nascimento'])

    nu_mes_nascimento = []
    for student in feminino:
        nu_mes_nascimento.append(student['nu_mes_nascimento'])

    nu_ano_nascimento = []
    for student in feminino:
        nu_ano_nascimento.append(student['nu_ano_nascimento'])

    DIAS = [
        'Segunda-feira',
        'Terca-feira',
        'Quarta-feira',
        'Quinta-feira',
        'Sexta-feira',
        'Sabado',
        'Domingo'
    ]

    dias_semana = []

    for y in range(len_feminino):
        data = datetime.date(year=nu_ano_nascimento[y], month=nu_mes_nascimento[y], day=nu_dia_nascimento[y])

        indice_da_semana = data.weekday()

        dia_semana = DIAS[indice_da_semana]

        dias_semana.append(dia_semana)

    len_semana = len(dias_semana)
    domingo = dias_semana.count('Domingo')
    media_domingo = (domingo / len_semana) * 100
    segunda = dias_semana.count('Segunda-feira')
    media_segunda = (segunda / len_semana) * 100
    terca = dias_semana.count('Terca-feira')
    media_ter = (terca / len_semana) * 100
    quarta = dias_semana.count('Quarta-feira')
    media_qua = (quarta / len_semana) * 100
    quinta = dias_semana.count('Quinta-feira')
    media_qui = (quinta / len_semana) * 100
    sexta = dias_semana.count('Sexta-feira')
    media_sex = (sexta / len_semana) * 100
    sabado = dias_semana.count('Sabado')
    media_sabado = (sabado / len_semana) * 100

    print(f'domingo:{media_domingo:5.1f}\n'
          f'segunda:{media_segunda:5.1f}\n'
          f'terca:{media_ter:5.1f}\n'
          f'quarta:{media_qua:5.1f}\n'
          f'quinta:{media_qui:5.1f}\n'
          f'sexta:{media_sex:5.1f}\n'
          f'sabado:{media_sabado:5.1f}')