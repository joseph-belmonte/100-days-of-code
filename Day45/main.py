"""scarping empire top 100 movies"""
from bs4 import BeautifulSoup
import requests
import re
import pprint

URL = "https://web.archive.org/web/20200518055830/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL, timeout=5)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

all_movies = soup.find_all(name="h3", class_="title")

movie_titles = [movie.getText() for movie in all_movies]
movies = movie_titles[::-1]

with open("movies.txt", mode="w", encoding="utf-8") as file:
    for movie in movies:
        file.write(f"{movie}\n")
