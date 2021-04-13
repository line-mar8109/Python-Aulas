import random
import PySimpleGUI as sg
import os


class PassGen:
    def __init__(self):
        sg.theme('Black')
        layout = [
            [sg.Text('Site/Software', size=(10, 1)),
             sg.Input(key='site', size=(20, 1))],
            [sg.Text('Email/Usuario', size=(10, 1)),
             sg.Input(key='usuario', size=(20, 1))],
            [sg.Text('Quantidade de caracteres'), sg.Combo(values=list(range(30)), key='total_chars',
                                                           default_value=1, size=(3, 1))],
            [sg.Output(size=(32, 5))],
            [sg.Button('Gerar Senha'), sg.Button('Sair')]
        ]
        # Declarar Janela
        self.janela = sg.Window('Password Generator', layout)

    def Iniciar(self):
        while True:
            evento, valores = self.janela.read()
            if evento == sg.WINDOW_CLOSED or 'Sair':
                break
            if evento == 'Gerar Senha':
                nova_senha = self.gerar_senha(valores)
                print(nova_senha)
    def gerar_senha(self, valores):
        char_list = 'ABCDEFGHIJKLMNOPQRSTUVabcdefghijklmnopqrstuv1234567890!@#$%*&'
        chars = random.choices(char_list, k=int(valores['total_chars']))
        return new_pass


    def salvarSenha(self):
        pass


gen = PassGen()
gen.Iniciar()
