import pika
import sys

credentials = pika.PlainCredentials('newnew', 'rabbitmq123')
connection = pika.BlockingConnection(pika.ConnectionParameters(
    '182.61.17.151',credentials=credentials))
channel = connection.channel()


#绑定exchange='logs'的转发器,类型广播方式
channel.exchange_declare(exchange='logs',type='fanout')

message = ' '.join(sys.argv[1:]) or "info: Hello World!"
#routing_key转发到哪个queue;广播模式下为空
channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=message)
print(" [x] Sent %r" % message)
connection.close()
