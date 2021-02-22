soma = cont = 0
while True:
    num = int(input('Digite o numero (999 para parar): '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'A soma dos {cont} valores é {soma}')
