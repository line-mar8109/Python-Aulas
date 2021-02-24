# interação help help() no pyconsole
# quit para sair do help
# print(input.__doc__)


# docstrings são manuais para uma função
def contador(i, f, p):
    """
    - Faz uma contagem e mostra na tela.    #docstrings
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c}', end='')
        c += p
    print('Fim!')


help(contador)


# parametros opcinais
def somar(a=0, b=0, c=0):
    """
    -faz a soma dos numero citados tendo valor opcional
    :param a:primeiro valor para ser somado
    :param b: segundo valor para ser somado
    :param c: terceira valor para ser somado
    """
    s = a + b + c
    print(f'A soma vale {s}')


somar(3, 2, 4)
somar(2, 5)
somar(1)


# escopo de variaveis onde vai existir e onde não vai existir variavel global e local
def funcao():
    global n2
    n1 = 4
    n2 = 6
    print(f'n1 dentro (local) vale {n1}')
    print(f'n2 dentro (local) vale {n2}')


n1 = 2
n2 = 8
funcao()
print(f'n1 fora (global) vale {n1}')
print(f'n2 fora (global) vale {n2}')


# return
def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = somar(2, 6, 5)
r2 = somar(86, 6, 5)
r3 = somar(5)
print(f'Meus calculos deram {r1}, {r2} e {r3}.')
