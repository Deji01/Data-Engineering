import json
import os
import requests
from datetime import datetime


def extract():
    url = "https://ac.cnstrc.com/search/nike%20dunk?c=ciojs-client-2.29.2&key=key_XT7bjdbvjgECO5d8&i=b1f2bb9e-2bd1-49a8-865d-75557d8f8e3c&s=4&page=1&num_results_per_page=60"

    headers = {
        "authority": "ac.cnstrc.com",
        "accept": "*/*",
        "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
        "cache-control": "no-cache",
        "origin": "https://www.goat.com",
        "pragma": "no-cache",
        "sec-ch-ua": '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
    }

    response = requests.get(url, headers=headers)
    result = response.json()

    step = 1

    filename = f"goat-{datetime.now().strftime('%d-%m-%Y')}-file-{step}.json"
    curr = os.getcwd
    data_dir = os.path.join(curr, "data")

    with open(f"{data_dir}/{filename}", "w", encoding="utf-8") as f:
        json.dump(result, f)

    i = 1

    while requests.get(url, headers=headers).text is not None:
        i += 1
        step += 1

        url = f"https://ac.cnstrc.com/search/nike%20dunk?c=ciojs-client-2.29.2&key=key_XT7bjdbvjgECO5d8&i=b1f2bb9e-2bd1-49a8-865d-75557d8f8e3c&s=4&page={i}&num_results_per_page=60"

        response = requests.get(url, headers=headers)
        result = response.json()

        filename = f"goat-{datetime.now().strftime('%d-%m-%Y')}-file-{step}.json"
        with open(f"{data_dir}/{filename}", "w", encoding="utf-8") as f:
            json.dump(result, f)

        print(f"Step {step} Done!!!")

if __name__ == "__main__":
    extract()
