# from urllib.request import urlretrieve
# from urllib.request import urlopen
# from bs4 import BeautifulSoup

# html = urlopen("http://www.pythonscraping.com")
# bsObj = BeautifulSoup(html, "html.parser")
# imageLocation = bsObj.find("a", {"id": "logo"}).find("img")["src"]
# urlretrieve(imageLocation, "logo.jpg")



# import csv

# csvFile = open("./files/test.csv", "w+")
# try: 
# 	writer = csv.writer(csvFile)
# 	writer.writerow(('number', 'number plus 2', 'number times 2'))
# 	for i in range(10):
# 		writer.writerow((i, i+2, i*2))
# finally:
# 	csvFile.close()



# import csv
# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import ssl

# ssl._create_default_https_context = ssl._create_unverified_context

# html = urlopen("http://en.wikipedia.org/wiki/Comparison_of_text_editors")
# bsObj = BeautifulSoup(html, "html.parser")
# #The main comparison table is currently the first table on the page
# table = bsObj.findAll("table",{"class":"wikitable"})[0]
# rows = table.findAll("tr")

# csvFile = open("./files/editors.csv", 'wt', newline='', encoding='utf-8')
# writer = csv.writer(csvFile)
# try:
# 	for row in rows:
# 		csvRow = []
# 		for cell in row.findAll(['td', 'th']):
# 			csvRow.append(cell.get_text().encode("utf-8"))
# 		writer.writerow(csvRow)
# finally:
#     csvFile.close()



import smtplib
from email.mime.text import MIMEText

msg = MIMEText("메일 내용 이다")

msg['Subjedt'] = "이메일"
msg['From'] = "chbin05@naver.com"
msg['To'] = "chbin05@naver.com"

s = smtplib.SMTP("smtp.naver.com", 587)
s.ehlo()
s.starttls()
s.ehlo()
s.login("chbin05", "password")
s.send_message(msg)
s.quit()