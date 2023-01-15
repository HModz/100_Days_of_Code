import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

stock_api_key = "1F7ARR0ZHT6YTO83"
stock_api_url = "https://www.alphavantage.co/query"
stock_parameters = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": stock_api_key
}

news_api_key = "f95d02d83afb4f00ba3ff1e2703c1b8b"
news_api_url = "https://newsapi.org/v2/everything"
news_parameters = {
    "q": COMPANY_NAME,
    "apiKey": news_api_url
}

response = requests.get(url=stock_api_url, params=stock_parameters)
response.raise_for_status()
data = response.json()
today_date = list(data["Time Series (Daily)"])[0]
yesterday_date = list(data["Time Series (Daily)"])[1]

today_price = data["Time Series (Daily)"][today_date]["4. close"]
yesterday_price = data["Time Series (Daily)"][yesterday_date]["4. close"]

change = (float(today_price)-float(yesterday_price))/float(today_price)*100
print(round(change,2))

if change >= 5 or change <= -5:
    print("Get News")

    response_news = requests.get(url=news_api_url, params=news_parameters)
    response_news.raise_for_status()
    news_data = response_news.json()
    print(news_data)





#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

