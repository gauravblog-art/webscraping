from bs4.element import Tag
import requests


from bs4 import BeautifulSoup

url='https://www.rosettacode.org/wiki/Web_scraping'

r=requests.get(url)

# print(content)


# step 1
htmlcontent=r.content

# print(htmlcontent)

# srep 2 passe the html

soup=BeautifulSoup(htmlcontent, 'html.parser')

# print(soup.prettify())

# step 3 HTML tree traverser
title=soup.title

print(type(title))

# types of object

# 1.tag
# 2.Navigation
# 3.beautfulshoup
# 4.comment

# print(type(soup))

# print(type(title))
# print(type(title.string)) 

# 1. get all paragraph

par=soup.find_all('p')

print(par.priti)

# 1.get all ancher Tag
acn= soup.find_all('a')

print(acn.prettify())