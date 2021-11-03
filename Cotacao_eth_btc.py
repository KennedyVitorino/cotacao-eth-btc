import json
from time import sleep
import requests


def cotacao_eth_btc():
    print('\n+-------+-------+-------+-------+--------+ \n'
          f'|    --> Cotação \033[1;94mBITCOIN\033[m para BRL <--    | \n'
          f'+-------+-------+-------+-------+--------+ \n'
          f'|    --> Cotação \033[1;95mETHEREUM\033[m para BRL <--   | \n'
          f'+-------+-------+-------+-------+--------+ \n')

    criptoMoeda = input('BCT ou ETH?').upper().strip()

    while True:
        api = requests.get(url=f'https://www.mercadobitcoin.net/api/{criptoMoeda}/ticker/')
        json_data = json.loads(api.text)

        api = float(json_data['ticker']['last'])
        apiLow = float(json_data['ticker']['low'])
        apiHigh = float(json_data['ticker']['high'])
        sleep(0.8)

        print('+-----------+-----------+-----------+ \n'
              f'|                                   |'
              f'\n| Cotação atual:...... R${api:.2f}   |\n'
              f'| Menor preço:........ R${apiLow:.2f}   |\n'
              f'| Maior preço:........ R${apiHigh:.2f}   |\n'
              f'|                                   |\n'
              '+-----------+-----------+-----------+')


cotacao_eth_btc()
