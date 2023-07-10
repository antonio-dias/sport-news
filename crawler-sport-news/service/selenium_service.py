from pathlib import Path
import scrapy
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class SeleniumSpider(scrapy.Spider):
    name = "selenium"

    custom_settings = {
        "BOT_NAME": 'selenium',
        "SPIDER_MODULES": ['selenium.spiders'],
        "NEWSPIDER_MODULE": 'selenium.spiders',
        "SELENIUM_DRIVER_NAME": "chrome",
        "SELENIUM_DRIVER_ARGUMENTS": ['--headless'],
        "DOWNLOADER_MIDDLEWARES": {"scrapy_selenium.SeleniumMiddleware": 800}
    }

    def __init__(self):
        self.start_requests()

    def start_requests(self):
        # urls = ["https://www.google.com/search?q=libertadores#sie=m;/g/11tgdthmhp;2;/m/01rrc6;tl;fp;1;;;"]
        urls = ["https://quotes.toscrape.com/"]
        for url in urls:
            print(url)
            yield SeleniumRequest(
                url=url,
                callback=self.parse,
                wait_time=60,
                wait_until=EC.element_to_be_clickable((By.CLASS_NAME, 'quote')),
            )

    # def parse(self, response):
    #     page = response.url.split("/")[-2]
    #     filename = f"quotes-{page}.html"
    #     Path(filename).write_bytes(response.body)
    #     print(f"Saved file {filename}")

    # def parse(self, response):
    #     with open('image.png', 'wb') as image_file:
    #         image_file.write(response.meta["screenshot"])

    async def parse(self, response):
        print("começando...")
        # filename = f"quotes.html"
        # Path(filename).write_bytes(response.css('div.EIaa9b').get())
        # print(f"Saved file {filename}")
        for quote in response.css('div.quote'):
            print("-- " + quote.get())

        # screenshot = await page.screenshot(path="example.png", full_page = True)
        # await page.close()

    async def errBack(self, failure):
        page = failure.request.meta["playwright_page"]
        await page.close()
