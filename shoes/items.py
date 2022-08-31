# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ShoesItem(scrapy.Item):
    product_title = scrapy.Field()
    stock_status = scrapy.Field()
    release_date = scrapy.Field()
    price = scrapy.Field()
    brand = scrapy.Field()
    model = scrapy.Field()
    style_code = scrapy.Field()
    image_url = scrapy.Field()
