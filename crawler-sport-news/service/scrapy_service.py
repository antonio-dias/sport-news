import scrapy
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


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

    def __init__(self):
        self.start_requests()

    def start_requests(self):
        urls = ["https://www.google.com/search?q=libertadores#sie=m;/g/11tgdthmhp;2;/m/01rrc6;tl;fp;1;;;"]
        urls = ["https://www.terra.com.br/esportes/futebol/libertadores/ao-vivo/internacional-x-independiente-medellin/78492/"]
        for url in urls:
            yield SeleniumRequest(
                url=url,
                callback=self.parse,
                wait_time=100,
                wait_until=EC.element_to_be_clickable((By.CSS_SELECTOR, '#narration-1-half')),
            )


    async def parse(self, response):
        for quote in response.css('div#narration-1-half ul li'):
            print("-- " + quote.css('li::attr(data-time)').get())
            for comment in quote.css('div.comment'):
                print("---- " + comment.css('div.comment-line::text').get())


    async def errBack(self, failure):
        page = failure.request.meta["playwright_page"]
        await page.close()
