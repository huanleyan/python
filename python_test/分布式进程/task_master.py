import random, time, queue
from multiprocessing.managers import BaseManager


#创建发送任务的队列
task_queue=queue.Queue()
#接收结果的队列
result_queue = queue.Queue()

#从BaseManager继承QueueManager:
class QueueManager(BaseManager):
    """docstring for QueueManager."""
    pass

#把两个queue都注册到网络上，callable参数关联了Queue对象
QueueManager.register('get_task_queue', callable=lambda:task_queue)
QueueManager.register('get_result_queue', callable=lambda:result_queue)

#绑定验证码，设置端口号5000
manager = QueueManager(address=('127.0.0.1',6000), authkey=b'abc')

#启动queue
manager.start()

#获得通过网路访问的Queue对象
task = manager.get_task_queue()
result = manager.get_result_queue()

#放几个任务进去
for i in range(10):
    n = random.randint(0, 10000)
    print('Put task %d...' % n)
    task.put(n)

#从result队列读取结果
print('Try get results...')
for i in range(10):
    r=result.get(timeout=10)
    pass

#关闭
manager.shutdown()
print('master exit')
