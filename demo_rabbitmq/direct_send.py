import pika
import sys
credentials = pika.PlainCredentials('newnew', 'newnew')
connection = pika.BlockingConnection(pika.ConnectionParameters(
    '182.61.17.151',credentials=credentials))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs',type='direct')
#组播根据关键字来接收消息,第一个参数是级别,第二个参数才是消息
severity = sys.argv[1] if len(sys.argv) > 1 else 'info' #严重程度,级别

message = ' '.join(sys.argv[2:]) or 'Hello World!'
#routing_key队列绑定
channel.basic_publish(exchange='direct_logs',
                      routing_key=severity,
                      body=message)
print(" [x] Sent %r:%r" % (severity, message))
connection.close()
