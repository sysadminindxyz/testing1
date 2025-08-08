import csv
import os
import sys


# Add the absolute path to central-pipeline to sys.path
central_pipeline_path = os.path.abspath(os.path.join(os.path.dirname(__file__),  '..','central-pipeline'))
sys.path.append(central_pipeline_path)
from indxyz_utils.tweet_to_image_tools import extract_tweet_id 
from indxyz_utils.tweet_to_image_tools import fetch_oembed_html, save_html_as_image

# --- Load tweet list from CSV ---
tweet_list = []
with open('data/toptweets.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
        tweet_list.append(row)

# Optional: Limit to top N
#print(tweet_list)

for tweet in tweet_list:
    tweet_url=tweet[0]
    print(tweet_url)
    tweet_id = extract_tweet_id(tweet_url)
    html = fetch_oembed_html(tweet_url)
    image_name = f"tweet_{tweet_id}.png"
    image_path = os.path.join("images/social", image_name)
    save_html_as_image(html, image_path)
