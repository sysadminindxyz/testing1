# render_tweet_to_image.py

import asyncio
import argparse
from pathlib import Path
from playwright.async_api import async_playwright

async def render_tweet_to_image(tweet_url, output_path):
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        print(f"📸 Capturing: {tweet_url}")
        await page.goto(f"https://publish.twitter.com/?query={tweet_url}&widget=Tweet")
        await page.wait_for_selector("iframe", timeout=10_000)

        # Grab the iframe and screenshot just the embedded tweet
        frame = await page.frame_locator("iframe").first.content_frame()
        tweet = await frame.locator("body").screenshot(path=output_path)
        await browser.close()
        print(f"✅ Saved to {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--tweet-url", type=str, required=True)
    parser.add_argument("--output", type=str, default="tweet.png")
    args = parser.parse_args()

    asyncio.run(render_tweet_to_image(args.tweet_url, args.output))
