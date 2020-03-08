# Alpha Vantage API Key C5XOWJ3QMQVSFQD1

import urllib.request
import json 


#Q 1 ANS 
def getStockData(st_symbol):
    #To make the request across the Internet
    url = 'https://www.alphavantage.co/query'
    funct = 'TIME_SERIES_DAILY'
    symbol = st_symbol
    apikey = 'C5XOWJ3QMQVSFQD1'
    ### 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=AAPL&apikey=C5XOWJ3QMQVSFQD1'

    completeURL = url + '?function=' + funct + '&symbol=' + symbol + '&apikey=' + apikey

    connection = urllib.request.urlopen(completeURL)

    responseString = connection.read().decode()

    # JSON-formatted response-string
    return responseString



#getStockData('AAPL')
        

# Q 2 Main Method
def main():
    fileWrite = open('japi.out', 'w')
    #asks the user for a stock symbol until user enters quit
    while True:

        inputVal = input('\nEnter Stock Symbol OR Enter QUIT to Exit: ')

        if inputVal == 'quit' or inputVal == 'QUIT':    
            print(':::::::: THANKS ::::::')
            break
        else:
            jsonString = getStockData(inputVal)
            
            # Convert the response from JSON to Python dictionary
            objDict = json.loads(jsonString) # returns Python dictionary

            print(':::::::::::JSON Formated  response ::::::::::::::::\n\n' , objDict)
            stockPrice = objDict['Time Series (Daily)']
            for key in stockPrice:
                if key in stockPrice:       # getting latest(top one) stock price
                    latestPrice = stockPrice[key]['4. close']
                    break
                
            print('\n\n!!!!!!!!!!! CURRENT PRICE   !!!!!!!!!!')
            priceOutput = 'The current price of ' + inputVal.upper() +' is: ' + latestPrice + '\n'
            fileWrite.write(priceOutput)   #write to file

            print(priceOutput)
    fileWrite.close()


if __name__== "__main__":    
    main()




