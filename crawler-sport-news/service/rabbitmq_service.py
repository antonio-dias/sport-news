import pika


class RabbitMQ:

    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='queue_new_games')

    def init_consume(self):
        method_frame, header_frame, body = self.channel.basic_get(queue = 'queue_new_games')
        if method_frame is not None:
            self.channel.basic_ack(delivery_tag=method_frame.delivery_tag)
            return body
        return None

    def close(self):
        self.connection.close()
