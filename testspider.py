import scrapy


class TestspiderSpider(scrapy.Spider):
    name = "testspider"
    allowed_domains = ["www.covers.com"]
    start_urls = ["https://www.covers.com/sport/basketball/nba/teams/main/boston-celtics/2021-2022"]

    def parse(self, response):
        print('dir', dir(response))
        print('status',response.status)
        print('text',response.body)
