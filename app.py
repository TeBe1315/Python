from flask import Flask, render_template, url_for, request, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SNC'

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
        self.denied_codes = []

    def load_offer(self):
        self.currencies.append(Currency('USD', 'Dollar', 'flag_dollar.jpg'))
        self.currencies.append(Currency('EUR', 'Euro', 'flag_euro.jpg'))
        self.currencies.append(Currency('YEN', 'YEN', 'flag_jen.jpg'))
        self.denied_codes.append('USD')

    def get_by_code(self, code):
        for currency in self.currencies:
            if currency.code == code:
                return currency
        return Currency('unknow', 'unknow', 'flag_pirat.jpg')

@app.route('/')
def index():

    return render_template('index.html')

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

        if currency in offer.denied_codes:
            flash('This currency {} cannot be accepted'.format(currency))
        elif offer.get_by_code(currency) == 'unknow':
            flash('This selected currency is unknow and be cannot be accepted')
        else:
            flash('Request to exchenge {} was accepted'. format(currency))
        ammount = 100
        if 'ammount' is request.form:
            ammount = request.form['ammount']

        return render_template('exchange_result.html', currency=currency, ammount=ammount,
                               currency_info=offer.get_by_code(currency))

