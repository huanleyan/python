# _*_ coding: utf-8 _*_

import csv
import datetime

data = [
    [1, "程欢", 19.353, datetime.datetime(2001, 3, 17)],
    [2, "chenghuan", 13.287, datetime.datetime(2011, 4, 27)],
    [3, "aaa", 15.852, datetime.datetime(2003, 7, 14)],
    [4, "zh'n", 11.937, datetime.datetime(2012, 1, 9)],
    [5, "i\'op", 12.057, datetime.datetime(2009, 5, 18)],
]

#如果不指定newline='',则每写入一行将有一空行被写入。上面的代码生成如下内容。
with open("test.csv", "w" , newline='') as file:
    writer = csv.writer(file, dialect="excel")
    for item in data:
        print(item)
        writer.writerow(item)

with open("test.csv", "r") as file:
    reader = csv.reader(file, dialect="excel")
    for item in reader:
        pass
        #print(item)

with open("test.csv", "r") as file:
    reader = csv.DictReader(file, fieldnames=["id", "name", "float", "datetime"], dialect="excel")
    data=[item for item in reader]
    print(data)

with open("test.csv", "w" , newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["id", "name", "float", "datetime"], dialect="excel")
    ## 标头在这里传入，作为第一行数据
    writer.writeheader()
    for item in data:
        writer.writerow(item)
## 还可以写入多行
#    writer.writerows(data)
