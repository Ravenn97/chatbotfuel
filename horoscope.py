import requests
from bs4 import BeautifulSoup as BS
re = requests.get("http://afamily.vn/horoscope.html")
soup = BS(re.text, "html.parser")
URL = soup.find("div", class_="afwblul-info").find(href=True).get('href')
URL = "http://afamily.vn"+ URL
re = requests.get(URL)
soup = BS(re.text, "html.parser")
data = soup.find("div",class_="afcbc-body vceditor-content").get_text().replace("\n"," ").replace("\xa0","")
print(data)
