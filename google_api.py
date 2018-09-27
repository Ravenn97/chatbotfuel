
import requests
key  = "AIzaSyBgj-UKYIE4_cgfVAlLqPx6L74LlUBDFgQ"


def make_api(data):
	result = []
	url = (
	'https://maps.googleapis.com/maps/api/place/nearbysearch/json'
	'?location=20.981357,105.787503&radius=2000&'
	'name={}&key={}'
	).format(data, key)

	request = requests.get(url)
	data = request.json()
	list_data = data["results"]
	for coffe in list_data:
		result.append("{} Địa chỉ:{}".format(coffe["name"],coffe["vicinity"]))
	return result

if __name__ == '__main__':
	print("\n".join(make_api("sadasdasd")))

	
