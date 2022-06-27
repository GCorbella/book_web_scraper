import requests
import bs4

base_url = "http://books.toscrape.com/catalogue/page-{}.html"

for n in range(1,51):
    print(base_url.format(n))