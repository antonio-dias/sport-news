from operator import itemgetter

import scrapy
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from service.game_service import get_current_game_tag


class GameSpider(scrapy.Spider):
    name = "game"

    custom_settings = {
        "SELENIUM_DRIVER_NAME": "chrome",
        "SELENIUM_DRIVER_ARGUMENTS": ['--headless',
                                      "--no-sandbox",
                                      "enable-automation",
                                      "--disable-dev-shm-usage",
                                      "--window-size=1920x1080",
                                      "--disable-notifications",
                                      "--disable-extenstions",
                                      "--disable-gpu",
                                      "--dns-prefetch-disable",
                                      "disable-infobars",
                                      "force-device-scale-factor=0.65",
                                      "high-dpi-support=0.65"
                                      ],
        "DOWNLOADER_MIDDLEWARES": {"scrapy_selenium.SeleniumMiddleware": 800}
    }

    def __init__(self, time=1, minute=0):
        self.start_requests()
        self.time = time
        self.minute = minute
        self.current_game_tag_time = ""

    def start_requests(self):
        # urls = ["https://www.google.com/search?q=libertadores#sie=m;/g/11tgdthmhp;2;/m/01rrc6;tl;fp;1;;;"]
        # urls = ["https://www.terra.com.br/esportes/futebol/libertadores/ao-vivo/internacional-x-independiente-medellin/78492/"]
        urls = ["https://www.terra.com.br/esportes/futebol/libertadores/ao-vivo/flamengo-x-emelec/58925/"]

        self.current_game_tag_time = get_current_game_tag(self.time)
        print("tag_time: ", self.current_game_tag_time)
        for url in urls:
            yield SeleniumRequest(
                url=url,
                callback=self.parse,
                wait_time=100,
                wait_until=EC.element_to_be_clickable((By.CSS_SELECTOR, self.current_game_tag_time)),
            )


    async def parse(self, response):
        list_comments = []
        for quote in response.css(f'div{self.current_game_tag_time} ul li'):
            minute_to_save = quote.css('li::attr(data-time)').get()
            for comment in quote.css('div.comment'):
                comment_to_save = comment.css("div.comment-line::text").get()
                if comment_to_save == None:
                    comment_to_save = comment.css("div.comment-line::attr(id)").get()

                if int(self.minute) < int(minute_to_save):
                    list_comments.append(
                        {
                            "time": self.time,
                            "minute": minute_to_save,
                            "comment": comment_to_save,
                            "published": False
                        })

        list_comments = sorted(list_comments, key=lambda x: (int(itemgetter('minute')(x))))
        return list_comments
