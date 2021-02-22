temp = []
princ = []

while True:
    temp.append(str(input('NOME: ').upper()))
    temp.append(float(input('PESO: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('QUER CONTINUAR? [S/N]'))
    if resp in 'Nn':
        break
print('=_'*20)
print(f'Ao todo, você cadastrou {len(princ)} pessoas.')
print(f'O maior peso foi de {mai} Kg', end='')
for p in princ:
    if p[1] == mai:
        print(f' [{p[0]}]', end='')
print()
print(f'O maior peso foi de {men} Kg', end='')
for p in princ:
    if p[1] == men:
        print(f' [{p[0]}]', end='')
print()
print('=_'*20)
