import requests
from bs4 import BeautifulSoup as BS

def make_crawl():
	url = "https://www.accuweather.com/vi/vn/hanoi/353412/current-weather/353412"
	re = requests.get(url)
	data = re.text
	soup = BS(data, "html.parser")
	result = soup.find(class_="day fday1 current first cl { href: 'https://www.accuweather.com/vi/vn/hanoi/353412/daily-weather-forecast/353412?day=1' }").get_text().replace("\n"," ").strip()
	return "Hôm nay nhiệt độ {}".format(result)


if __name__ == '__main__':
    make_crawl()