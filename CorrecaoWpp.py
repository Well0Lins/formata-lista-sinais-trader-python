import datetime
from datetime import date
import emoji


def lista_corr():
    lista= input('Cole a correção: \n')
    return lista


def corr(lista):
    if 'Win C/GL 1' in lista:
        lista = lista + emoji.gale + emoji.acerto
    if 'Win C/GL 2' in lista:
        lista = lista + (emoji.gale * 2) + emoji.acerto
    if 'Win S/GL' in lista:
        lista = lista + emoji.acerto
    if 'Loss C/GL 2' in lista:
        lista = lista + (emoji.gale * 2) + emoji.erro
    print(lista)
