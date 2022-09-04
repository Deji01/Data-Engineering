import json


def transform(file):
    with open(file, "r") as f:
        data = json.load(f)

    for product in data["Products"]:
        id = product.get("id")
        uuid = product.get("uuid")
        shoe = product.get("shoe")
        title = product.get("title")
        brand = product.get("brand")
        colorway = product.get("colorway")
        condition = product.get("condition")
        description = (
            product.get("description").replace("\n<br>", "").replace("\n", " ")
        )
        product_category = product.get("productCategory")
        release_date = product.get("releaseDate")
        retail_price = product.get("retailPrice")
        lowest_ask = product["market"].get("lowestAsk")
        sales_this_period = product["market"].get("salesThisPeriod")
        sales_last_period = product["market"].get("salesLastPeriod")
        highest_bid = product["market"].get("highestBid")
        volatility = product["market"].get("volatility")
        deadstock_sold = product["market"].get("deadstockSold")
        price_premium = product["market"].get("pricePremium")
        average_deadstock_price = product["market"].get("averageDeadstockPrice")
        last_sale = product["market"].get("lastSale")
        change_value = product["market"].get("changeValue")
        change_percentage = product["market"].get("changePercentage")
        last_lowest_ask_time = product["market"].get("lastLowestAskTime")
        last_highest_bid_time = product["market"].get("lastHighestBidTime")
        last_sale_date = product["market"].get("lastSaleDate")
        url_key = product.get("urlKey")
        small_image_url = product["media"].get("smallImageUrl")
        thumb_url = product["media"].get("thumbUrl")

        yield (
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
            last_lowest_ask_time,
            last_highest_bid_time,
            last_sale_date,
            url_key,
            small_image_url,
            thumb_url,
        )
