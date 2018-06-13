import redis
import base64
import re

def make_connect():
    r=redis.Redis(host='127.0.0.1',port='6379')
    return r

def parse_coupon(c_code):
    return c_code.encode('utf-8')


def upload_to_database():
    session = make_connect()
    with open('coupondata.txt', 'r') as file:
        key = 'abc'
        n=1
        for line in file.readlines():
            c_id=parse_coupon(line)
            n+=1
            session.set(key+str(n), line.strip())

if __name__ == '__main__':
    upload_to_database()
