#!/usr/bin/env python3
#下面2行表示从python包的绝对路径里导入"celery",而不是当前路径导入
from __future__ import absolute_import, unicode_literals
from celery import Celery
 
#app = Celery('proj',
#              broker='amqp://',
#              backend='amqp://',
#                include=['proj.tasks']
#            )
app = Celery('proj',
              broker='redis://127.0.0.1',
              backend='redis://127.0.0.1',
              include=['AutoOps.tasks','AutoOps.tasks2','AutoOps.periodic_task'])

# Optional configuration, see the application user guide.
#app.conf.update(
#      result_expires=3600,
#  )

if __name__ == '__main__':
    app.start()
