from playwright.async_api import async_playwright

async def render_tweet_to_image(tweet_url, output_path):
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto(f"https://publish.twitter.com/?query={tweet_url}&widget=Tweet")
        await page.wait_for_selector("iframe", timeout=10_000)
        frame = await page.frame_locator("iframe").first.content_frame()
        tweet = await frame.locator("body").screenshot(path=output_path)
        await browser.close()
