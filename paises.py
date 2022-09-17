import requests 

URL_ALL = 'https://restcountries.com/v3.1/all'
URL_NAME = 'https://restcountries.com/v3.1/name/brazil'

resposta_all = requests.get(URL_ALL)
resposta_name = requests.get(URL_NAME)

print(f'{resposta_all}')
print(f'{type(resposta_all)}')

print(f'{resposta_name}')
print(f'{type(resposta_name)}')
print(f'{resposta_name.text}')
