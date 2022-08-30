import requests
import json

url = "https://product-proxy-v2.adtech-prod.nikecloud.com/products"

payload = json.dumps({
  "experienceProducts": [
    {
      "cloudProductId": "eb0949f4-7f19-5b6a-9631-6f779b3369f1",
      "currentPrice": 190
    },
    {
      "cloudProductId": "89f203c5-b169-531f-be87-fd77f4105f90",
      "currentPrice": 180
    },
    {
      "cloudProductId": "37c841d0-caed-5aa1-8125-928fcda25ed0",
      "currentPrice": 150
    },
    {
      "cloudProductId": "7ad40567-879e-5999-8f55-9743de13ccd4",
      "currentPrice": 140
    },
    {
      "cloudProductId": "0d06a88a-6606-57cb-8dfd-afec9494a8f6",
      "currentPrice": 200
    },
    {
      "cloudProductId": "e57c5228-fab9-563f-8113-3412f6d6d24b",
      "currentPrice": 200
    },
    {
      "cloudProductId": "30694dee-8fb4-5e23-a8be-02dc261bc7b0",
      "currentPrice": 110
    },
    {
      "cloudProductId": "8c60b5ca-e612-5b86-a094-2532aa3b68c6",
      "currentPrice": 130
    },
    {
      "cloudProductId": "e5469991-fb4d-5e1b-aa3d-f9f5f0dc7b31",
      "currentPrice": 135
    },
    {
      "cloudProductId": "a07b42af-7069-58c6-8519-d7f85f654082",
      "currentPrice": 125
    },
    {
      "cloudProductId": "54c97ad5-3e2d-579f-9071-fb0053162774",
      "currentPrice": 160
    },
    {
      "cloudProductId": "24a8c897-06be-588a-ba3b-1e5676a41505",
      "currentPrice": 150
    },
    {
      "cloudProductId": "0ef6f73f-055c-556f-973f-4e587c0d718f",
      "currentPrice": 130
    },
    {
      "cloudProductId": "bf7e117f-6b7b-55c2-a6f1-dd1389f5dbbf",
      "currentPrice": 140
    },
    {
      "cloudProductId": "cc723357-7ce6-5b07-89b2-ee349c91485f",
      "currentPrice": 105
    },
    {
      "cloudProductId": "cf9be361-6d7a-5afe-86e7-716479d4a121",
      "currentPrice": 105
    },
    {
      "cloudProductId": "09e0d404-f3f8-5b1e-a504-6baf88ac59cf",
      "currentPrice": 210
    },
    {
      "cloudProductId": "94d3987e-b47f-508a-afcd-47b230eccc7d",
      "currentPrice": 210
    },
    {
      "cloudProductId": "18251c5a-5cd4-5465-8929-041df08d9d1c",
      "currentPrice": 165
    },
    {
      "cloudProductId": "c5aec9ef-e0d5-531b-9625-a2673bcb1dfa",
      "currentPrice": 130
    },
    {
      "cloudProductId": "22a7c9f1-2b8b-51aa-8794-a6ffc525ac61",
      "currentPrice": 110
    },
    {
      "cloudProductId": "9ddb5691-5264-5682-91b4-d4f0629a1c73",
      "currentPrice": 110
    },
    {
      "cloudProductId": "7e6a2e4c-3575-528f-bbf2-24d7cf723cc2",
      "currentPrice": 160
    },
    {
      "cloudProductId": "055a4593-fd17-5602-9b0f-3833f048fca9",
      "currentPrice": 180
    }
  ],
  "country": "us"
})
headers = {
  'authority': 'product-proxy-v2.adtech-prod.nikecloud.com',
  'accept': '*/*',
  'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
  'cache-control': 'no-cache',
  'content-type': 'application/json',
  'origin': 'https://www.nike.com',
  'pragma': 'no-cache',
  'referer': 'https://www.nike.com/',
  'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'cross-site',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}

response = requests.post(url, headers=headers, data=payload)

print(response.text)
