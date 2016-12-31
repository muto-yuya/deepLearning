from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import cv2
import urllib.request
import numpy as np
import time
import  url_convert


person_name = "arageki" #とってくる人の名前
first_number = 0 #連番一つ目のファイルの番号
i=0


def parse_url(target_url):
    des_cap = dict(DesiredCapabilities.PHANTOMJS)
    des_cap["phantomjs.page.settings.userAgent"] = (
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/28.0.1500.52 Safari/537.36'
    )
    driver = webdriver.PhantomJS(desired_capabilities=des_cap)
    driver.get(target_url)
    data = driver.page_source.encode('utf-8')

    html = BeautifulSoup(data,"lxml")
    return html.find('title').text.split(' ')[2]


def make_image(image_url,numbering):
    print(str(i)+" dowloading...")
    # URLの画像情報をロード
    resp = urllib.request.urlopen(image_url)

    # OpenCVで読み込めるよう画像のメモリバッファ再構築
    image = np.asarray(bytearray(resp.read()), dtype=np.uint8)

    # メモリバッファより画像読み込み
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)

    # 新たな画像として書き出す
    cv2.imwrite(person_name+str(numbering+first_number)+".jpg", image)

#実行
url_convert.url_convert()

url_list = []
f = open('output.txt', 'r')
for line in f:
    url_list.append(line[:-1])
f.close()

for i in range(0,len(url_list)):
    image_url = parse_url(url_list[i])
    make_image(image_url,i)
    time.sleep(1)