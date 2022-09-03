import re

def useRegex(input):
    pattern = re.compile(r"^[a-zA-Z]{2,3}[0-9]{3,4}[-][0-9]{3,4}$", re.IGNORECASE)
    return bool(pattern.match(input))


def clean_price(value):
        return round(float(value.replace("£", "")), 2)

# print(useRegex("DO2321-111"))
# print(useRegex("DO2521-113"))
# print(useRegex("Runstar Hike"))

print(clean_price("£ 1355.4555"))

# SQL QUERY
query_1 = """
        UPDATE sole_supplier 
        SET style_code = model , model = style_code
        WHERE model <> 'Dunk' AND model ~ '^[a-zA-Z]{2,3}[0-9]{3,4}[-][0-9]{3,4}$' AND style_code is NULL;
        """
query_2 = """
        UPDATE sole_supplier 
        SET style_code = model , model = style_code
        WHERE model <> 'Dunk' AND model ~ '^[0-9]{6}[-][0-9]{3,4}$' AND style_code is NULL;
        """
query_3 = """
        UPDATE sole_supplier 
        SET brand = 'Nike' , model = 'Dunk'
        WHERE brand = 'Dunk';
        """
query_4 = """
        DELETE FROM sole_supplier
        WHERE brand <> 'Nike';
        """
query_5 = """
        DELETE FROM sole_supplier
        WHERE price(£) IS NULL;
        """








