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

    with open('data/issues.csv', newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        # Optional: normalize headers and strip whitespace
        reader.fieldnames = [h.strip() for h in reader.fieldnames]
        data = [{k.strip(): (v.strip() if isinstance(v, str) else v) for k, v in row.items()}
                for row in reader]

    with open('data.json', 'w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, ensure_ascii=False, indent=4)

    expected = {'issue', 'description', 'source', 'link'}
    assert set(reader.fieldnames) == expected, reader.fieldnames


    #print(data)
    # === Render Top Issues Widget HTML ===
    html_parts = [wb(" Top Issues", "megaphone")]

    html_parts.append("""
    <ul style="padding-left: 18px; margin: 0;">
    <ol style="margin-left: -30px; margin-bottom: 10px;" type="1">
    """)

    for title, desc, sources, url in (
        (row["issue"], row["description"], row["source"], row["link"]) 
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