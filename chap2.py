from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html, "html.parser")

nameList = bsObj.findAll("span", {"class":"green"})
for name in nameList:
    print(name.get_text())

html2 = urlopen("http://pythonscraping.com/pages/page3.html")
bsObj2 = BeautifulSoup(html2, "html.parser")

for child in bsObj2.find("table",{"id":"giftList"}).children:
    print(child)

for sibling in bsObj2.find("table", {"id":"giftList"}).tr.next_siblings:
    print(sibling)

print(bsObj2.find("img", {"src":"../img/gifts/img1.jpg"}).parent.previous_sibling.get_text())

images = bsObj2.findAll("img", {"src":re.compile("\.\.\/img\/gifts/img.*\.jpg")})
for image in images:
    print(image["src"])

print(bsObj2.findAll(lambda tag: len(tag.attrs) == 2))