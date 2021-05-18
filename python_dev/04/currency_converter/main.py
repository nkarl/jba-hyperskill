"""my wip vim-editor currency converter, jb feels a little too overwhelming.

GOAL: I have my currency, an amount. I want to convert it to a target currency.

    - First, read the currency to exchange (my_code)
    - Second, read the currency I might exchage my money for (target_code)
    - Third, my amount of money (float)

    So, the first input is taken only once. The second and third inputs might recur.

"""
import requests, json

# website to request exchange rate
site = 'http://www.floatrates.com/daily/'


my_code = input('Enter the currency code in your possession:')  # my currency I have


def get_target_code():
    return input('Enter your target currency code:')  # my target currency for exchange


def get_my_amount():
    return float(input('Enter the amount of money you have:'))  # the amount of money I have for exchange


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


my_amount = get_my_amount()
my_target = get_target_code()
while my_amount != "" or my_target != "":
    ex_amount = calc_exchange(curr_data, my_target, my_amount)
    print(f'You received {ex_amount} {my_target.upper()}')
    my_amount = get_my_amount()
    my_target = get_target_code()
