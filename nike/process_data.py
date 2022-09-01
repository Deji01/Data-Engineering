import json
from datetime import datetime


def transform(file):
    with open(file, "r") as f:
        data = json.load(f)

    date = datetime.today().strftime("%d-%m-%Y")
    search_term = data["data"]["products"]["pages"]["searchSummary"]["originalTerms"]

    for product in data["data"]["products"]["products"]:
        id = product["id"]
        pid = product["pid"]
        product_id = product["cloudProductId"]
        product_instance_id = product["productInstanceId"]
        product_type = product["producType"]
        title = product["title"]
        subtitle = product["subtitle"]
        color_description = product["colorDescription"]
        currency = product["price"]["currency"]
        current_price = product["price"]["currentPrice"]
        discounted = product["price"]["discounted"]
        employee_price = product["price"]["employeePrice"]
        full_price = product["price"]["fullPrice"]
        minimum_advertised_price = product["price"]["minimumAdvertisedPrice"]
        label = product["label"]
        in_stock = product["inStock"]
        is_coming_soon = product["isComingSoon"]
        is_best_seller = product["isBestSeller"]
        is_excluded = product["isExcluded"]
        is_gift_card = product["isGiftCard"]
        is_jersey = product["isJersey"]
        is_launch = product["isLaunch"]
        is_member_exclusive = product["isMemberExclusive"]
        is_nba = product["isNBA"]
        is_nfl = product["isNFL"]
        is_sustainable = product["isSustainable"]
        has_extended_sizing = product["hasExtendedSizing"]
        customizable = product["customizable"]
        portrait_url = product["images"]["portraitURL"]
        squarish_url = product["images"]["squarishURL"]
        url = product["url"]

        yield (
            date,
            id,
            pid,
            product_id,
            product_instance_id,
            product_type,
            title,
            subtitle,
            color_description,
            currency,
            current_price,
            discounted,
            employee_price,
            full_price,
            minimum_advertised_price,
            label,
            in_stock,
            is_coming_soon,
            is_best_seller,
            is_excluded,
            is_gift_card,
            is_jersey,
            is_launch,
            is_member_exclusive,
            is_nba,
            is_nfl,
            is_sustainable,
            has_extended_sizing,
            customizable,
            search_term,
            portrait_url,
            squarish_url,
            url,
        )
