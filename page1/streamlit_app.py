import streamlit as st
import streamlit.components.v1 as components
import csv
import base64
import os
import re
import sys
import json
from .widget1 import main as widget1

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
    pew6_base64= get_base64_image("images/pew6.png")
    pew7_base64= get_base64_image("images/pew7.png")

    #tweet images in base64
    tweet_list = []
    with open('data/toptweets.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            if len(row) == 3:
                tweet_list.append(row)
            else:
                raise ValueError(f"Unexpected row length: {row}")
    def extract_tweet_id(url: str) -> str:
        match = re.search(r"status/(\d+)", url)
        if match:
            return match.group(1)
        raise ValueError(f"Invalid tweet URL: {url}")            

    tweet_img64=[]
    for title, desc, link in tweet_list[0:10]:
        tweet_id=extract_tweet_id(link)
        tweet_img64.append(get_base64_image(f"images/tweet_{tweet_id}.png"))


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
    # === Dummy Data Refresh (on every interaction) ===
    news = get_news(source_type, st.session_state["time_selection"])

    # === News Widget HTML ===
    html_parts_news = [wb(" News Coverage", "newspaper")]
    html_parts_news.append("""
            <ul style="padding-left: 18px; margin: 0;">
    """)

    for title, desc, sources in news:
        html_parts_news.append(f"""
            <li style="margin-bottom: 10px;">
                {title}
                <ul style="padding-left: 16px; margin-top: 5px;">
                    <li>
                        <span class="desc">{desc}</span><br>
        """)
        for source_text, url, impact in sources:
            html_parts_news.append(f'<a class="source-link" href="{url}" target="_blank">{source_text}</a>')
            html_parts_news.append(f'{impact}')
        html_parts_news.append("""</li></ul></li>""")
    
    news_widget_html = "".join(html_parts_news)



    #TWEETS
    #GET TWEET DATA
    html_parts_social  = [wb(" Social Conversation", "twitter")]
   
    # Append content inside the scrollable area
    for cnt, (title, desc, link) in enumerate(tweet_list[:10]):
        base64_img = tweet_img64[cnt]
        html_parts_social.append(f"""
            <div style='margin-bottom: 20px;'>
                <img src="data:image/png;base64,{base64_img}" width="300">
                <br>
                <a class="source-link" href="https://www.{link}" target="_blank">link</a>
            </div>
        """)

    # Close the inner scrollable container and outer box
    html_parts_social.append("</div></div>")

    # Join HTML together
    social_widget_html = "".join(html_parts_social)


            
    #VULNERABILITIES
    # === Dummy Data Refresh (on every interaction) ===
    vulnerabilities = get_vulnerabilities(source_type, st.session_state["time_selection"])

    # === News Widget HTML ===
    html_parts_vulnerabilities =  [wb(" Key Vulnerabilities", "exclamation-triangle")]
    
    for title, desc, implication in vulnerabilities:
        html_parts_vulnerabilities.append(f"""
            <li style="margin-left: -30px; margin-bottom: 10px; list-style-type:none;">
                {title}
                <ul style="padding-left: 46px; margin-top: 5px;">
                    <li>
                        <span class="desc">{desc}</span><br>
        """)
        #for source_text, url, impact in sources:
        #html_parts_vulnerabilities.append(f'{desc}')
        html_parts_vulnerabilities.append(f'{implication}')
        html_parts_vulnerabilities.append("""</li></ul></li>""")
    
    vulnerabilities_widget_html = "".join(html_parts_vulnerabilities)


    # # EXECUTIVE SUMMARY WIDGET
    #with open("static/exec_sum.pdf", "rb") as f:
    #    b64_pdf = base64.b64encode(f.read()).decode()

    #href = f'<a href="data:application/pdf;base64,{b64_pdf}" download="Executive_Summary.pdf" class="summary-link">Full Report</a>'
    pdf_url="http://3.85.37.226:9000/exec_sum.pdf"
    href = f'<a href="{pdf_url}" target="_blank" class="summary-link">Full Report</a>'

    html_executive_summary = [wb(" Real-Time AI Reporting", "robot")]
    html_executive_summary.append(f"""
        <ul style="padding-left: 18px; margin: 0;">
                Recent shifts in public behavior related to GLP-1 drugs (e.g., Ozempic, Wegovy, Mounjaro) are
                signaling a notable decline in snack food consumption across key demographics. Analysis of
                social media conversations, influencer commentary, and digital news articles from
                January–June 2025 suggests an accelerating cultural association between GLP-1 usage and
                "mindful eating" or reduced snacking behavior...  
                {href}
        </ul>
    </div>
    </div>
    """)
    summary_html="".join(html_executive_summary)





    html_public_opinion = [wb(" Public Opinion", "chat-text")]

    
    html_public_opinion.append(f"""
        <div style='text-align: left;'>
            <img src="data:image/png;base64,{pew6_base64}" width='300'>
        </div>
        <a class="source-link" href="https://www.pewresearch.org/science/2024/02/26/how-americans-view-weight-loss-drugs-and-their-potential-impact-on-obesity-in-the-u-s/" target="_blank">Full Report</a>
        </div>
        </div>
        """
    )

    opinion_html="".join(html_public_opinion)

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
            components.html(opinion_html, height=370, scrolling=False)
            # st.markdown(
            #     f"""
            #     <div style='text-align: right;'>
            #         <img src="data:image/png;base64,{pew6_base64}" width='400'>
            #     </div>
            #     """,
            #     unsafe_allow_html=True
            # )
        with row2[1]:
            components.html(vulnerabilities_widget_html, height=370, scrolling=False)
        with row2[2]:
            components.html(summary_html, height=370, scrolling=False)



# === Mock Function to Return News (no filtering yet) ===
def get_news(source_type, time_selection):
    return [   
        (
            "The snacking recession: Why Americans are buying fewer treats",
            "Americans are snacking less — and that's a problem for the packaged food industry. Why it matters: After years of inflation, consumers are recoiling, fed up with food price increases and suddenly immersed in economic uncertainty...",
            [
                ("Axios", "https://www.axios.com/2025/03/19/general-mills-snacks-sales", "Impact factor = 27, Engagement=18"),
            ]
        ),
        (
            "Why GLP-1s could become the 'everything drug'",
            "The biggest buzz around GLP-1 drugs these days has nothing to do with weight loss. And that might lead to some problems for patients and insurers...",
            [
                ("Axios", "https://www.businessoffashion.com/articles/workplace-talent/plus-size-models-fashion-industry-slowdown-90s-thinness-ozempic",
                 "Impact factor=27, Engagement=11"),
            ]
        ),
    ]



def get_vulnerabilities(source_type, time_selection):
    return [  
        (
            "⚠️ 1. Cost and Accessibility",
            "GLP-1 medications remain prohibitively expensive for many, especially without insurance coverage — costing upwards of $1,000/month in the U.S.",
            "Limits adoption to higher-income or well-insured populations, undermining equity and mass market penetration."
        ),
        (
            "⚠️ 2. Supply Constraints and Manufacturing Bottlenecks",
            "Demand has outpaced supply globally, leading to shortages, prescription delays, and rationing of doses.",
            "Unreliable availability creates frustration, erodes trust, and slows adoption — especially for new users or non-prioritized patients."
        ),
        (
            "⚠️ 3. Long-Term Safety Unknowns",
            "Many patients are now taking GLP-1s for years, but long-term health consequences (on organs, nutrient absorption, fertility, etc.) remain under-researched.",
            "Hesitation among doctors, regulators, and consumers may intensify as real-world longitudinal data comes in."
        ),
        (
            "⚠️ 4. Side Effects and Dropout Rates",
            "Nausea, vomiting, gallbladder issues, muscle loss, and even psychological side effects (e.g., depression or ED relapse) are increasingly reported.",
            "High dropout rates (up to 50% in some studies) could limit sustained benefit and raise concerns about over-reliance."
        ),
        (
            "⚠️ 5. Medicalization of Weight Loss & Ethical Backlash",
            "Critics argue GLP-1s promote a pharmacological solution to a social and systemic issue (obesity), while marginalizing those with eating disorders or body diversity.",
            "Cultural and ethical pushback (especially from younger or body-positive communities) could constrain reputational support and policy expansion."
        ),
        (
            "⚠️ 6. Rebound Weight Gain After Discontinuation",
            "Studies show most patients regain a significant portion of lost weight when they stop taking GLP-1s.",
            "Undermines perception of long-term efficacy and raises questions about creating drug dependency for metabolic control."
        ),
        (
            "⚠️ 7. Off-Label Use and Legal Risk",
            "Widespread use by people without diabetes or clinical obesity — especially via telehealth and influencer endorsements — raises liability concerns.",
            "Regulatory scrutiny, litigation, and insurer backlash may emerge as unintended consequences of overly aggressive adoption."
        ),
        (
            "⚠️ 8. Food & Beverage Industry Disruption",
            "Reduced appetite and food consumption among users is already impacting packaged food, beverage, and restaurant sectors.",
            "Broader economic ripple effects could provoke industry lobbying against coverage or promotion of GLP-1s at scale."
        ),
        (
            "⚠️ 9. Insurance Resistance and Coverage Gaps",
            "Payers are pushing back on non-diabetic prescriptions and weight-loss-only use; some states and plans have banned coverage altogether.",
            "Without systemic coverage, adoption remains slow or inequitable — especially in public or employer health plans."
        ),
        (
            "⚠️ 10. Social Inequality and Public Perception",
            "The drugs are increasingly seen as tools of affluent vanity rather than public health — especially in communities with limited access.",
            "Can drive stigma, resentment, and political backlash if adoption is seen as elitist or skewed."
        )
    ]



if __name__ == "__main__":
    main()