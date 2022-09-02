import scrapy
from ..items import ShoesItem
from scrapy.loader import ItemLoader

class SolesupplierSpider(scrapy.Spider):
    name = 'solesupplier'
    allowed_domains = ['thesolesupplier.co.uk']
    start_urls = ['https://thesolesupplier.co.uk/release-dates/?q=dunk']

    links = [f'https://thesolesupplier.co.uk/release-dates/?page={i}&q=dunk' for i in range(2, 44)]
    for link in links:
        start_urls.append(link)

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
            obj = ItemLoader(item=ShoesItem(), selector=item)
            obj.add_css("product_title", "div.product__info > h1::text")
            obj.add_css("stock_status", "div.product__info > div.product__header-row > div > strong::text")
            obj.add_css("price", "div.product__info > div.product__header-row > div > div > div.product__price > span > span::text")
            obj.add_css("image_url", "div.product__gallery > div > div.carousel--product > div > div > div > div.slick-slide.slick-active.slick-current > div > figure > picture > img::attr(src)")
            obj.add_css("release_date", "article > div > div.product-footer > section > div:nth-child(1) > p > span::text")
            obj.add_css("brand", "article > div > div.product-footer > section > div:nth-child(3) > p::text")
            obj.add_css("model", "article > div > div.product-footer > section > div:nth-child(4) > p::text")
            obj.add_css("style_code", "article > div > div.product-footer > section > div:nth-child(5) > p::text")
            
            yield obj.load_item()
            
            

