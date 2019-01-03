  
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
    data = "Hôm nay nhiệt độ Hà Nội {}".format(result)
    r = {
    "messages": [
    {"text": data},
    ]
    }
    if "mưa" in data:
        r = {
        "messages": [
        {"text": data},
        {"text": "trời mưa nhớ mang ô nhaa, ướt người về ốm thì em thương lắm :("}
        ]
        }
    #r.headers['Content-Type'] = 'application/json'
    return jsonify(r)

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

@app.route("/buabaokeo", methods=['GET','POST'])
def play_game():
    param = request.args.get('param')
    list_ = ['Búa', 'Bao', 'Kéo']
    if param.title() in list_:
        text_ = random.choice(list_)
        if param.lower() == 'búa':
            if text_ == 'Búa':
                sent_text = 'Hòa rùi chơi lại nhaa \n😙😙😙'
            if text_ == 'Bao':
                sent_text = 'ahihi ngu vclon` :))'
            if text_ == 'Kéo':
                sent_text = 'Hay lắm dmm chơi lại =.=!'
        elif param.lower() == 'bao':
            if text_ == 'Bao':
                sent_text = 'Hòa rùi chơi lại nhaa \n😙😙😙'
            if text_ == 'Kéo':
                sent_text = 'ahihi ngu vclon` :))'
            if text_ == 'Búa':
                sent_text = 'Hay lắm dmm chơi lại =.=!'
        elif param.lower() == 'kéo':
            if text_ == 'Kéo':
                sent_text = 'Hòa rùi chơi lại nhaa \n😙😙😙'
            if text_ == 'Búa':
                sent_text = 'ahihi ngu vclon` :))'
            if text_ == 'Bao':
                sent_text = 'Hay lắm dmm chơi lại =.=!'
    else:
        text_ = "Chỉ chơi có bao búa kéo thôi "
        sent_text = "Đọc luật đi rồi chơi nhé :3 "
    r = {
        "messages": [
        {"text": text_},
        {"text": sent_text}
        ]
        }  
    return jsonify(r)

@app.route("/xsmb", methods=['GET','POST'])
def find_lucky_number():
    re = requests.get("https://xoso.com.vn/")
    data = re.text
    soup = BS(data, "html.parser")
    number = soup.find("span", id ="mb_prizeDB_item0").get_text()
    text_ = "Ting, ting.. con số may mắn hôm nay là {}".format(number[-2:])
    r = {
        "messages": [
        {"text": text_}
        ]
        }  
    return jsonify(r)


if __name__ == '__main__':
    app.run(debug=True)