import json
from datetime import datetime

def transform(file):
    with open(file, "r") as f:
        data = json.load(f)

    date = datetime.today().strftime("%d-%m-%Y")

    for product in data["Products"]:
        id = product["id"]
        uuid = product["uuid"]
        shoe = product["shoe"]
        title = product["title"]
        brand = product["brand"]
        colorway = product["colorway"]
        condition = product["condition"]
        description = product["description"].replace("\n<br>","").replace("\n"," ")
        product_category = product["productCategory"]
        release_date = product["releaseDate"]
        retail_price = product["retailPrice"]
        lowest_ask = product["market"]["lowestAsk"]
        sales_this_period = product["market"]["salesThisPeriod"]
        sales_last_period = product["market"]["salesLastPeriod"]
        highest_bid = product["market"]["highestBid"]
        volatility = product["market"]["volatility"]
        deadstock_sold = product["market"]["deadstockSold"]
        price_premium = product["market"]["pricePremium"]
        average_deadstock_price = product["market"]["averageDeadstockPrice"]
        last_sale = product["market"]["lastSale"]
        change_value = product["market"]["changeValue"]
        change_percentage = product["market"]["changePercentage"]
        lastLowest_ask_time = product["market"]["lastLowestAskTime"]
        lastHighest_bid_time = product["market"]["lastHighestBidTime"]
        last_sale_date = product["market"]["lastSaleDate"]
        urlKey = product["urlKey"]
        small_image_url = product["media"]['smallImageUrl']
        thumb_url = product["media"]['thumbUrl']

        yield (
            date,
            id,
            uuid,
            shoe,
            title,
            brand,
            colorway,
            condition,
            description,
            product_category,
            release_date,
            retail_price,
            lowest_ask,
            sales_this_period,
            sales_last_period,
            highest_bid,
            volatility,
            deadstock_sold,
            price_premium,
            average_deadstock_price,
            last_sale,
            change_value,
            change_percentage,
            lastLowest_ask_time,
            lastHighest_bid_time,
            last_sale_date,
            urlKey,
            small_image_url,
            thumb_url,
        )
