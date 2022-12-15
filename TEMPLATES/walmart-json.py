import requests
import json
import pandas as pd
import time

def get_data(page):
    url = f"https://www.walmart.com/cp/api/get-deals=list?prg=desktop&deals=christmas-gifts&ps=60&page={page}&sort=new"

    headers = {
      "authority": "www.walmart.com",
      "client-ip": "",
      "accept": "application/json",
      "cid": "undefined",
      "useragent": "undefined",
      "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.42",
      "content-type": "application/json",
      "sec-fetch-site": "same-origin",
      "sec-fetch-mode": "cors",
      "sec-fetch-dest": "empty",
      "referer": "https://www.walmart.com/m/christmas-gifts?page=2&ps=60&sort=new",
      "accept-language": "en-US,en;q=0.9",
      "cookie": ""
       }

    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    return data

if __name__ == "__main__":
    products = pd.DataFrame([])
    for page in range(10):
        data = get_data(page)
        products = products.append(pd.json_normalize(data["items"]), ignore_index=True)
        time.sleep(1)
        print(f"Getting Page {page} waiting..."

products.to_csv("walmart_products.csv")

