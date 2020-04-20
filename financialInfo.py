import time
from datetime import datetime
import json
import requests

class FinancialInformation:

    def __init__(self):
        self.result = {
            "symbol": "",
            "Organization": "",
            "error": "",
            "TimeDate": "",
            "priceOfStock": "",
            "changeInPrice": "",
            "percentChangeInPrice": "",
        }

    def getFinanceInformation(self, data):

        #getting data from the request form
        symbol = data.get('symbol')
        getSymbolLink = "https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords=" + symbol + "&apikey=P5AZFTXZ9H1006UX"
        getQuoteLink = "https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=" + symbol + "&apikey=P5AZFTXZ9H1006UX"

        getSymbolResponse = json.loads(
                requests.request("GET", getSymbolLink).text)

        try:
            MachingResponse = getSymbolResponse["bestMatches"]
            if (not MachingResponse or
                    (MachingResponse and MachingResponse[0]["9. matchScore"] != "1.0000")):
                error = "Stock Symbol Not Found"
                print(error)
                self.result["error"] = error
                return self.result
            else:
                Organization = MachingResponse[0]["2. name"]
                try:
                    getQuoteResponse = json.loads(
                        requests.request("GET", getQuoteLink).text)["Global Quote"]
                except:
                    error = "Failed to connect to Internet to get the Price Quote. Please try again"
                    print(error)
                    self.result["error"] = error
                    return self.result
                year, month, date = map(str, time.strftime("%Y %m %d").split())
                TimeDate = datetime.today().strftime('%a') + " " + datetime.now(
                ).strftime("%b") + " " + date + " " + str(
                    datetime.now().time()) + " " + time.tzname[1] + " " + year

                changeInPrice = getQuoteResponse["09. change"]
                priceOfStock = getQuoteResponse["05. price"]
                percentChangeInPrice = getQuoteResponse["10. change percent"]
                if int(float(changeInPrice)) > 0:
                    changeInPrice = changeInPrice
                    percentChangeInPrice = percentChangeInPrice
                else:
                    changeInPrice = changeInPrice
                    percentChangeInPrice = percentChangeInPrice
            #assigning the values back to class variables
            self.result["symbol"] = symbol
            self.result["Organization"] = Organization
            self.result["TimeDate"] = TimeDate
            self.result["priceOfStock"] = priceOfStock
            self.result["changeInPrice"] = changeInPrice
            self.result["percentChangeInPrice"] = percentChangeInPrice
            return self.result
        except:
            error = "Please type valid symbol"
            print(error)
            self.result["error"] = error
            return self.result