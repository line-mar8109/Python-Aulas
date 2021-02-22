n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opçao = 0
while opçao != 5:
    print('''    [1]Somar
    [2]Mutiplicar
    [3]Maior
    [4]Novos Numeros
    [5]Sair do programa
    Qual é a sua opção''')
    opçao = int(input('Sua opção: '))
    if opçao == 1:
        soma = n1 + n2
        print('A somo entre {} + {} é {}'.format(n1, n2, soma))
    elif opçao == 2:
        muitl = n1*n2
        print('A resultado entre {} X {} é {}'.format(n1, n2, muitl))
    elif opçao == 3:
        if n1 > n2:
            print('O Numero {} é MAIOR que o numero {}'.format(n1, n2))
        elif n1 < n2:
            print('O numero {} é MAIOR que o numero {}'.format(n2, n1))
        elif n1 == n2:
            print('Os numeros são IGUAIS')
    elif opçao == 4:
        print('INFORME NOVAMENTE')
        n1 = int(input('Primero valor: '))
        n2 = int(input('Segundo valor: '))
    elif opçao == 5:
        print('OK! Até mais!')
        exit()
    else:
        print('OPÇÃO INVALIDA')
    print('-=-'*10)

print('Fim do programa! Obrigado!')
