from time import sleep


print('''Quer Hackear a Nasa?:
[1]Sim
[2]Não''')
escolha = int(input('Sua opção: '))

if escolha == 1:
    print('HACKING Nasa 10%.....')
    sleep(1)
    print('HACKING Nasa 30%.....')
    sleep(0.8)
    print('HACKING Nasa 47%.....')
    sleep(0.5)
    print('HACKING Nasa 50%.....')
    print('HACKING Nasa 60%.....')
    print('HACKING Nasa 89%.....')
    sleep(2)
    print('HACKING Nasa 99%.....')
    sleep(1.5)
    print('HACKING Nasa 100%....')
    print('HACKING Nasa SUCEDIDO')
elif escolha == 2:
    print('Tudo bem então, bye!')
