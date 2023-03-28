import requests
import json


def stock_data(stock_symbol):
    # Use the alphaAvantage API to get stock data
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={stock_symbol}&apikey=56HHQ94E7AC0CFXM"
    response = requests.get(url)
    data = json.loads(response.text)

    # get most recent stock data
    latest_data = data['Time Series (Daily)'][list(data['Time Series (Daily)'].keys())[0]]

    # Print stock info
    print(f"Stock Symbol: {stock_symbol}")
    print(f"Latest Open: ${latest_data['1. open']}")
    print(f"Latest Close: ${latest_data['4. close']}")
    print(f"Latest High: ${latest_data['2. high']}")
    print(f"Latest Low: ${latest_data['3. low']}")


# ask user for stock
stock_symbol = input("Enter a stock symbol: ")

#retrieve stock inputed by user
stock_data(stock_symbol.upper())
