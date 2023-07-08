import logging
from service.rabbitmq_service import RabbitMQ


def extract_game_info():
    try:

        rabbitmq = RabbitMQ()
        game_to_start = rabbitmq.init_consume()
        rabbitmq.close()
        if game_to_start is not None:
            print(game_to_start)
        else:
            print("nada")

    except Exception as e:
        logging.error(exc_info=True, msg=str(e))
