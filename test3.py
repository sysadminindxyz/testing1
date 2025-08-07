import streamlit as st
from streamlit_option_menu import option_menu
#import PsychologyTwoToneIcon from '@mui/icons-material/PsychologyTwoTone';

#import  components
#import twitter 
import page1 
import page2_twitter
import page3_news
import page4_blogs
import page5_surveys

from utils.page import page_group
# import nooz 
# import blogs
# import opinion




def main():
    page = page_group("p")

    # Define page names and their associated callbacks
    pages = {
        "Topline": page1.page1,
        "Twitter/X": page2_twitter.page2,
        "News": page3_news.page3,
        "Blogs": page4_blogs.page4,
        "Opinion": page5_surveys.page5,
        # "Executive Summary": components.exec_summary,
    }

    # Register them with page_group
    for name, callback in pages.items():
        page.item(name, callback)

    # Sidebar navigation using option_menu
    # with st.tabs:
    #     # st.title("The Great Crunch: Snacklash Live")

    selected = option_menu(
        menu_title="",
        options=list(pages.keys()),
        icons=["graph-up", "twitter-x", "newspaper", "keyboard-fill", "people-fill"],  # Add icons as needed
        menu_icon="cast",
        default_index=0,
        orientation="horizontal",
        styles={
        #"container": {"padding": "0!important", "background-color": "#fafafa"},
        "icon": {"color": "#84C36B", "font-size": "25px"}, 
        "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#433DD7"},
        }
    )

    # Show the selected page
    pages[selected]()  # ✅ call the function directly

if __name__ == "__main__":
    st.set_page_config(page_title="Snacklash", page_icon="🥨", layout="wide")
    main()
