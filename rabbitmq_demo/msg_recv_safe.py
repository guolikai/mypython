import pika, time

credentials = pika.PlainCredentials('newnew', 'rabbitmq123')
connection = pika.BlockingConnection(pika.ConnectionParameters(
    '182.61.17.151',credentials=credentials))
channel = connection.channel()


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    time.sleep(20)
    print(" [x] Done")
    print("method.delivery_tag", method.delivery_tag)
#ch.basic_ack 决定消息是否被安全传递,例如接受失败,队列依然存在  
    ch.basic_ack(delivery_tag=method.delivery_tag)
    #ackownledgement,返回给服务端标识符:method.delivery_tag(rabbitmq自带的)

#no_ack=True 不需要确认消息,默认False,不需要写
channel.basic_consume(callback,
                      queue='task_queue',
                      #no_ack=True
                      )

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
