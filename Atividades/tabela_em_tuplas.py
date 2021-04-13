# Tabelas em tuplas, será que vai?
itens = ('lapis', 1.75,
         'borracha', 2,
         'caderno', 3.59)
print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)
for pos in range(0, len(itens)):
    if pos % 2 == 0:
        print(f'{itens[pos]:.<30}', end='')
    else:
        print(f'R${itens[pos]:>7.2f}')
print('-'*40)
