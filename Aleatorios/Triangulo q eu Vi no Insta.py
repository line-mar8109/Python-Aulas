linhas = 6
k = 2 * linhas - 2
for i in range(linhas, -1, 1):
    for j in range(k, 0, -1):
        print(end='')
    k = k + 1
    for j in range(0, i + 1):
        print('*', end='')
    print('')
# aparentemente não foi como pensei, fazer oq, nem entendi o codigo.
