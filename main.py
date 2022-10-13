# FORMATADOR DE LISTAS DE SINAIS PARA WHATSAPP

import ListaWpp
import emoji
import CorrecaoWpp

while True:
    escolha = input('Escolha a opção {1} para formatar a (LISTA DE SINAIS), {2} para formatar a (CORREÇÃO) '
                    'ou {3} para sair do programa: ')

    if escolha == '1':
        lista = ListaWpp.nome_lista()
        print(f'{emoji.fogo * 2}LISTA DE SINAIS{emoji.fogo * 2}')
        print(f'{emoji.tempo * 2}{ListaWpp.tempo_vela(lista)}{emoji.tempo * 2}'.rjust(17))
        if ListaWpp.otc() >= 5:
            print(f'{emoji.fogo * 2}OTC{emoji.fogo * 2}'.rjust(17))
        print()
        print(f'{emoji.data}DATA{emoji.data}'.rjust(24))
        ListaWpp.hora()
        print()
        ListaWpp.format_lista(lista)

    if escolha == '2':
        correcao = CorrecaoWpp.lista_corr()

    if escolha == '3':
        exit()

    else:
        print('ESCOLHA UMA DAS OPÇÕES')
