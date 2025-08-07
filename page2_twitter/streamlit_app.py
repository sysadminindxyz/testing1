import json
import streamlit as st
from pathlib import Path
from streamlit import session_state as state
from streamlit.components.v1 import html

#from .dashboard import Dashboard, Editor, Card, DataGrid, Radar, Pie, Player
import feedparser


def main():
    st.set_page_config(layout="wide")

    st.write(
        """
        Trending Social Posts &nbsp;
        =====================

        """
    )

    # ✅ Embedded tweet (clean, working version)

    tweet_embed01 = """
    <blockquote class="twitter-tweet" data-theme="dark">
    <p lang="en" dir="ltr">This is exact same man one year apart. 
    <br><br>Before AND After. <br><br>Ozempic is a miracle. 
    <a href="https://twitter.com/search?q=%24NVO&amp;src=ctag&amp;ref_src=twsrc%5Etfw">$NVO</a> 
    <a href="https://t.co/7lzFhlQcb0">pic.twitter.com/7lzFhlQcb0</a></p>&mdash; tic toc (@TicTocTick) <a href="https://twitter.com/TicTocTick/status/1946911910311371042?ref_src=twsrc%5Etfw">July 20, 2025</a></blockquote>
    <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
    """

    tweet_embed = """
    <blockquote class="twitter-tweet" data-theme="dark">
      <p lang="en" dir="ltr">
        Mike Pompeo looks like a totally different person now.<br><br>Ozempic is wild
        <a href="https://t.co/9PIgngr7UR">pic.twitter.com/9PIgngr7UR</a>
      </p>
      &mdash; Ken Theroux (@KenTheroux)
      <a href="https://twitter.com/KenTheroux/status/1947154448637419826?ref_src=twsrc%5Etfw">
        July 21, 2025
      </a>
    </blockquote>
    <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
    """
    html(tweet_embed01, height=700, scrolling=False)



    html(tweet_embed, height=600, scrolling=False)

    # rss_feeds = {
    # "Select" : "",
    # "Times of India Tech News" : "http://timesofindia.indiatimes.com/rssfeeds/66949542.cms",
    # "Times of India Top Stories" : "http://timesofindia.indiatimes.com/rssfeedstopstories.cms",
    # "BBC" : "https://www.bbc.com/news/rss.xml",
    # "The Guardian" : "https://www.theguardian.com/international/rss"
    # }

    # #Parses an RSS feed and returns a list of articles.
    # def parse_rss_feed(url):
    #     feed = feedparser.parse(url)
    #     articles = []
    #     for entry in feed.entries:
    #         article = {
    #         "title": entry.title,
    #         "link": entry.link,
    #         "description": entry.summary,
    #         "published_at": entry.published
    #         }
    #         articles.append(article)
    #     return articles

    # # Title
    # st.title("RSS Feed Reader")

    # # Choose a Feed
    # choose_news_feed = "**Select a News Feed:**"
    # rss_feed_selected = st.selectbox(choose_news_feed, rss_feeds.keys())
    # st.write(rss_feed_selected)
    # selected_rss_feed_url = rss_feeds[rss_feed_selected]

    # # Collect all Feeds
    # all_articles = []
    # articles = parse_rss_feed(selected_rss_feed_url)
    # all_articles += articles

    # # Sort articles by datetime
    # all_articles.sort(key=lambda article: article["published_at"], reverse=True)

    # #Display Articles
    # for article in all_articles:
    #     st.markdown(f"**{article['title']}**")
    #     st.markdown(f"{article['description']}", unsafe_allow_html=True)
    #     st.markdown(f"Published on: {article['published_at']}")
    #     st.markdown(f"Link: [More Info]({article['link']})")


    # if "w" not in state:
    #     board = Dashboard()
    #     w = SimpleNamespace(
    #         dashboard=board,
    #         radar=Radar(board, 6, 0, 6, 6, minW=2, minH=4),
    #         card=Card(board, 0, 10, 3, 4, minW=2, minH=3),
    #         data_grid=DataGrid(board, 6, 10, 6, 6, minH=4),
    #         pie=Pie(board, 0, 14, 6, 6, minW=3, minH=4),
    #         player=Player(board, 6, 16, 6, 6, minH=5),
    #     )
    #     state.w = w
    # else:
    #     w = state.w

    # from streamlit_elements import elements, event

    # with elements("demo"):
    #     event.Hotkey("ctrl+s", lambda: None, bindInputs=True, overrideDefault=True)
    #     with w.dashboard(rowHeight=80):
    #         w.radar(json.dumps(Radar.DEFAULT_DATA))
    #         w.card(Card.DEFAULT_CONTENT)
    #         w.data_grid(json.dumps(DataGrid.DEFAULT_ROWS, indent=2))


if __name__ == "__main__":
    main()

