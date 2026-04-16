class ContaBancaria:
    #construtor da classe
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        
    def depositar(self, valor):
        self.saldo += valor
        print(f'Deposito de R$ {valor}')
        
    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f'Saque de R$ {valor}')
            return valor
        
        else:
            print('Pobre')
    def exibir(self):
        print(f'Titular {self.titular}, R$ {self.saldo}')
                
            
                    