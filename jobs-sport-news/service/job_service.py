from db.database import Database
import logging
from service.rabbitmq_service import RabbitMQ


def find_games_to_start():
    try:
        mongodb_connection = Database()
        data = mongodb_connection.find_all_games_to_start()
        mongodb_connection.close_connection()
        print("- ", data)

        if len(data) > 0:
            rabbitmq = RabbitMQ()
            for message in data:
                rabbitmq.send_message(message['title'])
            rabbitmq.close()

    except Exception as e:
        logging.error(exc_info=True, msg=str(e))
