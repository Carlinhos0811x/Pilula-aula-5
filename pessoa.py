class Pessoa:
    def __init__(self, nome , idade):
        self.nome = nome
        self.idade = idade
        
    def apresentar(self):
        print(f'ola, me chamo {self.nome} e tenho {self.idade} anos')
        
    def fazer_aniver(self):
        self.idade += 1 