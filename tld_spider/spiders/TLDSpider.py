import scrapy

from tld_spider.items import TLDItem


class TLDSpider(scrapy.Spider):
    name = "tld"

    def start_requests(self):
        urls = ['https://www.iana.org/domains/root/db']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response, **kwargs):
        for line in response.css('#tld-table tbody tr'):
            suffix = line.css('.domain.tld a::text').get()
            suffix = suffix.lstrip('\u200f')
            suffix = suffix.rstrip('\u200e')
            tld = suffix[1:]
            idna_tld = tld.encode('idna').decode('utf-8')
            type_re = line.re('generic|infrastructure|country-code|sponsored|test')
            tld_type = type_re[0]
            yield TLDItem(tld=idna_tld, type=tld_type)
