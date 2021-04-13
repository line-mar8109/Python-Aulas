from random import randint

numbers = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('Os valores sorteados foram: ', end='')
for n in numbers:
    print(f'{n} ', end='')
print(f'\nO maior valor sorteado foi {max(numbers)}')
print(f'O menor valor sorteado foi {min(numbers)}')
