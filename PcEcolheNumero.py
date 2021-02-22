from random import randint
from time import sleep
Pc = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número pensei? '))
print('...PROCESSANDO...')
sleep(2.0)
if jogador == Pc:
    print('PARABÉNS!!!! Você conseguiu me vencer')
else:
    print('Você PERDEU eu ganhei, pensei no numero {} não no número {}'.format(Pc, jogador))
