import pika

from settings import URI

params = pika.URLParameters(URI)
conn = pika.BlockingConnection(params)
channel = conn.channel()


def calback(ch, method, properties, body) -> None:
    print(body)


channel.basic_consume(
    queue='test_q',
    on_message_callback=calback,
    auto_ack=True,
    consumer_tag='netology_consumer',
)

if __name__ == '__main__':
    channel.start_consuming()