import logging
from service.rabbitmq_service import RabbitMQ
from service.scrapy_service import GameSpider
from service.selenium_service import SeleniumSpider
from scrapy.crawler import CrawlerProcess


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
        process_crawler = CrawlerProcess()
        # process_crawler.crawl(GameSpider)
        process_crawler.crawl(SeleniumSpider)
        process_crawler.start()

    except Exception as e:
        logging.error(exc_info=True, msg=str(e))
