"""scrape ycombinator"""
from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news", timeout=5)
html = response.text

# want to get the top 30 articles, article title, link, and points
soup = BeautifulSoup(html, "html.parser")
articles = soup.select(selector=".titleline a")

article_texts = []
article_links = []

for article in articles:
    article_text = article.getText()
    article_texts.append(article_text)
    article_link = article.get("href")
    article_links.append(article_link)


article_upvotes = [
    int(score.getText().split()[0])
    for score in soup.find_all(name="span", class_="score")
]
most_upvoted_index = article_upvotes.index(max(article_upvotes))

print(article_texts[most_upvoted_index])
print(article_links[most_upvoted_index])
print(article_upvotes[most_upvoted_index])
