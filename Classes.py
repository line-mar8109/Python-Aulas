class Pessoas:
    def __init__(self, nome, idade, comendo= False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo

    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo!')
            return
        print(f'{self.nome} está comendo {alimento}!')
        self.comendo = True

    def para_de_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo!')
            return

        print(f'{self.nome} parou de comer!')
        self.comendo = False
