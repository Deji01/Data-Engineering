from itemloaders.processors import MapCompose, TakeFirst
from w3lib.html import remove_tags
import scrapy

def clean_price(value):
        conv_price = float(value.replace("£", "").replace(",", ""))
        return round(conv_price, 2)

class ShoesItem(scrapy.Item):

    

    product_title = scrapy.Field(input_processor = MapCompose(remove_tags),output_processor = TakeFirst())
    stock_status = scrapy.Field(input_processor = MapCompose(remove_tags),output_processor = TakeFirst())
    release_date = scrapy.Field(input_processor = MapCompose(remove_tags),output_processor = TakeFirst())
    price = scrapy.Field(input_processor = MapCompose(remove_tags, clean_price),output_processor = TakeFirst())
    brand = scrapy.Field(input_processor = MapCompose(remove_tags),output_processor = TakeFirst())
    model = scrapy.Field(input_processor = MapCompose(remove_tags),output_processor = TakeFirst())
    style_code = scrapy.Field(input_processor = MapCompose(remove_tags),output_processor = TakeFirst())
    image_url = scrapy.Field(output_processor = TakeFirst())
