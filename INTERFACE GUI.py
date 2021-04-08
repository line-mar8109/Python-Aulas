from PySimpleGUI import PySimpleGUI as sg

# Layout
sg.theme('Reddit')
layout = [
    [sg.Text('Nome do Livro '), sg.Input(key='Nlivro', size=(20, 1))],
    [sg.Text('Quantidade de sequencia'), sg.Combo(values=list(range(21)), key='total_chars', default_value=0, size=(3, 1))],
    [sg.Text('Autor             '), sg.Input(key='autor', size=(20, 1))],
    [sg.Text('Ano Lido        '), sg.Combo(values=list(range(2026)), key='ano', default_value=2020, size=(5, 1))],
    [sg.Button('Registrar', key='botao', size=(10, 0)), sg.Button('Sair', key='sair', size=(10, 0))]
]


# Janela
janela = sg.Window('Tela de registro de livros', layout)
# ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WIN_CLOSED or eventos == 'sair':
        quit()
    if eventos == 'botao':
        print('Livro registrado')
        print([valores])
