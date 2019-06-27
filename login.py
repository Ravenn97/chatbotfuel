from selenium import webdriver
from bs4 import BeautifulSoup
import requests
from selenium.webdriver.chrome.options import Options


def login(ID, password):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920x1080")
    driver = webdriver.Chrome("/home/van-xa/chat_bot/chromedriver")
    driver.get("http://qldt.ptit.edu.vn/")
    driver.find_element_by_id("ctl00_ContentPlaceHolder1_ctl00_ucDangNhap_txtTaiKhoa").send_keys(ID)
    driver.find_element_by_id("ctl00_ContentPlaceHolder1_ctl00_ucDangNhap_txtMatKhau").send_keys(password)
    driver.find_element_by_id("ctl00_ContentPlaceHolder1_ctl00_ucDangNhap_btnDangNhap").click()
    driver.find_element_by_id("ctl00_menu_lblThoiKhoaBieu").click()
    table = driver.find_element_by_id('ctl00_ContentPlaceHolder1_ctl00_Table1')
    head = table.find_element_by_tag_name('thead')
    body = table.find_element_by_tag_name('tbody')

    file_data = []
    file_header = []
    head_line = head.find_element_by_tag_name('tr')
    headers = head_line.find_elements_by_tag_name('th')
    for header in headers:
        header_text = header.text.encode('utf8')
        file_header.append(header_text)
    file_data.append(file_header)

    body_rows = body.find_elements_by_tag_name('tr')
    for row in body_rows:
        data = row.find_elements_by_tag_name('td')
        file_row = []
        for datum in data:
            datum_text = datum.text
            file_row.append(datum_text)
        file_data.append(file_row)

    result = []
    for i in file_data[1:]:
        if len(i) >= 2:
            result.append(i)

    result1 = [[j for j in i if j == '' or '\n' in j] for i in result[:-2]]
    return result1


def make_response(result1, number):
    result2 = [i[number] for i in result1]
    result3 = []
    for index, value in enumerate(result2):
        if not value == '':
            result3.append('tiết {} bắt đầu {}'.format(index + 1, value).replace('\n', ''))
    return result3


def take_day():
    re = requests.get('https://xoso.com.vn/')
    data = re.textsoup
    soup = BS(data, 'html.parser')
    ss = soup.find('span', class_='post-time display-desktop').get_text()
    sss = ss.lower().strip().split()
    list_of_day = ['hai', 'ba', 'tư', 'năm', 'sáu', 'bảy', 'nhật']
    for word in sss:
        if word in list_of_day:
            return word


def main():
    ID = request.args.get('id')
    password = request.args.get('password')


    data = login(ID, password)
    today = take_day()
    if today == 'hai':
        return make_response(0, data)
    elif today == 'ba':
        return make_response(1, data)
    elif today == 'tư':
        return make_response(2,data)
    elif today == 'năm':
        return make_response(3, data)
    elif today == 'sáu':
        return make_response(4, data)
    elif today == 'bảy':
        return make_response(5, data)
    elif today == 'nhật':
        return make_response(6, data)
