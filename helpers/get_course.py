import requests

def get_exchange_rates():
    url = "https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        rates = {}
        for currency in data:
            rates[currency['ccy']] = {
                'buy': currency['buy'],
                'sell': currency['sale']
            }

        return rates
    else:
        return None

def format_currency_rate(rate):
    return "{:.2f}".format(float(rate))

def get_dollar_rate():
    data = get_exchange_rates()
    if "USD" in data:
        buy_rate = "{:.2f}".format(float(data['USD']['buy']))
        sell_rate = "{:.2f}".format(float(data['USD']['sell']))
        return f"$: {buy_rate}, {sell_rate}"
    else:
        return "Dollar rate not available"

def get_euro_rate():
    data = get_exchange_rates()
    if "EUR" in data:
        buy_rate = "{:.2f}".format(float(data['EUR']['buy']))
        sell_rate = "{:.2f}".format(float(data['EUR']['sell']))
        return f"€: {buy_rate}, {sell_rate}"
    else:
        return "Euro rate not available"