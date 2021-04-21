# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem

class TestSpiderPipeline:
    # 최초 1회 실행
    def open_spider(self, spider):
        spider.logger.info('TestSpider Pipeline Started ')

    def process_item(self, item, spider):
        if int(item.get('rank_num')) < 41:
            item['is_pass'] = True
            return item

        else:
            raise DropItem('Dropped Item. Because This Site Rank is {}'.format(item.get('rank_number')))
            # print('Sorry, Dropped')
    # 마지막 1회 실행
    def close_spider(self, spider ):
        spider.logger.info('TestSpider Pipeline Closed')
