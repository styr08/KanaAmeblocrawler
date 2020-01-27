from bs4 import BeautifulSoup
import requests

for i in range(1,43):
    if i == 1:
        target = "https://ameblo.jp/nishino-kana/entrylist.html"
    else:
        target = "https://ameblo.jp/nishino-kana/entrylist-" + str(i) + ".html"
    req = requests.get(target)
    html = req.text
    bf = BeautifulSoup(html)
    filename = 'url.txt'
    li = bf.find_all('li', class_='skin-borderQuiet')
    for i in range(0,len(li)):
        text = BeautifulSoup(str(li[i]))
        res = text.find_all('h2')
        text2 = BeautifulSoup(str(res))
        res2 = text2.find_all('a')
        for each in res2:
            with open(filename, 'a') as file_object:
                save = each.get('href')
                print(save)
                file_object.write("https://ameblo.jp"+save+"\n")