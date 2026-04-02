def simularCrescimento(pop, taxa, limite):
    anos = 0
    while pop <= limite:
        pop = pop * (1+taxa/100)
        anos += 1
    return anos

#main 
p = float(input('População:'))
t = float(input('taxa (%)'))
1 = float(input('Limite: '))
print('fAnos = {simularCrescimento(p,t,1)}')
