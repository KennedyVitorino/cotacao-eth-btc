import json
from time import sleep
import requests


def cotacao_eth_btc():
    print('\n+------+-------+-------+-------+-------+ \n'
          f'|    -> Cotação \033[1;94mBITCOIN\033[m para BRL <-    | \n'
          f'+-------+-------+-------+-------+------+ \n'
          f'|    -> Cotação \033[1;95mETHEREUM\033[m para BRL <-   | \n'
          f'+------+-------+-------+-------+-------+ \n')

    cripto_moeda = input('BCT ou ETH?').strip()

    while True:
        usdbrl = requests.get(url=f'http://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL')
        json_data_ = json.loads(usdbrl.text)

        btc_eth = requests.get(url=f'https://www.mercadobitcoin.net/api/{cripto_moeda}/ticker/')
        json_data_btc_eth = json.loads(btc_eth.text)

        api_usdbrl = float(json_data_['USDBRL']['bid'])
        api_eurbrl = float(json_data_['EURBRL']['bid'])

        api = float(json_data_btc_eth['ticker']['last'])
        api_low = float(json_data_btc_eth['ticker']['low'])
        api_high = float(json_data_btc_eth['ticker']['high'])
        # sleep(0.5)

        print(f'Preço atual do dolar convertido em real US${api_usdbrl:.2f} \n'
              f'Preço atual do euro convertido em real Є{api_eurbrl:.2f}')

        print('+-----------+-----------+------------+ \n'
              f'|                                    |'
              f'\n| Cotação atual:...... R${api:.2f}   |\n'
              f'| Menor preço:........ R${api_low:.2f}   |\n'
              f'| Maior preço:........ R${api_high:.2f}   |\n'
              f'|                                    |\n'
              '+-----------+-----------+------------+')
        break


cotacao_eth_btc()
