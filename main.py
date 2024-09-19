from firecrawl import FirecrawlApp
from pydantic import BaseModel
from typing import List
from openai import OpenAI
from dotenv import load_dotenv
import pandas as pd
import json
import os

load_dotenv()

# scrape data from pages 1 to 5

pages = range(1, 5)

items = []

for page in pages:

    app = FirecrawlApp(api_key=os.getenv('FIRECRAWL_API_KEY'))

    url = "https://www.python-unlimited.com/webscraping/hotels.php?page="+str(page)

    # store the page content in the variable page_content

    page_content = app.scrape_url(url=url)

    # initiate OpenAI

    client = OpenAI()

    # provide a list with output fields

    fields = ["hotel_name", "hotel_location", "hotel_rating"]

    system_prompt = "You are a helpful assistant. You receive a scraped webpage, and you extract the items and return them in valid JSON. You return a list with all fields."

    user_prompt = f"""
    The extracted webpage: {page_content}
    The fields you return: {fields}
    """

    # extract the data with OpenAI

    completion = client.chat.completions.create(
      model="gpt-4o",
      response_format={"type": "json_object"},
      temperature=0,
      messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
      ]
    )

    # decode JSON data

    data = json.loads(completion.choices[0].message.content)

    # if it exists, remove the dictionary item

    keys = list(data.keys())
    number_of_keys = len(keys)

    if(number_of_keys == 1):
        data=data[keys[0]]

    # add all items 

    for single_item in data:
        items.append(single_item)

    break


df = pd.DataFrame(items)
df.to_excel("hotels.xlsx", index=False)
df.to_csv("hotels.csv", index=False)
