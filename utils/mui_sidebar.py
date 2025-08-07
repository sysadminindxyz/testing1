from streamlit_elements import elements, mui
import streamlit as st
from utils.page import page_group

def sidebar_mui():
    pg = page_group("p")
    current = pg.selected or pg._default or "topline"

    clicked = st.session_state.get("nav_clicked", None)

    with st.sidebar:
        with elements("mui-sidebar"):
            def make_btn(page_id, label):
                return mui.ListItemButton(
                    mui.ListItemText(label),
                    selected=(current == page_id),
                    onClick=lambda *args: st.session_state.update({"nav_clicked": page_id}),
                )

            mui.Paper(
                mui.List(
                    make_btn("topline", "Topline"),
                    make_btn("old", "Old"),
                    sx={"width": "100%"},
                ),
                elevation=3,
                sx={"padding": 2},
            )

    # Perform navigation if clicked
    if clicked and clicked != current:
        st.session_state["nav_clicked"] = None  # Reset
        st.experimental_set_query_params(p=clicked)
        st.experimental_rerun()

    return pg
