
# now i am going to create a project wich has sent the main to me that price is hight
import  bs4

import urllib.request

import smtplib

from bs4 import BeautifulSoup

url = 'https://www.amazon.in/FancyDressWale-Halloween-Inflatable-Tyrannosaurus-Performance/dp/B085RGBGLC/ref=sr_1_1?crid=1WFJNKSGHPAGC&dchild=1&keywords=dinosaur+costume+for+adults&qid=1594392785&sprefix=dinasour+costime%2Caps%2C292&sr=8-1'

sauce = urllib.request.urlopen(url).read()
soup = bs4.BeautifulSoup(sauce, "html.parser")

prices = soup.find(id="corePrice_desktop").get_text()
prices = float(prices.replace(",", "").replace("₹", ""))
print(prices)



