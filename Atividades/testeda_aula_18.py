livros = list()
dados = list()
for c in range(0, 3):
    dados.append(str(input('Nome do livro: ')))
    dados.append(int(input('Quantas sequencias tem: ')))
    livros.append(dados[:])  # copia do dado
    dados.clear()
print(livros)
for c in livros:
    if c[1] >= 4:
        print('Voce leu muitos livros!')
