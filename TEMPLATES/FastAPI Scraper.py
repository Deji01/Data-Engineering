from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup

app = FastAPI()

@app.get("/{asin}")
async def get_data(asin:str):
    session = requests.Session()

    user_agent = "Mozilla/5.0 (X11; Linux x88_64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
 
    session.headers.update({"User-Agent":user_agent})

    response = session.get(f"https://amazon.co.uk/dp/{asin}")

    if response.status_code != 200:
        return {"error": f"bad status code {response.status_code}"}

    soup = BeautifulSoup(response.text, "html.parser")

    try:
        data = {
            "asin": asin,
            "name": soup.select_one("h1#title").text.strip(),
            "price": soup.select_one("span.a-offscreen").text,
            }
        return {"results": data}
    except IndexError:
        return {"error": "Unable to parse page"}



# uvicorn main:app --reload
