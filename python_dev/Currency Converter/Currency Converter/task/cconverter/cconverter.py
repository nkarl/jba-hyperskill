# write your code here!
# u = float(input())
# ex = {'RUB':2.98, 'ARS':0.82, 'HNL':0.17, 'AUD':1.9622, 'MAD':0.208}
# for k in ex:
#     print(f'I will get {ex[k] * u} {k} from the sale of {u} conicoins.')
import requests
import json

# take a currency from user input
curr = input()
amount = float(input())

# given the website
site = 'http://www.floatrates.com/daily/'


def make_link(server: str, currency: str):
    return server + currency + '.json'


def request_data(cache: dict, currency: str):
    # make request
    if currency not in cache:
        # load currency's data as python object
        r = requests.get(make_link(site, curr))
        curr_data = json.loads(r.text)
        cache[currency] = [curr_data['usd'], curr_data['eur']]
    return cache


buffer = {}
buffer = request_data(buffer, curr)

