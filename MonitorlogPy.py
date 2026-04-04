import random
import datetime


def menu():
    nome_arq = 'log.txt'

    while True:
        print('\nMENU')
        print('1 - Gerar logs')
        print('2 - Analisar logs')
        print('3 - Gerar e Analisar logs')
        print('4 - SAIR')

        try:
            opc = int(input('Escolher uma opção: '))
        except ValueError:
            print('Entrada inválida')
            continue

        if opc == 1:
            try:
                qtd = int(input('Quantidade de logs (registros): '))
                gerarArquivo(nome_arq, qtd)
            except ValueError:
                print('Entrada inválida')

        elif opc == 2:
            try:
                qtd = int(input('Quantidade de logs (registros): '))
                gerarArquivo(nome_arq, qtd)
                analisarLogs(nome_arq, qtd)
            except ValueError:
                print('Entrada inválida')

        elif opc == 3:
            try:
                qtd = int(input('Quantidade de logs (registros): '))
                gerarArquivo(nome_arq, qtd)
                analisarLogs(nome_arq, qtd)
            except ValueError:
                print('Entrada inválida')

        elif opc == 4:
            print('Até mais')
            break

        else:
            print('Opção inválida')


def gerarArquivo(nome_arq, qtd):
    with open(nome_arq, "w", encoding="UTF-8") as arq:
        for i in range(qtd):
            arq.write(montarLog(i) + "\n")
            print('Log gerado')


def montarLog(i):
    data = gerarData(i)
    ip = gerarIp(i)
    recurso = gerarRecurso(i)
    metodo = gerarMetodo(i)
    status = gerarStatus(i)
    tempo = gerarTempo(i)
    agente = gerarAgente(i)
    protocolo = gerarProtocolo(i)
    tamanho = gerarTamanho(i)

    return f'[{data}] {ip} - {metodo} - {status} - {recurso} - {tempo}ms - {tamanho} - {protocolo} - {agente} - /home'


def gerarData(i):
    base = datetime.datetime.now()
    delta = datetime.timedelta(seconds=i * random.randint(5, 20))
    return (base + delta).strftime('%d/%m/%y %H:%M:%S')


def gerarIp(i):
    if i >= 20 and i <= 50:
        return '203.120.45.7'
    else:
        return f'192.168.0.{random.randint(1, 254)}'


# ============================
# FUNÇÕES AINDA NÃO IMPLEMENTADAS
# (mantidas apenas para o código funcionar)
# ============================

def gerarRecurso(i):
    return '/index.html'


def gerarMetodo(i):
    return 'GET'


def gerarStatus(i):
    return 200


def gerarTempo(i):
    return random.randint(10, 500)


def gerarAgente(i):
    return 'Mozilla/5.0'


def gerarProtocolo(i):
    return 'HTTP/1.1'


def gerarTamanho(i):
    return random.randint(200, 5000)


def analisarLogs(nome_arq, qtd):
    # TODO: implementar análise
    print('Análise ainda não implementada')
