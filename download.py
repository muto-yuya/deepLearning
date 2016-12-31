import cv2
import urllib.request
import numpy as np
import time
import url_convert
def make_image(image_url,numbering):
    print(str(i)+" dowloading...")
    # URLの画像情報をロード
    resp = urllib.request.urlopen(image_url)

    # OpenCVで読み込めるよう画像のメモリバッファ再構築
    image = np.asarray(bytearray(resp.read()), dtype=np.uint8)

    # メモリバッファより画像読み込み
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)

    # 新たな画像として書き出す
    first_number = 0 #連番一つ目のファイルの番号
    cv2.imwrite("yamaga"+str(numbering+first_number)+".jpg", image)

url_convert.url_convert()


url_list = []
f = open('output.txt', 'r')
for line in f:
    url_list.append(line[:-1])
f.close()

print(url_list)
for i in range(0,len(url_list)):
    make_image(url_list[i],i)
    time.sleep(1)
