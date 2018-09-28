  
#Python libraries that we need to import for our bot
import random
from google_api import make_api
from flask import Flask, request, make_response, jsonify
from weather import make_crawl
import os
import requests
from bs4 import BeautifulSoup as BS
app = Flask(__name__)
import json
from selenium import webdriver

#We will receive messages that Facebook sends our bot at this endpoint

@app.route('/')
def welcome():
    return 'hello word'

@app.route("/weather", methods=['GET', 'POST'])
def crawl_weather():  
    url = "https://www.24h.com.vn/ttcb/thoitiet/thoi-tiet-ha-noi"
    re = requests.get(url)
    data = re.text
    soup = BS(data, "html.parser")
    result = soup.find("td",class_="ttCel").get_text().replace("\n"," ").strip()
    data = "Hôm nay nhiệt độ Hà Nội{}".format(result)
    res = {
 "messages": [
   {"text": data}
 ]
}
    r = jsonify({
 "messages": [
   {"text": data},
 ]
})
    #r.headers['Content-Type'] = 'application/json'
    return r

@app.route("/place", methods=['GET', 'POST'])
def crawl_tea():
    data = request.args.get('param')
    key  = "AIzaSyBgj-UKYIE4_cgfVAlLqPx6L74LlUBDFgQ"
    result = []
    url = (
    'https://maps.googleapis.com/maps/api/place/nearbysearch/json'
    '?location=20.981357,105.787503&radius=3000&'
    'name={}&key={}'
    ).format(data, key)

    re = requests.get(url)
    data = re.json()
    list_data = data["results"]
    for store in list_data:
        result.append("{} Địa chỉ:{}".format(store["name"],store["vicinity"]))
    text_ = "\n".join(result)   
    dict_ = {
    "messages": [
    {"text": text_}
    ]
    }
    return jsonify(dict_)
    

if __name__ == '__main__':
    app.run(debug=True)