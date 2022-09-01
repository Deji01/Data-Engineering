import json
from datetime import datetime

file = "/workspaces/Data-Engineering/goat/data/goat-01-09-2022-file-1.json"


def transform(file):
    with open(file, "r") as f:
        data = json.load(f)

    date = datetime.today().strftime("%d-%m-%Y")

    for product in data["response"]["results"]:
        matched_terms = " ".join(product["matched_terms"])
        id = product["data"]["id"]
        variation_id = product["data"]["variation_id"]
        sku = product["data"]["sku"]
        slug = product["data"]["slug"]
        color = product["data"]["color"]
        category = product["data"]["category"]
        release_date = product["data"]["release_date"]
        release_date_year = product["data"]["release_date_year"]
        value = product["value"]
        product_type = product["data"]["product_type"]
        product_condition = product["data"]["product_condition"]
        count_for_product_condition = product["data"]["count_for_product_condition"]
        retail_price_cents = product["data"]["retail_price_cents"]
        retail_price_cents_gbp = product["data"]["retail_price_cents_gbp"]
        retail_price_cents_twd = product["data"]["retail_price_cents_twd"]
        retail_price_cents_cad = product["data"]["retail_price_cents_cad"]
        retail_price_cents_hkd = product["data"]["retail_price_cents_hkd"]
        retail_price_cents_sgd = product["data"]["retail_price_cents_sgd"]
        retail_price_cents_krw = product["data"]["retail_price_cents_krw"]
        retail_price_cents_cny = product["data"]["retail_price_cents_cny"]
        retail_price_cents_aud = product["data"]["retail_price_cents_aud"]
        retail_price_cents_jpy = product["data"]["retail_price_cents_jpy"]
        retail_price_cents_eur = product["data"]["retail_price_cents_eur"]
        lowest_price_cents = product["data"]["lowest_price_cents"]
        lowest_price_cents_krw = product["data"]["lowest_price_cents_krw"]
        lowest_price_cents_aud = product["data"]["lowest_price_cents_aud"]
        lowest_price_cents_cad = product["data"]["lowest_price_cents_cad"]
        lowest_price_cents_cny = product["data"]["lowest_price_cents_cny"]
        lowest_price_cents_sgd = product["data"]["lowest_price_cents_sgd"]
        lowest_price_cents_gbp = product["data"]["lowest_price_cents_gbp"]
        lowest_price_cents_eur = product["data"]["lowest_price_cents_eur"]
        lowest_price_cents_hkd = product["data"]["lowest_price_cents_hkd"]
        lowest_price_cents_jpy = product["data"]["lowest_price_cents_jpy"]
        lowest_price_cents_twd = product["data"]["lowest_price_cents_twd"]
        instant_ship_lowest_price_cents = product["data"][
            "instant_ship_lowest_price_cents"
        ]
        instant_ship_lowest_price_cents_eur = product["data"][
            "instant_ship_lowest_price_cents_eur"
        ]
        instant_ship_lowest_price_cents_gbp = product["data"][
            "instant_ship_lowest_price_cents_gbp"
        ]
        instant_ship_lowest_price_cents_twd = product["data"][
            "instant_ship_lowest_price_cents_twd"
        ]
        instant_ship_lowest_price_cents_sgd = product["data"][
            "instant_ship_lowest_price_cents_sgd"
        ]
        instant_ship_lowest_price_cents_hkd = product["data"][
            "instant_ship_lowest_price_cents_hkd"
        ]
        instant_ship_lowest_price_cents_cny = product["data"][
            "instant_ship_lowest_price_cents_cny"
        ]
        instant_ship_lowest_price_cents_jpy = product["data"][
            "instant_ship_lowest_price_cents_jpy"
        ]
        instant_ship_lowest_price_cents_cad = product["data"][
            "instant_ship_lowest_price_cents_cad"
        ]
        instant_ship_lowest_price_cents_krw = product["data"][
            "instant_ship_lowest_price_cents_krw"
        ]
        instant_ship_lowest_price_cents_aud = product["data"][
            "instant_ship_lowest_price_cents_aud'"
        ]
        image_url = product["data"]["image_url"]
        used_image_url = product["data"]["used_image_url"]

        return (
            date,
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
