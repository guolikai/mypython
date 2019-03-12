#!/usr/bin/env python3
from celery import Celery
import time
#celery worker设置 tasks是App名字，broker连接的中间件，backend是worker执行结果收取中间件
app = Celery('tasks',
    broker='redis://localhost',
# broker='redis://:srt123@127.0.0.1:6379/0',
    #backend='redis://:@127.0.0.1:6379/0')
    backend='redis://127.0.0.1:6379/0')

 
@app.task        #表示worker可以执行的一个任务
def add(x,y):
    print("running...",x,y)
    return x+y

@app.task        #表示worker可以执行的一个任务
def cmd(cmd):
    print("running cmd",cmd)
    time.sleep(10)
    return time.time()

if __name__ == '__main__':
    pass
