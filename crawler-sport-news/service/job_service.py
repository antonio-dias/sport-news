import logging
from service.rabbitmq_service import RabbitMQ
from service.scrapy_service import GameSpider
from service.game_service import verify_halftime
from scrapy.crawler import CrawlerProcess
from db.database import Database
from scrapy import signals
from scrapy.signalmanager import dispatcher


def extract_game_info():
    try:

        # Capturing the result from crawler
        results = []

        def crawler_results(signal, sender, item, response, spider):
            results.append(item)

        dispatcher.connect(crawler_results, signal=signals.item_scraped)

        # WORKING WITH RABBITMQ
        # rabbitmq = RabbitMQ()
        # game_to_start = rabbitmq.init_consume()
        # rabbitmq.close()
        # if game_to_start is not None:
        #     print(game_to_start)
        # else:
        #     print("nothing")

        mongodb_connection = Database()
        _id = "64a776b16e8cdd16f2f2b096"
        # _id = "64a3826aca8392654a4b5c36"
        game = mongodb_connection.find_game_to_crawl(_id)

        if len(game) > 0:

            current_time = 1
            current_minute = -1
            if (game.get("timeline")):
                last_comment = game.get("timeline")[-1]
                current_time, current_minute = verify_halftime(last_comment)

            # GETING DATAS FROM THE SITE
            process_crawler = CrawlerProcess()
            process_crawler.crawl(GameSpider, time=current_time, minute=current_minute)
            process_crawler.start()

            if len(results) > 0:
                comment = results[0]
                print("- ", comment)

                mongodb_connection.save_new_comment(_id, comment, status_game="IN_PROGRESS")

        mongodb_connection.close_connection()

        # SAVING TIMELINE IN MONGO
        # mongodb_connection = Database()
        # _id = "64a776b16e8cdd16f2f2b096"
        # comment = {"time": "1", "minute": "2", "comment": "E FAAAAALTA", "published": False}
        # mongodb_connection.save_new_comment(_id, comment)

    except Exception as e:
        logging.error(exc_info=True, msg=str(e))
