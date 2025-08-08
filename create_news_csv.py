import csv
import os
import sys
from playwright.async_api import async_playwright
import asyncio
import pandas as pd
from concurrent.futures import ThreadPoolExecutor


# Add the absolute path to central-pipeline to sys.path
central_pipeline_path = os.path.abspath(os.path.join(os.path.dirname(__file__),  '..','central-pipeline'))
sys.path.append(central_pipeline_path)

from indxyz_utils.news_info_from_link_tools import fetch_article_info  # async

async def _fetch_all_async(links):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        try:
            tasks = [fetch_article_info(link, browser) for link in links]
            return await asyncio.gather(*tasks, return_exceptions=False)
        finally:
            await browser.close()

def fetch_all_sync_in_worker(links):
    return asyncio.run(_fetch_all_async(links))

# run the async pipeline in a dedicated thread (separate event loop)

df = pd.read_csv("data/news.csv")
links = df["Link"].dropna().tolist()

with ThreadPoolExecutor(max_workers=1) as pool:
    results = pool.submit(fetch_all_sync_in_worker, links).result()

print(results)

with open("data/news_prepped.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(results)