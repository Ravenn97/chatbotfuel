  
#Python libraries that we need to import for our bot
import random
from google_api import make_api
from flask import Flask, request
from weather import make_crawl
import os
import requests
app = Flask(__name__)

#We will receive messages that Facebook sends our bot at this endpoint 
@app.route("/weather", methods=['GET', 'POST'])
def crawl_weather():
    
    place = request.args.get('place')
    key = '42b238e3c80d1cd15a5dcc981deed41f'
    url = 'api.openweathermap.org/data/2.5/weather?q={city name},{country code}'

@app.route("/tea", methods=['GET', 'POST'])
def crawl_tea():
    data = request.args.get('param')
    key  = "AIzaSyBgj-UKYIE4_cgfVAlLqPx6L74LlUBDFgQ"
    result = []
    url = (
    'https://maps.googleapis.com/maps/api/place/nearbysearch/json'
    '?location=20.981357,105.787503&radius=3000&'
    'name={}&key={}'
    ).format(data, key)

    request = requests.get(url)
    data = request.json()
    list_data = data["results"]
    for store in list_data:
        result.append("{} Địa chỉ:{}".format(store["name"],store["vicinity"]))
    return '\n'.join(result)


