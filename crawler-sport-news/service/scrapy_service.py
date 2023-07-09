from pathlib import Path
import scrapy


class GameSpider(scrapy.Spider):
    name = "game"

    def __init__(self):
        self.start_requests()

    def start_requests(self):
        urls = ["https://www.google.com/search?q=libertadores#sie=m;/g/11tgdthmhp;2;/m/01rrc6;tl;fp;1;;;"]
        for url in urls:
            print(url)
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f"quotes-{page}.html"
        Path(filename).write_bytes(response.body)
        print(f"Saved file {filename}")