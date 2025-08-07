import streamlit as st
import streamlit.components.v1 as components
import csv
import base64
import sys
import os
import re

def main(): 


    # Add the absolute path to central-pipeline to sys.path
    central_pipeline_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'central-pipeline'))
    sys.path.append(central_pipeline_path)

    from indxyz_utils.widgetbox import main as wb
    print(wb("TITLE HERE", "newspaper"))

if __name__ == "__main__":
    main()