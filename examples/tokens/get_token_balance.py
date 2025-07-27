from etherscan.tokens import Tokens
import json

with open('../../api_key.json', mode='r') as key_file:
    key = json.loads(key_file.read())['key']

address = '0x4f19f6f747f43a3d9fcf8bb7d2214e798cd2ece8'
api = Tokens(contract_address='0xdAC17F958D2ee523a2206206994597C13D831ec7',
             api_key=key)
balance = api.get_token_balance(address=address)
print(balance)
