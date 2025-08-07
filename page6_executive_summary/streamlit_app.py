import base64
import streamlit as st
def main():

    with open("static/exec_sum.pdf", "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'<center><iframe src="data:application/pdf;base64,{base64_pdf}" width="1200" height="850" type="application/pdf"></iframe>'


    st.markdown(pdf_display, unsafe_allow_html=True)


if __name__ == "__main__":
    st.set_page_config(page_title="Snacklash", page_icon="🥨", layout="wide")
    main()
