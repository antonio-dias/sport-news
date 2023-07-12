import logging
from service.rabbitmq_service import RabbitMQ
from service.scrapy_service import GameSpider
from scrapy.crawler import CrawlerProcess
from db.database import Database


def extract_game_info():
    try:

        # WORKING WITH RABBITMQ
        # rabbitmq = RabbitMQ()
        # game_to_start = rabbitmq.init_consume()
        # rabbitmq.close()
        # if game_to_start is not None:
        #     print(game_to_start)
        # else:
        #     print("nothing")

        # GETING DATAS FROM GOOGLE
        # process_crawler = CrawlerProcess()
        # process_crawler.crawl(GameSpider)
        # process_crawler.start()

        # SAVING TIMELINE IN MONGO
        # mongodb_connection = Database()
        # _id = "64a3826aca8392654a4b5c36"
        # comment = {"time": "1", "minute": "2", "comment": "E FAAAAALTA", "published": False}
        # mongodb_connection.save_new_comment(_id, comment)

    except Exception as e:
        logging.error(exc_info=True, msg=str(e))
