import requests
import pyquery
url = 'http://www.51lovelife.com/index.php/Home/Index/article/aid/32'
url_list = list()
resp = requests.get(url)
doc = pyquery.PyQuery(resp.content.decode())
a_tags = doc.find('a')
for a in a_tags.items():
    if a.attr('href').startswith('http'):
        url_list.append(a.attr('href'))
    elif a.attr('href').startswith('/'):
        url_list.append('http://www.51lovelife.com'+a.attr('href'))

print(url_list)
