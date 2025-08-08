import streamlit as st
import streamlit.components.v1 as components
#import playwright
from playwright.async_api import async_playwright
import asyncio

import csv
#import base64
import os
#import re
import sys
#import json
import pandas as pd

async def main():
    # Add the absolute path to central-pipeline to sys.path
    central_pipeline_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..', 'central-pipeline'))
    sys.path.append(central_pipeline_path)
    from indxyz_utils.widgetbox import main as wb
    from indxyz_utils.news_info_from_link_tools import fetch_article_info

    # Load CSV
    df = pd.read_csv("data/news.csv")
    links = df["link"].dropna().tolist()

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        tasks = [fetch_article_info(link, browser) for link in links]
        results = await asyncio.gather(*tasks)

    # Build HTML

    html_items = [wb(" Top Issues", "megaphone")]

    for article in filter(None, results):
        html_items.append(f"""
        <li>
          <strong>{article['headline']}</strong>
          <div style="margin-left:20px;">
            {article['paragraph']}<br>
            <a href="{article['link']}">{article['source']}</a>
          </div>
        </li>
        """)

    final_html = "<ul>" + "\n".join(html_items) + "</ul>"

    return(final_html)

if __name__ == "__main__":
    main()