num = []
maior = 0
men = 0
for c in range (0, 5):
    num.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        maior = men = num[c]
    else:
        if num [c] > maior:
            maior = num[c]
        if num[c] < men:
            men = num[c]
print('=_'*30)
print(f'Você digitou os valores{num}')
print(f'O maior valor digitado foi {maior}')
print(f'O menor valor digitado foi {men}')
