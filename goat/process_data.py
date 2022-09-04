import json


def transform(file):
    with open(file, "r") as f:
        data = json.load(f)

    for product in data["response"]["results"]:
        matched_terms = " ".join(product["matched_terms"])
        id = product["data"].get("id")
        variation_id = product["data"].get("variation_id")
        sku = product["data"].get("sku")
        slug = product["data"].get("slug")
        color = product["data"].get("color")
        category = product["data"].get("category")
        release_date = product["data"].get("release_date")
        release_date_year = product["data"].get("release_date_year")
        value = product["value"]
        product_type = product["data"].get("product_type")
        product_condition = product["data"].get("product_condition")
        count_for_product_condition = product["data"].get("count_for_product_condition")
        retail_price_cents = product["data"].get("retail_price_cents")
        retail_price_cents_gbp = product["data"].get("retail_price_cents_gbp")
        retail_price_cents_twd = product["data"].get("retail_price_cents_twd")
        retail_price_cents_cad = product["data"].get("retail_price_cents_cad")
        retail_price_cents_hkd = product["data"].get("retail_price_cents_hkd")
        retail_price_cents_sgd = product["data"].get("retail_price_cents_sgd")
        retail_price_cents_krw = product["data"].get("retail_price_cents_krw")
        retail_price_cents_cny = product["data"].get("retail_price_cents_cny")
        retail_price_cents_aud = product["data"].get("retail_price_cents_aud")
        retail_price_cents_jpy = product["data"].get("retail_price_cents_jpy")
        retail_price_cents_eur = product["data"].get("retail_price_cents_eur")
        lowest_price_cents = product["data"].get("lowest_price_cents")
        lowest_price_cents_krw = product["data"].get("lowest_price_cents_krw")
        lowest_price_cents_aud = product["data"].get("lowest_price_cents_aud")
        lowest_price_cents_cad = product["data"].get("lowest_price_cents_cad")
        lowest_price_cents_cny = product["data"].get("lowest_price_cents_cny")
        lowest_price_cents_sgd = product["data"].get("lowest_price_cents_sgd")
        lowest_price_cents_gbp = product["data"].get("lowest_price_cents_gbp")
        lowest_price_cents_eur = product["data"].get("lowest_price_cents_eur")
        lowest_price_cents_hkd = product["data"].get("lowest_price_cents_hkd")
        lowest_price_cents_jpy = product["data"].get("lowest_price_cents_jpy")
        lowest_price_cents_twd = product["data"].get("lowest_price_cents_twd")
        instant_ship_lowest_price_cents = product["data"].get(
            "instant_ship_lowest_price_cents"
        )
        instant_ship_lowest_price_cents_eur = product["data"].get(
            "instant_ship_lowest_price_cents_eur"
        )
        instant_ship_lowest_price_cents_gbp = product["data"].get(
            "instant_ship_lowest_price_cents_gbp"
        )
        instant_ship_lowest_price_cents_twd = product["data"].get(
            "instant_ship_lowest_price_cents_twd"
        )
        instant_ship_lowest_price_cents_sgd = product["data"].get(
            "instant_ship_lowest_price_cents_sgd"
        )
        instant_ship_lowest_price_cents_hkd = product["data"].get(
            "instant_ship_lowest_price_cents_hkd"
        )
        instant_ship_lowest_price_cents_cny = product["data"].get(
            "instant_ship_lowest_price_cents_cny"
        )
        instant_ship_lowest_price_cents_jpy = product["data"].get(
            "instant_ship_lowest_price_cents_jpy"
        )
        instant_ship_lowest_price_cents_cad = product["data"].get(
            "instant_ship_lowest_price_cents_cad"
        )
        instant_ship_lowest_price_cents_krw = product["data"].get(
            "instant_ship_lowest_price_cents_krw"
        )
        instant_ship_lowest_price_cents_aud = product["data"].get(
            "instant_ship_lowest_price_cents_aud"
        )
        image_url = product["data"].get("image_url")
        used_image_url = product["data"].get("used_image_url")

        yield (
            matched_terms,
            id,
            variation_id,
            sku,
            slug,
            color,
            category,
            release_date,
            release_date_year,
            value,
            product_type,
            product_condition,
            count_for_product_condition,
            retail_price_cents,
            retail_price_cents_gbp,
            retail_price_cents_twd,
            retail_price_cents_cad,
            retail_price_cents_hkd,
            retail_price_cents_sgd,
            retail_price_cents_krw,
            retail_price_cents_cny,
            retail_price_cents_aud,
            retail_price_cents_jpy,
            retail_price_cents_eur,
            lowest_price_cents,
            lowest_price_cents_krw,
            lowest_price_cents_aud,
            lowest_price_cents_cad,
            lowest_price_cents_cny,
            lowest_price_cents_sgd,
            lowest_price_cents_gbp,
            lowest_price_cents_eur,
            lowest_price_cents_hkd,
            lowest_price_cents_jpy,
            lowest_price_cents_twd,
            instant_ship_lowest_price_cents,
            instant_ship_lowest_price_cents_eur,
            instant_ship_lowest_price_cents_gbp,
            instant_ship_lowest_price_cents_twd,
            instant_ship_lowest_price_cents_sgd,
            instant_ship_lowest_price_cents_hkd,
            instant_ship_lowest_price_cents_cny,
            instant_ship_lowest_price_cents_jpy,
            instant_ship_lowest_price_cents_cad,
            instant_ship_lowest_price_cents_krw,
            instant_ship_lowest_price_cents_aud,
            image_url,
            used_image_url,
        )
