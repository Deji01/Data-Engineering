from datetime import datetime
import json
import os
import requests


headers = {
    'Cookie': '__cf_bm=JOO0duaKpdWVlbBYWMUWk0IrY8oKnWQaTmv.g69UkhM-1661968626-0-AX1dTVxlCPvEdS/fafAM3No8iM7ZOhY9pZvxe/mLsjF6O4sKXWpdcNe0m6OuZlxVcYR+xRSUDXQORORUiCY5WJs='
}

step = 1

curr = os.getcwd()

data_dir = os.path.join(curr, "data")

for i in range(1, 26):
    url = f"https://stockx.com/api/browse?&page={i}&_search=nike%20dunk&dataType=product&propsToRetrieve[][]=id&propsToRetrieve[][]=uuid&propsToRetrieve[][]=childId&propsToRetrieve[][]=title&propsToRetrieve[][]=media.thumbUrl&propsToRetrieve[][]=media.smallImageUrl&propsToRetrieve[][]=urlKey&propsToRetrieve[][]=productCategory&propsToRetrieve[][]=releaseDate&propsToRetrieve[][]=market.lowestAsk&propsToRetrieve[][]=market.highestBid&propsToRetrieve[][]=brand&propsToRetrieve[][]=colorway&propsToRetrieve[][]=condition&propsToRetrieve[][]=description&propsToRetrieve[][]=shoe&propsToRetrieve[][]=retailPrice&propsToRetrieve[][]=market.lastSale&propsToRetrieve[][]=market.lastSaleValue&propsToRetrieve[][]=market.lastSaleDate&propsToRetrieve[][]=market.bidAskData&propsToRetrieve[][]=market.changeValue&propsToRetrieve[][]=market.changePercentage&propsToRetrieve[][]=market.salesLastPeriod&propsToRetrieve[][]=market.volatility&propsToRetrieve[][]=market.pricePremium&propsToRetrieve[][]=market.averageDeadstockPrice&propsToRetrieve[][]=market.salesThisPeriod&propsToRetrieve[][]=market.deadstockSold&propsToRetrieve[][]=market.lastHighestBidTime&propsToRetrieve[][]=market.lastLowestAskTime&propsToRetrieve[][]=market.salesInformation&facetsToRetrieve[]=%7B%7D"

    response = requests.get(url, headers=headers)

    result = response.json()

    filename = f"stockx-{datetime.now().strftime('%d-%m-%Y')}-file-{step}.json"

    with open(f"{data_dir}/{filename}", "w", encoding='utf-8') as f:
        json.dump(result, f)

    print(f'Step {step} Done!!!')
    step += 1
