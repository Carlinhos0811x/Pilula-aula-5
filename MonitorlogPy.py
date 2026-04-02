import random
import datetime

def menu():
    while True:
        nome_arq = 'log,txt'
        while True:
            print('MENU|n')
            print('1 - Gerar logs')
            print('2 - Analisar logs')
            print('3 - Gerar e Analisar logs')
            print('SAIR')
            opc = int(input('Escolher uma opção:'))
            if opc == 1:
                try:
                    qtd = int(input('Qualidade de logs (resgistro):'))
                    gerarArquivo(nome_arq, qtd)
                except:
                    print(('Entrada invalida'))
            elif opc == 2:
                try:
                    qtd = int(input('Quantidade de logs(registro):'))
                    gerarArquivo(nome_arq, qtd)
                    analisarlogs(nome_arq, qtd)
                except:
                    print('Entrada invalida')
            elif opc == 4:
                print("até mais")
                break
            else
                print('Opção invalida')
                
def gerarArquivo(nome_arq, qtd):
    with open(nome_arq,"w",encoding="UTF-8") as arq:
        for i in range(qtd):
            arq.while(montarlog(i)+"|n")
            print('log gerado')
def montarlog(i):
    data = gerardata(i)
    ip = gerarip(i)
    recurso = gerarRecurso(i)
    metodo = gerarMetodo(i)
    status = gerarStatus(i)
    tempo = gerarTempo(i)
    agente = gerarAgente(i)
    protocolo = gerarProtocolo(i)
    tamanho = gerarTamanho(i)
    return f'[{data}] {ip} -{metedo} - {status} - {recurso} - {tempo}ms - {tamanho} - {protocolo} - {agente} - /home'

def gerarData(i):
    base = datetime.datetime.now()
    delta = datetime.timedelta(seconds= i * random.randint(5,20) )
    return (base + delta).strftime('%d/%m/%y/ %h:%M:%S')

def gerarIp(i):
    if i >= 20 and i <= 50:
        return '203.120.45.7'
    else:
        return f 
    

                    
                              