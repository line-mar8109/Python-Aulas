teste = list()
teste.append('Giusta')
teste.append(40)
galera = list()
galera.append(teste[:])  # importante fazer um fatiamento assim que se cria uma copia
teste[0] = 'Maria'
teste[1] = '67'
galera.append(teste)
print(galera)
turma = [['João', 34], ['Ali', 12], ['Julia', 15]]
for p in turma:
    print(p[1], end='')
    print(' anos ')
    print(f'{p[0]} tem {p[1]} anos de idade.')
