import requests
import json


def stock_data(stock_symbol):
    # Use the requests library to make a GET request to the Alpha Vantage API
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={stock_symbol}&apikey=56HHQ94E7AC0CFXM"
    response = requests.get(url)
    data = json.loads(response.text)

    # Extract the most recent data from the response
    latest_data = data['Time Series (Daily)'][list(data['Time Series (Daily)'].keys())[0]]

    # Print the data to the user
    print(f"Stock Symbol: {stock_symbol}")
    print(f"Latest Open: ${latest_data['1. open']}")
    print(f"Latest Close: ${latest_data['4. close']}")
    print(f"Latest High: ${latest_data['2. high']}")
    print(f"Latest Low: ${latest_data['3. low']}")


# Ask the user for a stock symbol
stock_symbol = input("Enter a stock symbol: ")

# Call the stock_data function with the user's input
stock_data(stock_symbol.upper())
