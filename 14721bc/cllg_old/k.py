import scrapy
import logging


class DataSpider(scrapy.Spider):
    name = 'data'
    allowed_domains = [
        'https://in.finance.yahoo.com/quote/AAPL/history?p=AAPL']
    start_urls = ['https://in.finance.yahoo.com/quote/AAPL/history?p=AAPL']

    def start_requests(self):
        urls = [
            'https://in.finance.yahoo.com/quote/AAPL/history?p=AAPL',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse_data(self, response):
        table = response.xpath('//*[@class="W(100%) M(0)"]')
        table = response.xpath('//*[@class="W(100%) M(0)"]//tbody')
        rows = table.xpath('//tr')

        for row in response.xpath('//*[@class="W(100%) M(0)"]//tbody//tr'):
            yield {
                'date': row.xpath('td[1]//text()').extract_first(),
                'open': row.xpath('td[2]//text()').extract_first(),
                'high': row.xpath('td[3]//text()').extract_first(),
                'low': row.xpath('td[4]//text()').extract_first(),
                'close': row.xpath('td[5]//text()').extract_first(),
                'adj': row.xpath('td[6]//text()').extract_first(),
                'volume': row.xpath('td[7]//text()').extract_first(),
            }
            print(data)
            df = df.append(data, ignore_index=True)
