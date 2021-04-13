from random import randint
from time import sleep
from PySimpleGUI import PySimpleGUI as sg

sg.theme('Dark')
arquivo = open("HISTORICOBOOKYEARS.txt", "w")
lista = list()
jogos = list()
print('-='*20)
print('         JOGA NA MEGA SENNA       ')
print('-='*20)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-='*5, f'SORTEANDO {quant} JOGOS ', '-='*5)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(0.5)
arquivo.write("Jogos: " + str(jogos))
arquivo.close()
print('-='*6, '  Boa sorte!! ', '-='*6)
print('-='*20)
