import requests
from bs4 import BeautifulSoup
import bs4

def gethtml(url) :
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return""

def biglist(list, html) :
    soup = BeautifulSoup(html, 'html.parser')
    for header in soup.find('body').children:
        if isinstance(header,bs4.element.Tag):
            h2s = header('h2')
            list.append([h2s[0].string, h2s[1].string, h2s[2].string, h2s[3].string])
    
    

def printlist(list,num) :
    print("{:^10}\t{:^6}\t{:^10}\t{:^10}".format("标题", "时间", "作者", "概要"))
    for i in range(num):
        u = list[i]
        print("{:^10}\t{:^6}\t{:^10}\t{:^10}".format(u[0], u[1], u[2], u[3]))
    

def main() :
    list = []
    url = "https://blog.snowstar.org/"
    html = gethtml(url)
    biglist(list,html)
    printlist(list,10)

main()
