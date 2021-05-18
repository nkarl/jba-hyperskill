# write your code here!
# u = float(input())
# ex = {'RUB':2.98, 'ARS':0.82, 'HNL':0.17, 'AUD':1.9622, 'MAD':0.208}
# for k in ex:
#     print(f'I will get {ex[k] * u} {k} from the sale of {u} conicoins.')
import requests, json

# website to request exchange rate
site = 'http://www.floatrates.com/daily/'


my_code = input()  # my currency I have


def makeLink(server: str, code: str):
    """compose the link to the server with the currency code
    """
    return server + code + '.json'


def calc_exchange(cache: dict, code: str, amount: float):
    return cache[code]['rate'] * amount


# request data for my currency
r = requests.get(makeLink(site, my_code))

# load the json text into Python data structure
curr_data = json.loads(r.text)

my_cache = dict()
if my_code == 'usd':
    my_cache['eur'] = curr_data['eur']
elif my_code == 'eur':
    my_cache['usd'] = curr_data['usd']
else:
    my_cache['usd'] = curr_data['usd']
    my_cache['eur'] = curr_data['eur']

while True:
    my_target = input()
    if len(my_target) < 1:
        break
    my_amount = input()
    if len(my_amount) < 1:
        break
    my_amount = float(my_amount)

    ex_amount = 0
    print('Checking the cache...')
    if my_target in my_cache:
        print('Oh! It is in the cache!')
        ex_amount = calc_exchange(my_cache, my_target, my_amount)
    else:
        print('Sorry, but it is not in the cache!')
        r = requests.get(makeLink(site, my_code))
        curr_data = json.loads(r.text)
        my_cache[my_target] = curr_data[my_target]
        ex_amount = calc_exchange(my_cache, my_target, my_amount)

    print(f'You received {round(ex_amount, 2)} {my_target.upper()}')
