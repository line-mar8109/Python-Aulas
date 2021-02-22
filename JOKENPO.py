import emoji
from random import randint

itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0, 2)
print(emoji.emojize('''Suas opções:
[0]Pedra:facepunch:
[1]Papel:hand:
[2]Tesoura:v:''', use_aliases=True))
jogador = int(input('Qual sua jogada?: '))
print('-=' * 11)
print('Computador jogou {}'.format(itens[pc]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)
if pc == 0:  # computador jogou PEDRA
    if jogador == 0:
        print(emoji.emojize('EMPATE :grin:', use_aliases=True))
    elif jogador == 1:
        print(emoji.emojize('Jogador VENCEU :tada: ', use_aliases=True))
    elif jogador == 2:
        print(emoji.emojize('Computador VENCEU :computer:', use_aliases=True))
    else:
        print("JOGADA INVALIDA")
elif pc == 1:  # computador jogou papel
    if jogador == 0:
        print(emoji.emojize('Computador VENCEU :computer:', use_aliases=True))
    elif jogador == 1:
        print(emoji.emojize('EMPATE :grin:', use_aliases=True))

    elif jogador == 2:
        print(emoji.emojize('Jogador VENCEU :tada: ', use_aliases=True))

    else:
        print("JOGADA INVALIDA")
elif pc == 2:  # computador jogou TESOURA
    if jogador == 0:
        print(emoji.emojize('Jogador VENCEU :tada: ', use_aliases=True))

    elif jogador == 1:
        print(emoji.emojize('Computador VENCEU :computer:', use_aliases=True))

    elif jogador == 2:
        print(emoji.emojize('EMPATE :grin:', use_aliases=True))

    else:
        print("JOGADA INVALIDA")
