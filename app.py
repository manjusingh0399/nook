from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components


APP_DIR = Path(__file__).parent
HTML_PATH = APP_DIR / "index.html"


st.set_page_config(
    page_title="Nook Control Room",
    page_icon="*",
    layout="wide",
    initial_sidebar_state="collapsed",
)


def check_password() -> bool:
    configured_password = st.secrets.get("APP_PASSWORD", "")
    if not configured_password:
        st.warning("Set APP_PASSWORD in Streamlit secrets before sharing this app.")
        return True

    with st.form("password_form", border=False):
        st.markdown("### Nook Control Room")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Enter")

    if submitted and password == configured_password:
        st.session_state["authenticated"] = True
        st.rerun()

    if submitted:
        st.error("Incorrect password.")

    return st.session_state.get("authenticated", False)


if check_password():
    html = HTML_PATH.read_text(encoding="utf-8")
    components.html(html, height=920, scrolling=True)
