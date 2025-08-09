import streamlit as st
from streamlit.components.v1 import html as html
import base64
import os
import sys
central_pipeline_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..', 'central-pipeline'))
sys.path.append(central_pipeline_path)
from indxyz_utils.widgetbox import main as wb
from indxyz_utils.tweet_to_image_tools import get_base64_image

def main():
    # pages/External_Tool.py

    st.set_page_config(layout="wide")
    st.title("Public Opinion")
    #PUBLIC OPINION
    #html_public_opinion = [wb(" Public Opinion", "chat-text")]
    yougov_img=get_base64_image(f"images/yougov.png")
    # st.image(
    #     f"data:image/png;base64,{yougov_img}",
    #     use_container_width=True
    # )

    url = "https://today.yougov.com/topics/economy/explore/public_figure/Bill_Gates"

    st.markdown(
        f"""
        <center>
        <a href="{url}" target="_blank" rel="noopener noreferrer">
        <img src="data:image/png;base64,{yougov_img}"
            style="max-width:100%; height:auto; display:block; cursor:pointer;">
        </a>
        </center>
        """,
        unsafe_allow_html=True,
    )

    # html_public_opinion=[]
    # html_public_opinion.append(f"""
    #     <div style='margin-bottom: 20px;'>
    #         <img src="data:image/png;base64,{yougov_img}" 
    #             style="max-width: 100%; height: auto; display: block;">
    #         <br>
    #         <a class="source-link" href="https://today.yougov.com/topics/economy/explore/public_figure/Bill_Gates" target="_blank">link</a>
    #     </div>
    #     <script>
    #         function resize() {{
    #         const img = document.getElementById('yg');
    #         if (!img) return;
    #         const h = Math.ceil(img.getBoundingClientRect().height) + 16;
    #         window.parent.postMessage({{
    #             isStreamlitMessage: true,
    #             type: "streamlit:setFrameHeight",
    #             height: h
    #         }}, "*");
    #         }}
    #         const img = document.getElementById('yg');
    #         img.addEventListener('load', resize);
    #         new ResizeObserver(resize).observe(img);
    #         window.addEventListener('resize', resize);
    #         resize();
    #     </script>
    #     """)
    
    # # Close the inner scrollable container and outer box
    # #html_public_opinion.append("</div></div>")
    # opinion_widget_html="".join(html_public_opinion)
    # html(opinion_widget_html, scrolling=False)

    # url = "https://today.yougov.com/topics/economy/explore/public_figure/Bill_Gates"

    # html(
    #     f"""
    #     <style>
    #     html, body {{ margin:0; padding:0; }}
    #     .wrap {{ width:100%; height:100vh; }}
    #     .wrap > iframe {{ width:100%; height:100%; border:0; }}
    #     </style>
    #     <div class="wrap">
    #     <iframe
    #         src="{url}"
    #         allow="clipboard-write; fullscreen; geolocation *; microphone *; camera *"
    #         referrerpolicy="no-referrer-when-downgrade">
    #     </iframe>
    #     </div>
    #     <script>
    #     function setHeight() {{
    #         const h = Math.max(window.innerHeight - 16, 600);
    #         window.parent.postMessage({{ isStreamlitMessage: true, type: "streamlit:setFrameHeight", height: h }}, "*");
    #     }}
    #     window.addEventListener("load", setHeight);
    #     window.addEventListener("resize", setHeight);
    #     </script>
    #     """,
    #     height=600,  # initial; JS bumps it to fill the viewport
    # )


if __name__ == "__main__":
    st.set_page_config(page_title="Gateway", page_icon="robot", layout="wide")
    main()
