import pika
import time
#消息持久化必须确保队列持久化存在

credentials = pika.PlainCredentials('newnew', 'rabbitmq123')
connection = pika.BlockingConnection(pika.ConnectionParameters(
    '182.61.17.151',credentials=credentials))
channel = connection.channel()

# 声明queue,durable=True确保rabbitmq服务端队列存在,队列持久化
#重启rabbitmq队列依然存在
channel.queue_declare(queue='task_queue',durable=True)

# n RabbitMQ a message can never be sent directly to the queue, it always needs to go through an exchange.
import sys
#join把脚本收到的参数合并起来
message = ' '.join(sys.argv[1:]) or "Hello World! %s" % time.time()

#properties=pika.BasicProperties(delivery_mode=2) 确保rabbitmq服务端队列中存储数据存在,消息持久化
channel.basic_publish(exchange='',
                      routing_key='task_queue',
                      body=message,
                      properties=pika.BasicProperties(
                          delivery_mode=2,  # make message persistent
                      )
                  )
print(" [x] Sent %r" % message)
connection.close()
