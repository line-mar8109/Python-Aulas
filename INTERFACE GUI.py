from PySimpleGUI import PySimpleGUI as sg


# Layout
sg.theme('Reddit')
layout = [
    [sg.Text('Nome do Livro '), sg.Input(key='Nlivro', size=(20, 1))],
    [sg.Text('Sequencias    '), sg.Input(key='Qseque', size=(20, 1))],
    [sg.Text('Autor             '), sg.Input(key='autor', size=(20, 1))],
    [sg.Text('Ano Lido        '), sg.Input(key='ano', size=(20, 1))],
    [sg.Button('Registrar'), sg.Button('Sair')]
]


# Janela
janela = sg.Window('Tela de registro de livros', layout)
# ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WIN_CLOSED or eventos == 'Sair':
        break
    if eventos == 'Registrar':
        print('Livro registrar')
        print([valores])
        break
