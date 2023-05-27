import json  # ler as informçãoes consumidas através do URL
import requests  # para consumir url externo
from time import sleep

print('\n+------+-------+-------+-------+-------+ \n'
      f'|    -> Cotação \033[1;94mBITCOIN\033[m para BRL <-    | \n'
      f'+-------+-------+-------+-------+------+ \n'
      f'|    -> Cotação \033[1;95mETHEREUM\033[m para BRL <-   | \n'
      f'+------+-------+-------+-------+-------+ \n')

# modalidade - 1 2 3
criptomoeda = input('BITCOIN ou ETHEREUM:').upper().strip()
modalidade = input("""Escolha o que você deseja Monitorar
(1) Venda | (2) Compra | (3) Venda e compra: """)

resultado = requests.get(url=f'https://www.mercadobitcoin.net/api/{criptomoeda}/ticker/')
json_data = json.loads(resultado.text)  # converter o resultado em texto
resultado = json_data['ticker']['last']
print(f'\nValor atual do {criptomoeda}: {resultado} ')

if modalidade == '3':
    compra = input(f'\nPor quanto você deseja comprar o {criptomoeda}? Ex: {resultado} ')
    venda = input(f'Por quanto você deseja vender o {criptomoeda}? Ex: {resultado} ')

    while True:
        resultado = requests.get(url=f'https://www.mercadobitcoin.net/api/{criptomoeda}'
                                     f'/ticker/')
        json_data = json.loads(resultado.text)  # converter o resultado em texto
        resultado = json_data['ticker']['last']
        print(f'{resultado}')
        sleep(1.5)

        # quando o resultado for maior ou igual ao valor digitado ele enviará mensagem de
        # vender
        if compra >= resultado:
            print('\n$$$ Hora de comprar ativos! $$$$')
            break

        if venda <= resultado:  # quando a compra for maior ou igual ao valor digitado
            # ele enviará mensagem de comprar
            print('\n$$$$ Hora de vender seus ativos $$$$')
            break

elif modalidade == '2':
    compra = input(f'\nPor quanto você deseja comprar o {criptomoeda}? Ex: {resultado} ')

    while True:
        resultado = requests.get(url=f'https://www.mercadobitcoin.net/api/{criptomoeda}'
                                     f'/ticker/')
        json_data = json.loads(resultado.text)  # converter o resultado em texto
        resultado = json_data['ticker']['last']
        print(f'{resultado}')
        sleep(1.5)

        # quando o resultado for maior ou igual ao valor digitado ele enviará mensagem
        # de vender
        if compra >= resultado:
            print(f'\nHora de vender seus ativos à {resultado}')  #
            break
else:
    venda = input(f'\nPor quanto você deseja seu vender o {criptomoeda} Ex: {resultado} ')

    while True:
        resultado = requests.get(url=f'https://www.mercadobitcoin.net/api/{criptomoeda}'
                                     f'/ticker/')
        json_data = json.loads(resultado.text)  # converter o resultado em texto
        resultado = json_data['ticker']['last']
        print(f'{resultado}')
        sleep(1.5)

        if venda <= resultado:
            print(f'\nHora de vender seus ativos à {resultado}')
            break
