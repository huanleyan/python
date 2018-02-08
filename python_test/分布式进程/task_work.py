import time,sys,queue
from multiprocessing.managers import BaseManager

#创建类似的QueueManager:
class QueueManager(BaseManager):
    pass

#由于这个QueueManager只能从网络上获取Queue,所以注册时只提供名字
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

#连接到服务器，也就是运行task_master.py的机器
server_addr = '127.0.0.1'
print('connect to server %s....' % server_addr)

#端口和验证码注意保持和task_master.py的设置一致
m=QueueManager(address=(server_addr, 6000), authkey=b'abc')
#从网络链接
m.connect()

#获取Queue的对象
task = m.get_task_queue()
result = m.get_result_queue()

for i in range(10):
    try:
        n = task.get(timeout=1)
        print('run task %d*%d...' % (n,n))
        r = '%d*%d=%d' % (n,n,n*n)
        time.sleep(1)
        result.put(r)
    except Queue.Empty:
        print('task queue is Empty')

#处理结束
print('work exit')
