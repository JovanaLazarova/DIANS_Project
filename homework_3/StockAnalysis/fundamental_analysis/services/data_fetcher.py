import requests
import pandas as pd

def fetch_financial_data():
    api_key = "YOUR_API_KEY"
    symbol = "AAPL"
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={api_key}"
    response = requests.get(url)
    data = response.json()

    time_series = data.get("Time Series (Daily)", {})
    dates = []
    prices = []
    for date, metrics in time_series.items():
        dates.append(date)
        prices.append(float(metrics.get("5. adjusted close", 0)))

    df = pd.DataFrame({"Date": dates, "Price": prices})
    return df.sort_values("Date").to_dict(orient="records")