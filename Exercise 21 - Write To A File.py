# Get text from a webpage - save in a .txt file

import requests
from bs4 import BeautifulSoup

url = 'https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'
r = requests.get(url)
r_html = r.text
page = BeautifulSoup(requests.get(url).text, "lxml")

fname = input("Name text file (inc .txt): ")
open_file = open(fname,'w')
for text in page.find_all("p"):
    open_file.write(text.text.strip())
open_file.close()
