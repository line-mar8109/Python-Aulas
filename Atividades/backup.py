print('-'*10, 'LIVROS LIDOS', '-'*10)
soma = cont = 0
while True:

    nome = str(input('Nome do livro: '))
    seque = int(input('Quantas sequecias tem?: '))
    autor = str(input('Nome do Autor: '))
    ano = int(input('Ano lido: '))
    sair = str(input('Sair [S/N]: '.upper()))
    cont += 1
    soma += seque
    if sair == 's':
        print('PROGRAMA FINALIZADO!!!!')
        break

print(f'Você leu {soma} livros! ')
if seque >= 30:
    print('Parabens você leu mais de 30 Livros ')
