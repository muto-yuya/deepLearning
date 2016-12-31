import cv2
import urllib.request
import numpy as np
import time
import  url_convert
from bs4 import BeautifulSoup

url ='https://www.google.com/imgres?imgurl=https%3A%2F%2Fflyawaysimulation.com%2Fimages%2Fdownloadshots%2F24180-f-22-starscream-repaint-by-agnott-d6ae93izip-0-f22-starscream-6.jpg&imgrefurl=https%3A%2F%2Fflyawaysimulation.com%2Fdownloads%2Ffiles%2F24180%2Ffsx-f22-starscream%2F&docid=-HajR04rqlG-SM&tbnid=IoSQnQ0N81JNRM%3A&vet=1&w=1900&h=900&bih=803&biw=1435&q=f22&ved=0ahUKEwjtjaf7853RAhXKTrwKHQqpA8IQMwiPAShjMGM&iact=mrc&uact=8#h=900&vet=1&w=1900'
req = urllib.request.Request(url, headers={'User-Agent' : "Magic Browser"})
html = urllib.request.urlopen( req )
soup = BeautifulSoup(html,"lxml")
print(soup)
print(soup.find_all('img'))
