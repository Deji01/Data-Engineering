import re

def useRegex(input):
    pattern = re.compile(r"^[a-zA-Z]{2,3}[0-9]{3,4}[-][0-9]{3,4}$", re.IGNORECASE)
    return bool(pattern.match(input))


def clean_price(value):
        return round(float(value.replace("£", "")), 2)

# print(useRegex("DO2321-111"))
# print(useRegex("DO2521-113"))
# print(useRegex("Runstar Hike"))

print(clean_price("£1355.4555"))