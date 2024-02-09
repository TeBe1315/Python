from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route('/')
def index():

    return 'This is new project'

@app.route('/exchange', methods=['GET', 'POST'])
def exchange():
    if request.method == 'GET':
        return render_template('exchange.html')
    else:
        currency = 'EUR'
        if 'currency' in request.form:
            currency = request.form['currency']

        ammount = 100
        if 'ammount' is request.form:
            ammount = request.form['ammount']

        return render_template('exchange_result.html', currency=currency, ammount=ammount)

