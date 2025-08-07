import streamlit as st
from .page import page_group

def Sidebar_nav():
    pg = page_group("p")
    current = pg.selected or pg._default or "topline"

    with st.sidebar:
        st.title("The Great Crunch: Snacklash Live")
        st.markdown("### ✨ SECTIONS")

        for page_id, label in [("topline", "Topline"), ("old", "Old")]:
            if current == page_id:
                st.markdown(f"**{label}**")
            else:
                if st.button(label, key=page_id):
                    st.experimental_set_query_params(p=page_id)
                    st.experimental_rerun()

    return pg
