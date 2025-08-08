import streamlit as st
import streamlit.components.v1 as components
import csv
import base64
import os
import re
import sys
import json

def main():
    # Add the absolute path to central-pipeline to sys.path
    central_pipeline_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..', 'central-pipeline'))
    sys.path.append(central_pipeline_path)
    from indxyz_utils.widgetbox import main as wb
    from indxyz_utils.tweet_to_image_tools import get_base64_image, extract_tweet_id



    #########SOCIAL MEDIA POST IMAGES
    # === Dummy Data Refresh (on every interaction) ===
    tweet_list=[]
    with open('data/toptweets.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            tweet_list.append(row)

    tweet_img64=[]
    for idlist in tweet_list:
        tweet_id=extract_tweet_id(idlist[0])
        tweet_img64.append(get_base64_image(f"images/social/tweet_{tweet_id}.png"))



    html_parts = [wb(" Social Conversation", "twitter")]

    html_parts.append("""
    <ul style="padding-left: 18px; margin: 0;">
    <ol style="margin-left: -30px; margin-bottom: 10px;" type="1">
    """)


    html_parts  = [wb(" Social Conversation", "twitter")]
   
    # Append content inside the scrollable area
    #for cnt, (title, desc, link) in enumerate(tweet_list[:10]):
    for img in tweet_img64:
        #base64_img = tweet_img64[cnt]
        html_parts.append(f"""
            <div style='margin-bottom: 20px;'>
                <img src="data:image/png;base64,{img}" width="300">
            </div>
        """)
                # <br>
                # <a class="source-link" href="https://www.{link}" target="_blank">link</a>

    # Close the inner scrollable container and outer box
    html_parts.append("</div></div>")

    return("".join(html_parts))


if __name__ == "__main__":
    main()