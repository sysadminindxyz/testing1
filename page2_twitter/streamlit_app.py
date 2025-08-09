

import json
import streamlit as st
from pathlib import Path
from streamlit.components.v1 import html as html

#st.set_page_config(page_title="Tweet Embeds")


def main():
  
  st.write(
      """
      Trending Social Posts &nbsp;
      =====================

      """
  )

  # Load once
  DB = json.loads(Path("data/tweets.json").read_text())
  print(DB)
  # Include widgets.js once at the end (omit_script=True in oEmbed above)
  WIDGETS_JS = '<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>'

  for item in DB:
      html(item, height=700, scrolling=False)
      #st_html(item, max_width=700, scrolling=False, margin="auto")

  # Add the script once so embeds hydrate
  #st.markdown(WIDGETS_JS, unsafe_allow_html=True)



if __name__ == "__main__":
    main()

