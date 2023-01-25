import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com/")
website = response.text

soup = BeautifulSoup(website, "html.parser")

article_texts = []
article_links = []


titles = soup.find_all("span", "titleline")
for title in titles:
    new_title = title.find_next("a")
    title_name = new_title.getText()
    article_texts.append(title_name)
    title_link = new_title.get("href")
    article_links.append(title_link)

article_scores = [int(score.getText().split()[0]) for score in soup.find_all("span", "score")]


max_index = article_scores.index(max(article_scores))
print(article_texts[max_index])
print(article_links[max_index])
print(article_scores[max_index])

