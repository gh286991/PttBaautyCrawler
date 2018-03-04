import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import os


payload = {
    'from': '/bbs/Beauty/index.html',
     'yes':'yes'
}

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299'
}

rs = requests.Session()

rs.post('https://www.ptt.cc/ask/over18',data = payload , headers= headers )
res = rs.get('https://www.ptt.cc/bbs/Beauty/index.html',headers= headers)
#print(res.text)

soup = BeautifulSoup(res.text, 'html.parser')

items = soup.select('.r-ent')
links = soup.select('a[href^=/bbs/Beauty/M]')
'''
for item in items:
    D = item.select('.date')[0].text
    T = item.select('.title')[0].text
    A = item.select('.author')[0].text
    
    print('日期 :' ,D,'標題 :' ,T,'作者 :',A )
'''

for link in links:
    L = link.get('href')
    T2 = link.text
    print('標題 :' ,T2,'link =', 'https://www.ptt.cc/'+ L )

    res = requests.get('https://www.ptt.cc/'+L, headers =headers)

    soup = BeautifulSoup(res.text, 'html.parser')

    images = soup.select('a[href^=http://i.imgur]')
    #print('內容:' ,len(images))
    if len(images) ==  0 :
       images = soup.select('a[href^=https://i.imgur]')

    if len(images) ==  0 :
        images = soup.select('a[href^=https://imgur]')
            
    for image in images:

        print(image['href'])
        filename = image['href'].split('/')[3]
        print(filename)

        path = "./images/"+T2
        if not os.path.isdir(path):
            os.mkdir(path)
        
        print(path)
        img = urlopen(image['href'])
        with open(path +'/' + str(filename),'wb') as f:
            f.write(img.read())

## Test for git