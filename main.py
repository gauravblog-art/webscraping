import requests

from bs4 import BeautifulSoup

url='https://www.rosettacode.org/wiki/Web_scraping'

r=requests.get(url)

# print(content)

htmlcontent=r.content

print(htmlcontent)