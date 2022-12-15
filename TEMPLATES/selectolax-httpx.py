import csv
import httpx
from dataclasses import dataclass, asdict
from selectolax.parser import HTMLParser

@dataclass
class Product:
    manufacturer: str
    title: str
    price: str

def get_html(page):
    url = "https://www.thomann.de/gb/search_GF_electric_guitars.html?ls=100&pg={page}&hl=BLOWOUT"
    response = httpx.get(url)
    return HTMLParser(response.text)

def parse_products(html):
    products = html.css("div.product")
    results = []

    for item in products:
        new_item = Product(
	    manufacturer = item.css_first("span.title__manufacturer").text(),
	    title = item.css_first("span.title__name").text(),
	    price = item.css_first("div.product__price").text().strip()
        )
	results.append(asdict(new_item))
    return results

def to_csv(res):
    with open("results.csv", "a") as f:
        writer = csv.DictWriter(f, fieldnames=["manufacturer", "title", "price"])
	writer.writerows(res)

def main():
    # get html page(s)
    for x in range(1, 4):
        html = get_html(1)
        res = parse_products(html)
	to_csv(res)

if __name__ == "__main__":
    main()