# -*- coding:UTF-8 -*-
from bs4 import BeautifulSoup
import requests
import json
import os

'''
    Download all blogs
    From https://ameblo.jp/nishino-kana 
    param: none
    return: none
    modify: 2020-1-27
'''



target = 'https://ameblo.jp/nishino-kana/entry-12437594208.html'
req = requests.get(target)
html = req.text
bf = BeautifulSoup(html)
# content
content = bf.find_all('div', id='entryBody')
content1 = content[0].text
for each in content:
    print(each.get('p'))

'''
get_pic = BeautifulSoup(str(texts[0]))
plist = get_pic.find_all('a')
for each in plist:
    purl = each.get("href")
    pic = requests.get(purl)
    with open("text.jpg", 'wb') as f:
        f.write(pic.content)
        f.close()
'''