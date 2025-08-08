import os, sys, pandas as pd
import streamlit as st
import csv
import json

# paths
central_pipeline_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'central-pipeline'))
sys.path.append(central_pipeline_path)

from indxyz_utils.widgetbox import main as wb



def build_html(items):
    return "<ul>" + "\n".join(items) + "</ul>"

def main():

    with open('data/news.csv', newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        # Optional: normalize headers and strip whitespace
        reader.fieldnames = [h.strip() for h in reader.fieldnames]
        data = [{k.strip(): (v.strip() if isinstance(v, str) else v) for k, v in row.items()}
                for row in reader]

    with open('data.json', 'w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, ensure_ascii=False, indent=4)

    expected = {'title', 'summary', 'source', 'Link'}
    assert set(reader.fieldnames) == expected, reader.fieldnames


    #print(data)
    # === Render Top Issues Widget HTML ===
    html_parts = [wb(" News Coverage", "megaphone")]

    html_parts.append("""
    <ul style="padding-left: 18px; margin: 0;">
    <ol style="margin-left: -30px; margin-bottom: 10px;" type="1">
    """)

    for title, desc, sources, url in (
        (row["title"], row["summary"], row["source"], row["Link"]) 
        for row in data
    ):
        html_parts.append(f"""
            <li>
                <strong>{title}</strong>
                <div style="padding-left: 16px; margin-top: 5px;">
                    <div class="desc">{desc}</div>
                    <div>
        """)
        html_parts.append(f'<a class="source-link" href="{url}" target="_blank">{sources}</a>')
        html_parts.append("</div></div></li>")
    
    html_parts.append("</ol>")

    return("".join(html_parts))

if __name__ == "__main__":
    main()
