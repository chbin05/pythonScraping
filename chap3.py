from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import ssl
import re
random.seed(datetime.datetime.now())
ssl._create_default_https_context = ssl._create_unverified_context

pages = set()
def getLinks(pageUrl):
    global pages
    html = urlopen("https://en.wikipedia.org" + pageUrl)
    bsObj = BeautifulSoup(html, "html.parser")
    try:
        print(bsObj.h1.get_text())
        print(bsObj.find(id="mw-content-text").findAll("p")[0].encode("utf-8")) # window에서 인코딩 문제가 있어서 encode를 추가함
        print(bsObj.find(id="ca-edit").find("a").attrs['href'])
    except AttributeError:
        print("error")
    for link in bsObj.findAll("a", href=re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                # 새 페이지 발견
                newPage = link.attrs['href']
                print("-------\n" + newPage)
                pages.add(newPage)
                getLinks(newPage)

getLinks("")


# def getLinks(articleUrl):
#     html = urlopen("https://en.wikipedia.org" + articleUrl)
#     bsObj = BeautifulSoup(html, "html.parser")
#     return bsObj.find("div", {"id":"bodyContent"}).findAll("a",href=re.compile("^(/wiki/)((?!:).)*$"))
#
# links = getLinks("/wiki/Kevin_Bacon")
# print(len(links))
#
# while len(links) > 0:
#     newArticle = links[random.randint(0, len(links) - 1)].attrs["href"]
#     print(newArticle)
#     links = getLinks(newArticle)


# html = urlopen("https://en.wikipedia.org/wiki/Kevin_Bacon")
# bsObj = BeautifulSoup(html, "html.parser")
# for link in bsObj.find("div", {"id":"bodyContent"}).findAll("a",href=re.compile("^(/wiki/)((?!:).)*$")):
#     if 'href' in link.attrs:
#         print(link.attrs['href'])