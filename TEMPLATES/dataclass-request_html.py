from dataclasses import dataclass, asdict
from requests_html import HTMLSession
from typing import Optional

@dataclass
class Item:
    name: str
    price: float
    sku: str
    attributes: Optional[list[str]] = None

def get_data():
    url = "https://www.fxpedalplanet.co.uk/product/dirty-haggard-audio-797-overdrive-effects-pedal"
    session = HTMLSession()
    resp = session.get(url)
    return resp

def parse_data(response):
    product = Item(
        name = response.html.find("h1")[0].text,
        price = response.html.find("p.prod-price")[0].text,
        sku = response.html.find("h2.prod-title")[0].text,
        attributes = [item.text for item in response.html.find("div.medium-6.cell li")],
    )
    return product

def main():
    html = get_data()
    pedal = parse_data(html)
    print(asdict(pedal))

if __name__ == "__main__":
    main()