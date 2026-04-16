from pessoa import Pessoa

pessoas = []

for i in range(3):    
    nome = input('nome :')
    idade = int(input('idade :'))
    pessoas.append( Pessoa(nome,idade))
    
pessoas [0].fazer_aniver()
pessoas[0].apresentar()

for p in pessoas:
    p.apresentar()
    