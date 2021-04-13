def soma(a, b):
    s = a + b
    print(s)


def contador(*num):  # desempacotador
    print(num)


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


# Prgrama principal
soma(2, 6)
soma(3, 6)
contador(2, 8, 6)
contador(2, 6, 1)
valores = [6, 3, 2, 5, 1]
dobra(valores)
print(valores)
