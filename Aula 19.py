pessoas = {'nome': 'aline', 'sexo': 'Feminino'}
print(f'A {pessoas["nome"]} é do sexo {pessoas["sexo"]}.')
print(pessoas.keys())  # chaves
print(pessoas.values())  # valores
print(pessoas.items())  # todos dentro do dicionario
for k, v in pessoas.items():   # no dicionarios usa o items em vez do enumerate
    print(f'{k} = {v}')

