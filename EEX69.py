while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).strip().upper()[0]

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar'))