num = [2, 3, 4, 5]
print(num)
num[2] = 9
print(num)
num.append(7)
print(num)
num.sort()
print(num)
num.sort(reverse=True)
print(num)
print(f'Essa lista tem {len(num)} elementos!')
num.pop()
print(num)
print(f'Essa lista tem {len(num)} elementos agr!')
print('-'*30)
valores = []
valores.append(5)
valores.append(6)
valores.append(3)

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista')
