import string
import random
def coupon_creator(digit):
    coupon = ''
    for word in range(digit):
        #random.choice从序列中获取一个随机元素。其函数原型为：random.choice(sequence)。参数sequence表示一个有序类型。这里要说明 一下
        coupon += random.choice(string.ascii_uppercase + string.digits)
    return coupon

def two_hundred_coupons():
    data = ''
    count = 1
    for count in range(200):
        digit=12
        count+=1
        data +='coupon no.'+str(count)+' '+coupon_creator(digit)+'\n'
    return data

coupondata = open('coupondata.txt', 'w')
coupondata.write(two_hundred_coupons())
coupondata.close()
