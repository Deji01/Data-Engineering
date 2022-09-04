import json

def transform(file):
    with open(file, "r") as f:
        data = json.load(f)

    search_term = data["data"]["products"]["pages"]["searchSummary"].get("originalTerms")

    for product in data["data"]["products"]["products"]:
        id = product.get("id")
        pid = product.get("pid")
        product_id = product.get("cloudProductId")
        product_instance_id = product.get("productInstanceId")
        product_type = product.get("producType")
        title = product.get("title")
        subtitle = product.get("subtitle")
        color_description = product.get("colorDescription")
        currency = product["price"].get("currency")
        current_price = product["price"].get("currentPrice")
        discounted = product["price"].get("discounted")
        employee_price = product["price"].get("employeePrice")
        full_price = product["price"].get("fullPrice")
        minimum_advertised_price = product["price"].get("minimumAdvertisedPrice")
        label = product.get("label")
        in_stock = product.get("inStock")
        is_coming_soon = product.get("isComingSoon")
        is_best_seller = product.get("isBestSeller")
        is_excluded = product.get("isExcluded")
        is_gift_card = product.get("isGiftCard")
        is_jersey = product.get("isJersey")
        is_launch = product.get("isLaunch")
        is_member_exclusive = product.get("isMemberExclusive")
        is_nba = product.get("isNBA")
        is_nfl = product.get("isNFL")
        is_sustainable = product.get("isSustainable")
        has_extended_sizing = product.get("hasExtendedSizing")
        customizable = product.get("customizable")
        portrait_url = product["images"].get("portraitURL")
        squarish_url = product["images"].get("squarishURL")
        url = product.get("url")

        yield (
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
            url
        )
