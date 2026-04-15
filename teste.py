meses = ['jan','fev','mar','abr','mai','jun',
         'jul','ago','set','out','nov','dez']

soma = 0
for i in range(12):
    salario = float(input(f'Digite o salario de {meses[i]}:'))
    soma = soma + salario
    
sal13 = soma/12
ferias = sal13 * 1/3
print(f'13 salario : {sal13}, ferias : {ferias}')
