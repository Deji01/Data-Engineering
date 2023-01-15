import pandas as pd
import requests
import os

# Read the dataset
df = pd.read_csv("logo-crypto-links.csv")

# Create a folder to save the images
if not os.path.exists("img"):
    os.makedirs("img")

# Iterate through each row of the dataset
for index, row in df.iterrows():
    icon_url = row["logo"]
    name = row["name"]
    response = requests.get(icon_url)
    open(f"img/{name}.png", "wb").write(response.content)
