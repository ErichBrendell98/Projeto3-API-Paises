from curses import noecho
import json
import sys

import requests

URL_ALL = 'https://restcountries.com/v2/all'
URL_NAME = 'https://restcountries.com/v2/name/'


def requisicao(url):
    try:
        resposta = requests.get(url)
        if resposta.status_code == 200:
            return resposta.text
    except:
        print('Erro ao fazer requisição em:', url)


def parsing(texto_resposta):
    try:
        return json.loads(texto_resposta)
    except:
        print('Erro ao fazer parsing')


def contagem_paises():
    resposta = requisicao(URL_ALL)
    if resposta:
        lista_paises = parsing(resposta)
        if lista_paises:
            return len(lista_paises)


def listar_paises(lista_paises):
    for pais in lista_paises:
        print(pais['name'])


def mostrar_populacao(nome_pais):
    resposta = requisicao(f'{URL_NAME}/{nome_pais}')
    if resposta:
        lista_paises = parsing(resposta)
        if lista_paises:
            for pais in lista_paises:
                print(f'{pais["name"]}: {pais["population"]} habitantes')
    else:
        print('País não encontrado')


def mostrar_moedas(nome_pais):
    resposta = requisicao(f'{URL_NAME}/{nome_pais}')
    if resposta:
        lista_paises = parsing(resposta)
        if lista_paises:
            for pais in lista_paises:
                print(f'Moedas de {pais["name"]}:')
                moedas = pais['currencies']
                for moeda in moedas:
                    print(f'{moeda["name"]} - {moeda["code"]}')
    else:
        print('País não encontrado')


def ler_nome_pais():
    try:
        nome_pais = sys.argv[2]
        return nome_pais
    except:
        print('É preciso passar o nome do país')


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('### Bem vindo ao sistema de paises ###')
        print('Uso: python paises.py <acao> <nome_pais>')
        print('Ações disponíveis: contagem, moeda, populacao')
    else:
        argumento1 = sys.argv[1]
        
        if argumento1 == 'contagem':
            numero_paises = contagem_paises()
            print(f'Existem {numero_paises} países no mundo todo')
        elif argumento1 == 'moeda':
            pais = ler_nome_pais()
            if pais:
                mostrar_moedas(pais)
        elif argumento1 == 'populacao':
            pais = ler_nome_pais()
            if pais:
                mostrar_populacao(pais)
        else:
            print('Argumento inválido')
