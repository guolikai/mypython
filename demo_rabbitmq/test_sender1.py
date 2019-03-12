import pika

credentials = pika.PlainCredentials('newnew', 'rabbitmq123')
connection = pika.BlockingConnection(pika.ConnectionParameters(
    '182.61.17.151',credentials=credentials))

channel = connection.channel() #建立了rabbit 协议的通道

# 声明queue
channel.queue_declare(queue='hello')

# n RabbitMQ a message can never be sent directly to the queue, it always needs to go through an exchange.
#body是消息内容,routing_key理解为发送消息到hello队列
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")
#队列关闭
connection.close()
