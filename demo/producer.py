import pika

from settings import URI

params = pika.URLParameters(URI)
conn = pika.BlockingConnection(params)
channel = conn.channel()

channel.queue_declare(queue='test_q')

if __name__ == '__main__':

    count = 0

    while True:
        channel.basic_publish(
            exchange='',
            routing_key='test_q',
            body=f'Hello, SYSDB-29! - {count}',
        )
        count += 1
