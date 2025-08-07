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

    #########ISSUES
    # === Dummy Data Refresh (on every interaction) ===
    with open('data/issues.json', 'r') as file:
        data = json.load(file)

    print(data)
    # === Render Top Issues Widget HTML ===
    html_parts = [wb(" Top Issues", "megaphone")]

    html_parts.append("""
    <ul style="padding-left: 18px; margin: 0;">
    <ol style="margin-left: -30px; margin-bottom: 10px;" type="1">
    """)

    for title, desc, sources in data:
        html_parts.append(f"""
                <li>
                        <strong>{title}</strong>
                <div style="padding-left: 16px; margin-top: 5px;">
                        <div class="desc">{desc}</div>
                        <div>
        """)
        for source_text, url in sources:
            html_parts.append(f'<a class="source-link" href="{url}" target="_blank">{source_text}</a>')
        html_parts.append("</div></div></li>")
    
    html_parts.append("</ol>")

    return("".join(html_parts))


if __name__ == "__main__":
    main()