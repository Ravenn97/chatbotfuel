  
#Python libraries that we need to import for our bot
import random
from flask import Flask, request, make_response, jsonify
import os
import requests
from bs4 import BeautifulSoup as BS
app = Flask(__name__)

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
    r = jsonify({
    "messages": [
    {"text": data},
    ]
    })  
    if "mưa" in data:
        r = jsonify({
        "messages": [
        {"text": data},
        {"text": "trời mưa nhớ mang ô nhaa, ướt người về ốm thì em thương lắm :("}
        ]
        })  
    #r.headers['Content-Type'] = 'application/json'
    return r

@app.route("/place", methods=['GET', 'POST'])
def crawl_tea():
    param = request.args.get('param')
    key  = "AIzaSyBgj-UKYIE4_cgfVAlLqPx6L74LlUBDFgQ"
    result = []
    url = (
    'https://maps.googleapis.com/maps/api/place/nearbysearch/json'
    '?location=20.981357,105.787503&radius=3000&'
    'name={}&key={}'
    ).format(param, key)

    re = requests.get(url)
    data = re.json()
    list_data = data["results"]
    for store in list_data:
        result.append("{} Địa chỉ:{}".format(store["name"],store["vicinity"]))
    text_ = "\n".join(result)   
    r = {
    "messages": [
    {"text": text_}
    ]
    }
    if param in ["tea","coffee"]:
        r = {
            "messages": [
            {"text": text_},
            {"text":"đi chơi nhớ mua phần em với nhaa :>"}
            ]
            }   

    return jsonify(r)
    

if __name__ == '__main__':
    app.run(debug=True)