print('-'*20, 'LIVROS LIDOS', '-'*20)
livros = list()
dados = list()
while True:

    dados.append(str(input('Nome do livro: ').upper()))
    dados.append(int(input('Quantas sequecias tem?: ')))
    dados.append(str(input('Nome do Autor: ').upper()))
    dados.append(int(input('Ano lido: ')))
    if len(livros) == 0:
        mai = men = dados[1]
    else:
        if dados[1] > mai:
            mai = dados[1]
        if dados[1] < men:
            men = dados[1]
    livros.append(dados[:])
    sair = str(input('Sair [S/N]: '.upper()))
    dados.clear()
    if sair == 's':
        print('CADASTRO FINALIZADO!!!!')
        break
print('-'*20, 'ANALISE DE DADOS', '-'*20)

print(f'Você ao todo cadastrou {len(livros)} livros!!!')
print(f'A maior serie é de {mai} livros!!!', end='')
for p in livros:
    if p[1] == mai:
        print(f' [{p[0]}]', end='')
print()
print(f'A menor serie é de {men} livros!!!', end='')
for p in livros:
    if p[1] == men:
        print(f' [{p[0]}]', end='')
print()
if len(livros) >= 10:
    print('PARABÉNS!!! VOCÊ LEU MAIS DE 10 LIVROS (sem contar com as sequêcias)!')
elif len(livros) <= 10:
    print('VOCÊ LEU MENOS DE 10 LIVROS (sem contar com as sequêcias), VAMOS LER MAIS!!!!!!!')
print('-'*50)
