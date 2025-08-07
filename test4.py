import streamlit as st
from streamlit_option_menu import option_menu
#import PsychologyTwoToneIcon from '@mui/icons-material/PsychologyTwoTone';
import base64
#import  components
#import twitter 
import page1 
import page2_twitter
import page3_news
#import page4_blogs
import page5_surveys
#import page6_executive_summary
import page6_ai_summary
import os
import sys

#import csv

from utils.page import page_group
# import nooz 
# import blogs
# import opinion

central_pipeline_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..', 'central-pipeline'))
sys.path.append(central_pipeline_path)
from indxyz_utils.render_title import render_title


def main():
    st.set_page_config( layout="wide")

    render_title("Gates Monitor")

    st.markdown("---")

    page = page_group("p")

    # Define page names and their associated callbacks
    pages = {
        "Overview": page1.page1,
        "News Coverage": page3_news.page3,
        "Social Conversation": page2_twitter.page2,
        "Public Opinion": page5_surveys.page5,
        "AI Reporting": page6_ai_summary.page6b,
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
        icons=["graph-up", "newspaper", "twitter", "people-fill", "robot"],  # Add icons as needed
        menu_icon="cast",
        default_index=0,
        orientation="horizontal",
        styles={
        #"container": {"padding": "0!important", "background-color": "#fafafa"},
        "icon": {"color": "#84C36B", "font-size": "15px"}, 
        "nav-link": {"font-size": "15px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#433DD7"},
        }
    )

    # Show the selected page
    pages[selected]()  # ✅ call the function directly

    
    st.markdown("""
    <hr style="margin-top: 40px; margin-bottom: 10px;">
    <div style="text-align: center; color: #666;">
        Questions? More Information? \n\n Contact: <a href="mailto:info@indxyz.com" style="color: #007acc; text-decoration: none;">info@indxyz.com</a>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    st.set_page_config(page_title="Snacklash"
                       , page_icon="🥨"
                       , layout="wide"
                       )
    main()
