import pika
#广播模式下，每个消费者都有单独的一个队列，对列名字需要服务端自动随机生成
#注意:广播模式下消费者收不到生产者之前发布的消息
credentials = pika.PlainCredentials('newnew', 'rabbitmq123')
connection = pika.BlockingConnection(pika.ConnectionParameters(
    '182.61.17.151',credentials=credentials))
channel = connection.channel()


channel.exchange_declare(exchange='logs', type='fanout')

#不指定queue名字,rabbit会随机分配一个名字,exclusive=True会在使用此queue的消费者断开后,自动将queue删除
result = channel.queue_declare(exclusive=True)  

queue_name = result.method.queue
#把随机生成的队列queue绑定到生成的exchange(交换机/转发器)上；
channel.queue_bind(exchange='logs', queue=queue_name)

print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] %r" % body)


channel.basic_consume(callback, queue=queue_name,no_ack=True)

channel.start_consuming()
