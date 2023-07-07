import pika


class RabbitMQ:

    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='queue_new_games')

    def send_message(self, message_body):
        self.channel.basic_publish(exchange='',
                              routing_key='queue_new_games',
                              body=message_body)
        print("Message send to queue_new_games")

    def close(self):
        self.connection.close()
