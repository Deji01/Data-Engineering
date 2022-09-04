create_table_query = """
    CREATE TABLE IF NOT EXISTS goat (
    date TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    matched_terms VARCHAR(20),
    id VARCHAR(50) NOT NULL PRIMARY KEY,
    variation_id VARCHAR(50),
    sku VARCHAR(20),
    slug VARCHAR(100),
    color VARCHAR(20),
    category VARCHAR(20),
    release_date INTEGER,
    release_date_year INTEGER,
    value VARCHAR(50),
    product_type VARCHAR(20),
    product_condition VARCHAR(20),
    count_for_product_condition INTEGER,
    retail_price_cents NUMERIC(10, 2),
    retail_price_cents_gbp NUMERIC(10, 2),
    retail_price_cents_twd NUMERIC(10, 2),
    retail_price_cents_cad NUMERIC(10, 2),
    retail_price_cents_hkd NUMERIC(10, 2),
    retail_price_cents_sgd NUMERIC(10, 2),
    retail_price_cents_krw NUMERIC(10, 2),
    retail_price_cents_cny NUMERIC(10, 2),
    retail_price_cents_aud NUMERIC(10, 2),
    retail_price_cents_jpy NUMERIC(10, 2),
    retail_price_cents_eur NUMERIC(10, 2),
    lowest_price_cents NUMERIC(10, 2),
    lowest_price_cents_krw NUMERIC(10, 2),
    lowest_price_cents_aud NUMERIC(10, 2),
    lowest_price_cents_cad NUMERIC(10, 2),
    lowest_price_cents_cny NUMERIC(10, 2),
    lowest_price_cents_sgd NUMERIC(10, 2),
    lowest_price_cents_gbp NUMERIC(10, 2),
    lowest_price_cents_eur NUMERIC(10, 2),
    lowest_price_cents_hkd NUMERIC(10, 2),
    lowest_price_cents_jpy NUMERIC(10, 2),
    lowest_price_cents_twd NUMERIC(10, 2),
    instant_ship_lowest_price_cents NUMERIC(10, 2),
    instant_ship_lowest_price_cents_eur NUMERIC(10, 2),
    instant_ship_lowest_price_cents_gbp NUMERIC(10, 2),
    instant_ship_lowest_price_cents_twd NUMERIC(10, 2),
    instant_ship_lowest_price_cents_sgd NUMERIC(10, 2),
    instant_ship_lowest_price_cents_hkd NUMERIC(10, 2),
    instant_ship_lowest_price_cents_cny NUMERIC(10, 2),
    instant_ship_lowest_price_cents_jpy NUMERIC(10, 2),
    instant_ship_lowest_price_cents_cad NUMERIC(10, 2),
    instant_ship_lowest_price_cents_krw NUMERIC(10, 2),
    instant_ship_lowest_price_cents_aud NUMERIC(10, 2),
    image_url VARCHAR(255),
    used_image_url VARCHAR(255),
    )
    """

insert_data_query = """
    INSERT INTO goat (
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
        used_image_url
        )
    VALUES (
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s,
        %s
    )
    """

