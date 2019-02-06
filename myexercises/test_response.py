import requests

response = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=5min&apikey=demo")
jsonvalue = response.json()
timeseries = jsonvalue["Time Series (5min)"]


# print(timeseries)
# this was tested in the Debugger : [timeseries[list(timeseries.keys())[i]]["4. close"] for i in range(0,10)]

print([timeseries[list(timeseries.keys())[i]]["4. close"] for i in range(0,10)])


# ignore
