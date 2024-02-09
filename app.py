from flask import Flask, render_template, url_for, request

app = Flask(__name__)

class Currency:

    def __init__(self, code, name, flag):
        self.code = code
        self.name = name
        self.flag = flag

    def __repr__(self):
        return '<Currency {}>'.format(self.code)

class CantorOffer:
    def __init__(self):
        self.currencies = []

    def load_offer(self):
        self.currencies.append(Currency('USD', 'Dollar', 'dollar.jpg'))
        self.currencies.append(Currency('EUR', 'Euro', 'euro.jpg'))
        self.currencies.append(Currency('YEN', 'YEN', 'jen.jpg'))

    def get_by_code(self, code):
        for currency in self.currencies:
            if currency.code == code:
                return currency
        return Currency('unknow', 'unknow', 'pirat.jpg')

@app.route('/')
def index():

    return 'This is new project'

@app.route('/exchange', methods=['GET', 'POST'])
def exchange():

    offer = CantorOffer()
    offer.load_offer()

    if request.method == 'GET':
        return render_template('exchange.html', offer=offer)
    else:
        currency = 'EUR'
        if 'currency' in request.form:
            currency = request.form['currency']

        ammount = 100
        if 'ammount' is request.form:
            ammount = request.form['ammount']

        return render_template('exchange_result.html', currency=currency, ammount=ammount,
                               currency_info=offer.get_by_code(currency))

