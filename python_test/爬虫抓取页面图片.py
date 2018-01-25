import requests
from pyquery import PyQuery
from urllib.request import urlopen

class DownLoadImage(object):
    def __init__(self):
        self.urls = list()
        self.url = 'http://tieba.baidu.com/p/2166231880'
        self.headers = {
                'Accept':'text/html.application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'Accept-Encoding':'gzip,deflate',
                'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
                'Cache-Control':'max-age=0',
                'Connection':'keep-alive',
                #'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) Chrome/59.0.3071.109 Safari/537.36'
                
        }
        self.s = requests.session()
        self.s.headers.update(self.headers)

    def get_image_url(self):
        resp = self.s.get(self.url)
        doc=PyQuery(resp.content.decode())
        imgs = doc.find('img')
        for img in imgs.items():
            self.urls.append(img.attr('src'))

    def save(self):
        for i in range(len(self.urls)):
            url = self.urls[i]
            print(url)
            resp = self.s.get(url)
            filename = './images/img'+str(i)+'.jpg'
            with open(filename, 'wb') as file:
                file.write(resp.content)

    def download(self):
        self.get_image_url()
        self.save()

if __name__ == '__main__':
        d = DownLoadImage()
        d.download()
