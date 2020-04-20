import time
from datetime import datetime
import json
import requests

class FinancialInformation:

    def __init__(self):
        self.result = {
            "symbol": "",
            "Organization": "",
        }

    def getFinanceInformation(self, data):

        #getting data from the request form
        symbol = data.get('symbol')
        getSymbolLink = "https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords=" + symbol + "&apikey=P5AZFTXZ9H1006UX"
        getQuoteLink = "https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=" + symbol + "&apikey=P5AZFTXZ9H1006UX"

        getSymbolResponse = json.loads(
                requests.request("GET", getSymbolLink).text)


        MachingResponse = getSymbolResponse["bestMatches"]
        if (not MachingResponse or
                (MachingResponse and MachingResponse[0]["9. matchScore"] != "1.0000")):
            print("Stock Symbol Not Found")
        else:
            Organization = MachingResponse[0]["2. name"]
            try:
                getQuoteResponse = json.loads(
                    requests.request("GET", getQuoteLink).text)["Global Quote"]
            except:
                print("Failed to connect to Internet to get the Price Quote. Please try again")
            year, month, date = map(str, time.strftime("%Y %m %d").split())
            TimeDate = datetime.today().strftime('%a') + " " + datetime.now(
            ).strftime("%b") + " " + date + " " + str(
                datetime.now().time()) + " " + time.tzname[1] + " " + year

        #assigning the values back to class variables
        self.result["symbol"] = symbol
        self.result["Organization"] = Organization

        return self.result