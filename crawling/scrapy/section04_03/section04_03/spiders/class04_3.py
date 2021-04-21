import scrapy
from ..items import SiteRankItems

class TestSpider(scrapy.Spider):
    name = 'test10'
    allowed_domains = ['alexa.com/topsites']
    start_urls = ['https://alexa.com/topsites/']

    def parse(self, response):
        """
        :param : response
        :return : SiteRankItems
        """
        for p in response.css('div.listings.table > div.tr.site-listing'):
            # print(p)
            #아이템 객체 생성
            item = SiteRankItems()
            item['rank_num'] = p.css('div:nth-child(1)::text').get()
            item['site_name'] = p.css('div:nth-child(2) > p > a::text').get()
            item['daily_time_site'] = p.css('div:nth-child(3) > p::text').get()
            item['daily_page_view']=p.css('div:nth-child(4) > p::text').get()
            print(item)
            yield item
