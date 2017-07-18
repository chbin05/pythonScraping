# from urllib.request import urlopen
# textPage = urlopen("http://www.pythonscraping.com/pages/warandpeace/chapter1-ru.txt")
# print(str(textPage.read(), 'utf-8'))

# from urllib.request import urlopen
# from io import StringIO
# import csv

# data = urlopen("http://pythonscraping.com/files/MontyPythonAlbums.csv").read().decode('ascii', 'ignore')
# dataFile = StringIO(data)
# csvReader = csv.reader(dataFile)

# # for row in csvReader:
# # 	print(row)

# dictReader = csv.DictReader(dataFile)

# print(dictReader.fieldnames)

# for row in dictReader:
# 	print(row)

# from pdfminer.pdfinterp import PDFResourceManager, process_pdf
# from pdfminer.converter import TextConverter
# from pdfminer.layout import LAParams
# from io import StringIO
# from io import open
# from urllib.request import urlopen

# def readPDF(pdfFile):
#     rsrcmgr = PDFResourceManager()
#     retstr = StringIO()
#     laparams = LAParams()
#     device = TextConverter(rsrcmgr, retstr, laparams=laparams)

#     process_pdf(rsrcmgr, device, pdfFile)
#     device.close()

#     content = retstr.getvalue()
#     retstr.close()
#     return content

# pdfFile = urlopen("http://pythonscraping.com/pages/warandpeace/chapter1.pdf")
# outputString = readPDF(pdfFile)
# print(outputString)
# pdfFile.close()


from zipfile import ZipFile
from urllib.request import urlopen
from io import BytesIO
from bs4 import BeautifulSoup

wordFile = urlopen("http://pythonscraping.com/pages/AWordDocument.docx").read()
wordFile = BytesIO(wordFile)
document = ZipFile(wordFile)
xml_content = document.read('word/document.xml')

# print(xml_content.decode('utf-8'))

wordObj = BeautifulSoup(xml_content.decode('utf-8'), 'xml') # pip3 install lxml
textStrings = wordObj.findAll("w:t")
for textElem in textStrings:
    print(textElem.text)