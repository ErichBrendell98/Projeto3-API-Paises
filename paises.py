import json

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


def contagem_paises(lista_paises):
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
                print(f'{pais["name"]}: {pais["population"]}')
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

if __name__ == '__main__':
    # mostrar_populacao('portugal')
    mostrar_moedas('bra')