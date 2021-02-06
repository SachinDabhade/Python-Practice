# Python program to convert the currency
# of one country to that of another country

# Import the modules needed
import requests


class Currency_convertor:
    # empty dict to store the conversion rates
    rates = {}
    url = 'http://data.fixer.io/api/latest? access_key = 2eef63f3c766614c4f4ccf4d4e34e759'
    def __init__(self, url):
        data = requests.get(url).json()
        print(data)

        # Extracting only the rates from the json data
        self.rates = data["rates"]
        print(self.rates)
    # function to do a simple cross multiplication between
    # the amount and the conversion rates
    def convert(self, from_currency, to_currency, amount):
        initial_amount = amount
        if from_currency != 'EUR':
            amount = amount / self.rates[from_currency]

        # limiting the precision to 2 decimal places
        amount = round(amount * self.rates[to_currency], 2)
        print('{} {} = {} {}'.format(initial_amount, from_currency, amount, to_currency))

url = 'http://data.fixer.io/api/latest? access_key = 2eef63f3c766614c4f4ccf4d4e34e759'
# Driver code
if __name__ == "__main__":
    # YOUR_ACCESS_KEY = 'GET YOUR ACCESS KEY FROM fixer.io'
    url = str.__add__(url=url)
    c = Currency_convertor(url)
    from_country = input("From Country: ")
    to_country = input("TO Country: ")
    amount = int(input("Amount: "))
    c.convert('EUR', 'INR', 100)