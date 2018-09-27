import requests
from bs4 import BeautifulSoup as BS

def make_crawl():
	url = "https://www.24h.com.vn/ttcb/thoitiet/thoi-tiet-ha-noi"
	re = requests.get(url)
	data = re.text
	soup = BS(data, "html.parser")
	result = soup.find("td",class_="ttCel").get_text().replace("\n"," ").strip()
	return "Hôm nay nhiệt độ {}".format(result)


if __name__ == '__main__':
	make_crawl()