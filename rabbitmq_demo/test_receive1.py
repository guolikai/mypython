import pika
import time
#设置RabbitMq登录的用户名及密码
credentials = pika.PlainCredentials('newnew', 'rabbitmq123')
#RabbitMq连接,只是连接一个Socket
connection = pika.BlockingConnection(pika.ConnectionParameters(
    '182.61.17.151',credentials=credentials))
#建立RabbitMQ协议的通道,实例化一个channel
channel = connection.channel()

#声明hello的消息队列
channel.queue_declare(queue='hello')

#ch是channel的实例,method发送消息是的信息,properties属性,body是消息(bytes格式)
def callback(ch, method, properties, body):
    print("received msg...start processing....",body)
#    time.sleep(20)
    #print(" [x] Received %r" % ch,method, properties, body)
    print(" [x] msg process done....",body)

#队列消费,queue队列名,callback表示一收到消息时调用函数
channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
#开始消费
channel.start_consuming()
#消费端消费消息没给服务的回馈
