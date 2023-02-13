import requests
from twilio.rest import Client
import os
from datetime import date, datetime, timedelta

STOCK = "TSLA"
COMPANY_NAME = '"Tesla Inc"'
AV_API_KEY = "S3QUCNT4CBZDNW1F"
NEWS_API_KEY = "58bbba686d564e2ca6b5b8dfde03c71a"
TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACC_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")

# gets stock info
stock_parameters = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "outputsize": "compact",
    "datatype": "json",
    "apikey": AV_API_KEY
}
stock_response = requests.get(url="https://www.alphavantage.co/query?", params=stock_parameters)
stock_response.raise_for_status()
stock_data = stock_response.json()

# sets appropriate days to check (market is closed on weekends, so this is needed to make sure that code doesn't brick
# due to insufficient data
today = datetime.now().weekday()
if today == 0:
    yesterday = date.today() - timedelta(days=3)
    day_bf_yest = date.today() - timedelta(days=4)
elif today == 1:
    yesterday = date.today() - timedelta(days=1)
    day_bf_yest = date.today() - timedelta(days=4)
else:
    yesterday = date.today() - timedelta(days=1)
    day_bf_yest = date.today() - timedelta(days=2)

# converts object to string for later use
yesterday = yesterday.strftime("%Y-%m-%d")
day_bf_yest = day_bf_yest.strftime("%Y-%m-%d")

# find princes and do comparisons
yesterday_price = float(stock_data["Time Series (Daily)"][yesterday]["4. close"])
day_bf_yest_price = float(stock_data["Time Series (Daily)"][day_bf_yest]["4. close"])
change_in_price = yesterday_price/day_bf_yest_price
percent_change = round(((change_in_price - 1)*100), 2)

# set symbol to indicate if the market is up or down
if percent_change <= 0:
    symbol = "⬇️"
else:
    symbol = "⬆️"
# set var to absolute value to display later
percent_change = abs(percent_change)

# get 3 news articles about the stock
if percent_change >= 5:
    news_parameters = {
        "apiKey": NEWS_API_KEY,
        "q": f"+{COMPANY_NAME} OR +{STOCK}",
        "searchin": "title",
        "language": "en",
        "sortBy": "publishedAt",
        "pageSize": "3",
    }
    news_response = requests.get(url="https://newsapi.org/v2/everything?", params=news_parameters)
    news_response.raise_for_status()
    news_data = news_response.json()

# Text me a message with the stock change percentage and the 3 news articles' titles and descriptions.

    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        messaging_service_sid="MG176ecd1c5b7005f70414d270ddce923f",
        body=f"TSLA: {symbol} {percent_change}%\n\nHeadline: {news_data['articles'][0]['title']}\n\n"
             f"Brief: {news_data['articles'][0]['description']}\n\nHeadline: {news_data['articles'][1]['title']}\n\n"
             f"Brief: {news_data['articles'][1]['description']}\n\nHeadline: {news_data['articles'][2]['title']}\n\n"
             f"Brief: {news_data['articles'][2]['description']}\n\n",
        to="+14097671924",
    )
    print(message.status)
