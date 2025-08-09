# build_embeds.py
from pathlib import Path
import json, time, requests
import csv
import os
import sys

# Add the absolute path to central-pipeline to sys.path
central_pipeline_path = os.path.abspath(os.path.join(os.path.dirname(__file__),  '..','central-pipeline'))
sys.path.append(central_pipeline_path)
from indxyz_utils.tweet_to_image_tools import extract_tweet_id 
from indxyz_utils.tweet_to_image_tools import fetch_oembed_html, save_html_as_image



TWEET_IDS = []
with open('data/toptweets.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
        html_l1=fetch_oembed_html(row[2])
        html_l2 = f"""
            <html>
            <head>
                <meta charset="UTF-8">
                <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
            </head>
            <body>{html_l1}</body>
            </html>
        """
        TWEET_IDS.append(html_l2)

OUT = Path("data/tweets.json")
#print(TWEET_IDS)
OUT.write_text(json.dumps(TWEET_IDS, indent=2))


