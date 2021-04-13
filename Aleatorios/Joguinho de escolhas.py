from time import sleep


nome = (str(input('Qual seu nome?: ')))  # apresentação
print('Olá {}!'.format(nome))
sleep(1.0)
print('+_' * 20)
print('{} você iria para o cominho difícil ou facil?'.format(nome))  # escolha
print('+_' * 20)
sleep(1.0)
escolha = str(input('Digite difícil ou facil: '))
if escolha == 'dificil':
    print("Parabens você passou para a proxima fase")
elif escolha == 'facil':
    print('Nem sempre o facil te leva a vitória, VOCÊ MORREU!')
elif escolha != 'facil' or escolha != 'dificil':
    print("Digite facil ou dificil pvf!!!!")
