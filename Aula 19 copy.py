
estado = dict()
brasil = list()
for c in range(0, 2):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input("Sigla do estado: "))
    brasil.append(estado.copy())  # para copiar a lista no dicionario, pq não se usa o fatiamento
print(brasil)
print('HEllo')