import scrapy
from datetime import datetime

class SolesupplierSpider(scrapy.Spider):
    name = 'solesupplier'
    allowed_domains = ['thesolesupplier.co.uk']
    start_urls = ['https://thesolesupplier.co.uk/release-dates/?q=low%20dunk']

    def parse(self, response):
        for div in response.css("#main-content > div > div.advanced-listing-view > div.desktop-flex.advanced-listing-view__wrapper > section.md-10.advanced-listing-view__feed > div > article "):
            url =  div.css("a.card__main-link::attr(href)").get()
            url = response.urljoin(url)
            yield scrapy.Request(url=url, callback=self.parse_item)
        next_page = response.css("#main-content > div > div.advanced-listing-view > div.desktop-flex.advanced-listing-view__wrapper > section.advanced-listing-view__pagination > ul > li:nth-child(4) > a::attr(href)").get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(url=next_page, callback=self.parse)
            
    def parse_item(self, response):        
        for item in response.css("#main-content > div > div > article.product > div > div > section.product__trunk"):
            product_title = item.css("div.product__info > h1::text").get()
            stock_status = item.css("div.product__info > div.product__header-row > div > strong::text").get()
            price = item.css("div.product__info > div.product__header-row > div > div > div.product__price > span > span::text").get()
            image_url = item.css("div.product__gallery > div > div.carousel--product > div > div > div > div.slick-slide.slick-active.slick-current > div > figure > picture > img::attr(src)").get()
            release_date = item.css("article > div > div.product-footer > section > div:nth-child(1) > p > span::text").get()
            brand = item.css("article > div > div.product-footer > section > div:nth-child(3) > p::text").get()
            model = item.css("article > div > div.product-footer > section > div:nth-child(4) > p::text").get()
            style_code = item.css("article > div > div.product-footer > section > div:nth-child(5) > p::text").get()
            
            yield {
                "product_title" : product_title,
                "stock_status" : stock_status,
                "release_date" : release_date,
                "price" : price,
                "brand" : brand,
                "model" : model,
                "style_code" : style_code,
                "image_url": image_url,
                "date" : datetime.today()
            }

