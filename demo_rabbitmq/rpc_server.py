import pika
import time

credentials = pika.PlainCredentials('newnew', 'rabbitmq123')
connection = pika.BlockingConnection(pika.ConnectionParameters(
    '182.61.17.151',credentials=credentials))


channel = connection.channel()
channel.queue_declare(queue='rpc_queue')


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def on_request(ch, method, props, body):
    """Callback函数"""
    n = int(body)

    print(" [.] fib(%s)" % n)
    response = fib(n)

    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id=props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)

#prefetch_count=1 每次只接收一个消息,处理完会返回服务端;客户端主动向服务端要消息
channel.basic_qos(prefetch_count=1)
channel.basic_consume(on_request, queue='rpc_queue')

print(" [x] Awaiting RPC requests")
channel.start_consuming()
