""" Practice with BeautifulSoup"""
from bs4 import BeautifulSoup

with open("website.html", encoding="utf-8") as file:
    contents = file.read()

# entire soup object represents the entire html file
soup = BeautifulSoup(contents, "html.parser")
# print(soup.prettify())

# print(soup.li) will print the first li tag
# print(soup.find_all(name="li")) will print all li tags
# print(soup.find_all(name="li")[1]) will print the second li tag
# print(soup.find(name="h1", id="name")) will print the h1 tag with id="name"
# all anchor tags = soup.find_all(name="a")
# for tag in all_anchor_tags:
#   print(tag.getText()) will print all the text in the anchor tags

# finding an anchor tag inside a paragraph tag; select by css selector
anchor = soup.select_one(selector="p a")
print(anchor)

# select by id
name = soup.select_one(selector="#name")
print(name)

# select by class
headings = soup.select(".heading")
print(headings)
