from symtable import Symbol
from binance.client import Client
from cripto_test_data import api_key_test, secret_key_test
from time import sleep
from binance import ThreadedWebsocketManager

# ws_client = WebsocketClient(stream_url='wss://testnet.binance.vision')

# client = Client(base_url='https://testnet.binance.vision',  key=api_key_test, secret=secret_key_test)
# print(client.time())
# print(client.account_status())


# base_url='https://testnet.binance.vision'
client = Client(api_key_test,secret_key_test, testnet= True)

# # Get account information
# print(client.account())

# # Get asset balance
# user_coin = 'busd'
# farm_coin = 'btc'
# def get_asset_balance(assets = [farm_coin,user_coin]):
#     asset_balance = {asset:client.get_asset_balance(asset) for asset in assets}
#     return asset_balance

# print(get_asset_balance())

farm_pair = 'BTCUSDT'
# # Get market prices
# def get_market_price(pair=farm_pair):
#     last_price = client.get_symbol_ticker(symbol=pair)
#     return last_price

# print(get_market_price())

# Info about pair
# info = client.get_symbol_info('BTCUSDT')
# print(info)

# # Place sell order to binance
# def placeSellOrder(percent = 0.1, coin=farm_coin, pair=farm_pair):
#     quantity = float((get_asset_balance().get(coin)).get('free')) * percent
#     sell_order = client.create_test_order(symbol=pair, side='SELL', type='MARKET', quantity=quantity)
#     return sell_order
# print(placeSellOrder())
# print(get_asset_balance())