time = [('Atlético Mineiro',  38),  ('Internacional', 36), ('São paulo', 36), ('Flamengo', 36),
        ('Palmeiras', 30), ('Santos', 34), ('Grêmio', 33)]


print(str('''Você quer que lista seja em ordem crencente ou ascendente?'
[1] Crecente
[2] Ascendente'''))

escolha = (int(input('Sua escolha: ')))
print('-='*20)
if escolha == 1:
    time.sort(key=lambda x: x[1])

    for t in time:
        print(f'O time {t[0]} está com {t[1]} pontos.')

elif escolha == 2:
    time.sort(key=lambda x: x[1], reverse=True)
    for p in time:
        print(f'o time {p[0]} está com {p[1]} pontos.')
else:
    print('Valor invalido!!')
    exit()
    print('-=' * 20)
print('-='*20)
