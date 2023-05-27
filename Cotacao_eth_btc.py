import json
from time import sleep
import requests


def cotacao_eth_btc():
    print('Cotação do BITCOIN e do ETHEREUM')
    print()
    
    cripto_moeda = input('BCT ou ETH?').strip()

    while True:
        usd_brl = requests.get(url=f'https://economia.awesomeapi.com.br/json/last/USD'
                                   f'-BRL,EUR-BRL')
        json_data_ = json.loads(usd_brl.text)

        btc_eth = requests.get(url=f'https://www.mercadobitcoin.net/api/{cripto_moeda}'
                                   f'/ticker/')
        json_data_btc_eth = json.loads(btc_eth.text)

        api_usd_brl = float(json_data_['USDBRL']['bid'])
        api_eur_brl = float(json_data_['EURBRL']['bid'])

        api = float(json_data_btc_eth['ticker']['last'])
        api_low = float(json_data_btc_eth['ticker']['low'])
        api_high = float(json_data_btc_eth['ticker']['high'])
        sleep(0.5)

        print()
        print(f'Dólar para BRL em tempo real R$ {api_usd_brl:.2f}')
        print(f'Euro para BRL em tempo real R$ {api_eur_brl:.2f}')

        print()
        print('PREÇO ATUAL DO ETHERUM')
        print(f'Cotação atual:...... R${api:.2f}')
        print(f'Menor preço:........ R${api_low:.2f}')
        print(f'Maior preço:........ R${api_high:.2f}')
        break


cotacao_eth_btc()
