from time import sleep


def contador(i, f, p):  # i= inicio, f= fim, p= passo
    print(f'Contagem de {i} até {f} de {p} em {p}')

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont += p
        print('Fim!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont -= p
        print('Fim!')


# contador(1, 10, 1)
contador(5, 45, 4)
print('Agora é sua vez de contar!')
ini = int(input('Inicio: '))
fim = int(input('Fim; '))
pas = int(input('Passo: '))
contador(ini, fim, pas)
