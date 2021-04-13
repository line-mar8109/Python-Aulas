from time import sleep


print('''Quer Hackear a Nasa?:
[1]Sim
[2]Não''')
escolha = int(input('Sua opção: '))

if escolha == 1:
    for c in range(0, 101, 10):
        print('HACKING Nasa {}%.....'.format(c))
        sleep(1)

    print('HACKING Nasa SUCEDIDO')
elif escolha == 2:
    print('Tudo bem então, bye!')
elif escolha != 1 or escolha != 2:
    print('ERRO!!! FAÇA UMA ESCOLHA!!')
