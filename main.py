from flask import Flask, request, render_template
from financialInfo import FinancialInformation
app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def home():
    result = ''
    if (request.method == 'GET'):
        return render_template('LandingPage.html')
    else:
        result = FinancialInformation().getFinanceInformation(request.form)
        return render_template('ResultPage.html', result=result)

if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True)
