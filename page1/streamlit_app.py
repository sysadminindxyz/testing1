import streamlit as st
import streamlit.components.v1 as components
import csv
import base64
import os
import re
import sys
import json
from .widget1 import main as widget1
from .widget2 import main as widget2
from .widget3 import main as widget3


# Add the absolute path to central-pipeline to sys.path
central_pipeline_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..', 'central-pipeline'))
sys.path.append(central_pipeline_path)
from indxyz_utils.widgetbox import main as wb


def main(): 

    #GET IMAGES IN BASE64
    def get_base64_image(image_path):
        with open(image_path, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
 

    # === State Initialization ===
    if "time_selection" not in st.session_state:
        st.session_state["time_selection"] = "Past Week"

    # === Sidebar Layout ===
    with st.sidebar:
        st.title("Dashboard Filters")
        # === Toggle for Source Type ===
        source_type = st.radio("Media Types:", ["News+Social Media", "News Media", "Social Media"], horizontal=False)
        time_options = st.radio("Timeframe:", ["Past 24 hr", "Past Week", "Past Month"], horizontal=False)
    # === JS Listener for Updating Time Filter ===
    components.html("""
        <script>
        window.addEventListener("message", (event) => {
            if (event.data.time) {
                const streamlitEvent = new CustomEvent("streamlit:setComponentValue", {
                    detail: {key: "time_selection", value: event.data.time}
                });
                window.dispatchEvent(streamlitEvent);
            }
        });
        </script>
    """, height=0)


    #ISSUES
    issue_widget_html = widget1()

    #NEWS
    news_widget_html = widget2()

    #SOCIAL
    social_widget_html=widget3()

    #PUBLIC OPINION
    html_public_opinion = [wb(" Public Opinion", "chat-text")]
    yougov_img=get_base64_image(f"images/yougov.png")
    html_public_opinion.append(f"""
        <div style='margin-bottom: 20px;'>
            <img src="data:image/png;base64,{yougov_img}" width="300">
            <br>
            <a class="source-link" href="https://today.yougov.com/topics/economy/explore/public_figure/Bill_Gates" target="_blank">link</a>
        </div>
    """)
    # Close the inner scrollable container and outer box
    html_public_opinion.append("</div></div>")
    opinion_widget_html="".join(html_public_opinion)


    #CALENDAR WIDGET
    html_calendar = [wb(" Calendar", "calendar")]
    calendar_img=get_base64_image(f"images/calendar.png")
    html_calendar.append(f"""
        <div style='margin-bottom: 20px;'>
            <img src="data:image/png;base64,{calendar_img}" width="300">
            <br>
            <a class="source-link" href="https://www.gatesfoundation.org/ideas/speeches" target="_blank">link</a>
        </div>
    """)
    # Close the inner scrollable container and outer box
    html_calendar.append("</div></div>")
    calendar_widget_html="".join(html_calendar)



    # # EXECUTIVE SUMMARY WIDGET
    #with open("static/exec_sum.pdf", "rb") as f:
    #    b64_pdf = base64.b64encode(f.read()).decode()

    #href = f'<a href="data:application/pdf;base64,{b64_pdf}" download="Executive_Summary.pdf" class="summary-link">Full Report</a>'
    pdf_url="http://3.85.37.226:9000/gates_executive_summary.pdf"
    href = f'<a href="{pdf_url}" target="_blank" class="summary-link">Full Report</a>'

    html_executive_summary = [wb(" Real-Time AI Reporting", "robot")]
    html_executive_summary.append(f"""
        <ul style="padding-left: 18px; margin: 0;">
        popAI analyzed 237 News Articles and 872 Social Media Posts over the Past 14 Days as well as Public Opinion Survey Data to identify key themes, news coverage, and social conversations relating to Bill Gates...  
        {href}
        </ul>
    </div>
    </div>
    """)
    summary_widget_html="".join(html_executive_summary)






    # === Layout ROW 1===
    with st.container():
        #st.markdown("<div style='margin-top: -25px; margin-bottom: -25px;'>", unsafe_allow_html=True)
        row1 = st.columns(3)
        with row1[0]:
            components.html(issue_widget_html, height=370, scrolling=False)
        with row1[1]:
            components.html(news_widget_html, height=370, scrolling=False)

        with row1[2]:
            components.html(social_widget_html, height=370, scrolling=False)



    # Construct a download/open link (assumes you're running Streamlit locally)
    # === Layout ROW 2===
    with st.container():
        #st.markdown("<div style='margin-top: -100px; margin-bottom: -100px;'>", unsafe_allow_html=True)

        row2 = st.columns(3)
        with row2[0]:
            components.html(opinion_widget_html, height=370, scrolling=False)
            # st.markdown(
            #     f"""
            #     <div style='text-align: right;'>
            #         <img src="data:image/png;base64,{pew6_base64}" width='400'>
            #     </div>
            #     """,
            #     unsafe_allow_html=True
            # )
        with row2[1]:
            components.html(calendar_widget_html, height=370, scrolling=False)
        with row2[2]:
            components.html(summary_widget_html, height=370, scrolling=False)


if __name__ == "__main__":
    main()