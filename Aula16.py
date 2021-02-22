lanche = ('hamburguer', 'suco', 'pizza')
print(lanche[1])
print(lanche[2])
print(lanche[0])
# tuplas são imutaveis menos se for apagala inteira com o del
for pos, c in enumerate(lanche):
    print(f'Eu comi {c} na posição {pos}')
print('Comi muito!!!!')
print(sorted(lanche))  # mostra a tupla em ordem
