num = (int(input('Digite o 1º número: ')),
       int(input('Digite o 2º número: ')),
       int(input('Digite o 3º número: ')),
       int(input('Digite o 4º número: ')))
print(f'Você digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3) + 1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
