from pathlib import Path
import scrapy
import asyncio
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
from scrapy_playwright.page import PageMethod


class GameSpider(scrapy.Spider):
    name = "pwdemo"

    custom_settings = {
        "BOT_NAME": 'pwdemo',
        "SPIDER_MODULES": ['pwdemo.spiders'],
        "NEWSPIDER_MODULE": 'pwdemo.spiders',
        "TWISTED_REACTOR": "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
    }

    def __init__(self):
        self.start_requests()

    def start_requests(self):
        urls = ["https://www.google.com/search?q=libertadores#sie=m;/g/11tgdthmhp;2;/m/01rrc6;tl;fp;1;;;"]
        urls = ["https://quotes.toscrape.com/"]
        for url in urls:
            print(url)
            # yield scrapy.Request(url=url, callback=self.parse)
            yield scrapy.Request(url, meta=dict(
                playwright = True,
                playwright_include_page = True,
                playwright_page_methods = [
                    PageMethod('wait_for_selector', 'div.quote')
                ],
                errBack = self.errBack
            ))

    # def parse(self, response):
    #     page = response.url.split("/")[-2]
    #     filename = f"quotes-{page}.html"
    #     Path(filename).write_bytes(response.body)
    #     print(f"Saved file {filename}")

    async def parse(self, response):
        print("começando...")
        page = response.meta["playwright_page"]
        # filename = f"quotes.html"
        # Path(filename).write_bytes(response.css('div.EIaa9b').get())
        # print(f"Saved file {filename}")
        # for quote in response.css('div.AJLUJb'):
        #
        #     print("-- " + quote.get())

        screenshot = await page.screenshot(path="example.png", full_page = True)
        await page.close()

    async def errBack(self, failure):
        page = failure.request.meta["playwright_page"]
        await page.close()
