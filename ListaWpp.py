import datetime
from datetime import date
import emoji


def nome_lista():
    nome_arq = input('Nome do arquivo: ')
    return nome_arq


def dia_lista(lista):
    dia_dir = lista[21:23] + '.' + lista[18:20]
    return dia_dir


def Dir_Lista(lista):
    d = 'W://SINAIS/LISTAS/'  # diretorio da lista
    dir = d + dia_lista(lista) + '/' + lista + '.txt'
    return dir


def hora():
    data = datetime.date.today()
    data_format = '{} / {} / {}'.format(data.day, data.month, data.year)
    print(f'{data_format.rjust(29)}')


def tempo_vela(lista):
    temp = lista[26:]
    return temp


def otc():
    num = date.today().weekday()
    return int(num)


def format_lista(lista):
    with open(Dir_Lista(lista), 'r', encoding='UTF-8') as arq:
        texto = arq.read()
        palavras = texto.split('\n')
        for palavra in palavras:
            col1 = (palavra[0:5])
            col2 = (palavra[6:12])
            col3 = (palavra[13:17])

            if 'OTC' in col3:
                col3 = (palavra[17:21])
            if ',' in col3:
                col3 = col3[:-1]

            if 'CALL' in col3:
                col3 = col3 + emoji.verde
            else:
                col3 = col3 + ' ' + emoji.vermelho

            print(f'{col1:<8} {col2:^8} {col3:>8}')
