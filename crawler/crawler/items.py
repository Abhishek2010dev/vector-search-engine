# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlerItem(scrapy.Item):
    id = scrapy.Field()
    url = scrapy.Field()
    title = scrapy.Field()
    section_type = scrapy.Field()
    text = scrapy.Field()
    headings_context = scrapy.Field()
    language = scrapy.Field()
    crawl_time = scrapy.Field()
    pass
