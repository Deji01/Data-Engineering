from itemloaders.processors import MapCompose, TakeFirst
from w3lib.html import remove_tags
import scrapy

class ShoesItem(scrapy.Item):

    def clean_price(value):
        return round(float(value.replace("£", "")), 2)

    product_title = scrapy.Field(input_processor = MapCompose(remove_tags),output_processor = TakeFirst())
    stock_status = scrapy.Field(input_processor = MapCompose(remove_tags),output_processor = TakeFirst())
    release_date = scrapy.Field(input_processor = MapCompose(remove_tags),output_processor = TakeFirst())
    price = scrapy.Field(input_processor = MapCompose(remove_tags),output_processor = [TakeFirst(), MapCompose(clean_price)])
    brand = scrapy.Field(input_processor = MapCompose(remove_tags),output_processor = TakeFirst())
    model = scrapy.Field(input_processor = MapCompose(remove_tags),output_processor = TakeFirst())
    style_code = scrapy.Field(input_processor = MapCompose(remove_tags),output_processor = TakeFirst())
    image_url = scrapy.Field(output_processor = TakeFirst())
