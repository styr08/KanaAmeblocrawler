from bs4 import BeautifulSoup
import requests
import json

# read urls
file = open("url.txt")
for line in file.readlines():
    line = line.strip('\n')
    req = requests.get(target)
    html = req.text
    bf = BeautifulSoup(html)
    # title
    title = bf.find_all("h1", class_="skin-entryTitle")
    title = title[0].text

    # date
    get_date = bf.find_all("script", type="application/ld+json")
    text = get_date[0].text
    d = json.loads(text)
    date = d['datePublished']


    # content
    content = bf.find_all('div', id='entryBody')
    content = content[0].text

    # save blog
    fileroot = "./blogs/" + date[0:10]
    folder = os.path.exists(path)
    if not folder:
        os.mkdir(fileroot)
        filename = fileroot + "/blog.txt"
        with open(filename, 'a') as file_object:
            file_object.write(title + "\n")
            file_object.write(date + "\n")
            file_object.write(content)


    # save image
    text = bf.find_all('div', id='entryBody')
    get_pic = BeautifulSoup(str(text[0]))
    plist = get_pic.find_all('a')
    i = 0
    for each in plist:
        purl = each.get("href")
        pic = requests.get(purl)
        picname = date[0:10] + str(i)
        with open(, 'wb') as f:
            f.write(pic.content)
            f.close()
        i = i+1
