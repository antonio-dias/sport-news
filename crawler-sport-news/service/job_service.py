import logging
import schedule
from service.rabbitmq_service import RabbitMQ
from service.scrapy_service import GameSpider
from service.game_service import verify_halftime
from scrapy.crawler import CrawlerRunner
from multiprocessing import Process, Queue
from twisted.internet import reactor
from db.database import Database
from scrapy import signals
from scrapy.signalmanager import dispatcher


def start_job_crawler():
    schedule.every(30).seconds.do(extract_game_info)

    while True:
        schedule.run_pending()

    # WORKING WITH RABBITMQ
    # rabbitmq = RabbitMQ()
    # game_to_start = rabbitmq.init_consume()
    # rabbitmq.close()
    # if game_to_start is not None:
    #     print(game_to_start)
    #
    # else:
    #     print("nothing")

# Control all jobs using multiprocess to crawler work without restart
def extract_game_info():
    queue = Queue()
    process = Process(target=crawler_action, args=(queue,))
    process.start()
    process.join()


def crawler_action(queue):
    try:
        # Capturing the result from crawler
        results = []

        def crawler_results(signal, sender, item, response, spider):
            results.append(item)

        dispatcher.connect(crawler_results, signal=signals.item_scraped)

        mongodb_connection = Database()
        _id = "64a776b16e8cdd16f2f2b096"
        # _id = "64a3826aca8392654a4b5c36"
        game = mongodb_connection.find_game_to_crawl(_id)

        if len(game) > 0:

            current_time = 1
            current_minute = -1
            if game.get("timeline"):
                last_comment = game.get("timeline")[-1]
                current_time, current_minute = verify_halftime(last_comment)

            # GETTING DATAS FROM THE SITE
            runner = CrawlerRunner()
            deferred = runner.crawl(GameSpider, time=current_time, minute=current_minute)
            deferred.addBoth(lambda _: reactor.stop())
            reactor.run()
            queue.put(None)

            if len(results) > 0:
                new_comment = results[0]
                print("- ", new_comment)

                mongodb_connection.save_new_comment(_id, new_comment, status_game="IN_PROGRESS")

        mongodb_connection.close_connection()

    except Exception as e:
        queue.put(e)
        logging.error(exc_info=True, msg=str(e))
