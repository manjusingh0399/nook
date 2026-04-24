# nook control room — advanced version

import streamlit as st
from datetime import datetime
import random

st.set_page_config(page_title="nook control", layout="wide")

# -------------------- STYLE --------------------

st.markdown("""
<style>

/* ---------- BASE ---------- */
html, body, [data-testid="stApp"] {
    background: #0B0B0B;
    color: #EDEDED;
    font-family: -apple-system, BlinkMacSystemFont, sans-serif;
}

/* REMOVE DEFAULT */
#MainMenu, header, footer {visibility: hidden;}
.block-container {
    max-width: 1100px;
    margin: auto;
    padding-top: 2rem;
}

/* ---------- SIDEBAR ---------- */
[data-testid="stSidebar"] {
    background: #0A0A0A;
    border-right: 1px solid rgba(255,255,255,0.05);
}

/* ---------- CARD ---------- */
.card {
    background: #121212;
    border: 1px solid rgba(255,255,255,0.06);
    border-radius: 14px;
    padding: 1.5rem;
    margin-bottom: 12px;
    transition: all 0.2s ease;
}

.card:hover {
    border-color: rgba(255,255,255,0.12);
}

/* ---------- HERO ---------- */
.hero {
    background: linear-gradient(135deg, rgba(255,80,0,0.12), #121212);
    border-radius: 14px;
    padding: 1.8rem;
    margin-bottom: 20px;
}

/* ---------- METRIC ---------- */
.metric {
    font-size: 32px;
    font-weight: 700;
}
.metric-label {
    font-size: 11px;
    color: #777;
}

/* ---------- LIVE DOT ---------- */
.pulse {
    width: 8px;
    height: 8px;
    background: #ff3b30;
    border-radius: 50%;
    display: inline-block;
    margin-right: 6px;
    animation: pulse 1.5s infinite;
}

@keyframes pulse {
    0% { box-shadow: 0 0 0 0 rgba(255,59,48,0.6); }
    70% { box-shadow: 0 0 0 10px rgba(255,59,48,0); }
    100% { box-shadow: 0 0 0 0 rgba(255,59,48,0); }
}

/* ---------- TEXT ---------- */
.title {
    font-size: 26px;
    font-weight: 600;
}
.sub {
    font-size: 12px;
    color: #777;
}

/* ---------- BUTTON ---------- */
.stButton button {
    background: #1F1F1F;
    border-radius: 10px;
    border: 1px solid rgba(255,255,255,0.1);
}
.stButton button:hover {
    border-color: #FF5A00;
}

</style>
""", unsafe_allow_html=True)

# -------------------- DATA --------------------

if "members" not in st.session_state:
    st.session_state.members = [
        {"name": "Ishita", "tag": "quiet"},
        {"name": "Kabir", "tag": "expressive"},
        {"name": "Dev", "tag": "open"},
    ]

if "evenings" not in st.session_state:
    st.session_state.evenings = [
        {"name": "canvas night", "vibe": "mixed"},
        {"name": "lake walk", "vibe": "quiet"}
    ]

# -------------------- SIGNAL ENGINE --------------------

def get_signal():
    signals = [
        "quiet energy dominant",
        "social energy rising",
        "mixed balance stable",
        "low activity detected"
    ]
    return random.choice(signals)

# -------------------- SIDEBAR --------------------

with st.sidebar:
    st.markdown("### nook")
    st.markdown("<div class='sub'>control system</div>", unsafe_allow_html=True)

    page = st.radio("", [
        "control",
        "people",
        "evenings",
        "insights"
    ], label_visibility="collapsed")

# -------------------- CONTROL ROOM --------------------

def control():
    st.markdown("<div class='title'>control room</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub'>live system state</div><br>", unsafe_allow_html=True)

    # HERO SIGNAL
    st.markdown(f"""
    <div class='hero'>
        <span class="pulse"></span>
        <span style="font-size:18px;font-weight:600;">
            {get_signal()}
        </span>
        <div style="font-size:13px;color:#aaa;margin-top:6px;">
            system adapting in real time
        </div>
    </div>
    """, unsafe_allow_html=True)

    # METRICS
    cols = st.columns(3)

    metrics = [
        ("people", len(st.session_state.members)),
        ("evenings", len(st.session_state.evenings)),
        ("status", "active")
    ]

    for i, (label, val) in enumerate(metrics):
        with cols[i]:
            st.markdown(f"""
            <div class='card'>
                <div class='metric'>{val}</div>
                <div class='metric-label'>{label}</div>
            </div>
            """, unsafe_allow_html=True)

# -------------------- PEOPLE --------------------

def people():
    st.markdown("<div class='title'>people</div><br>", unsafe_allow_html=True)

    for m in st.session_state.members:
        st.markdown(f"""
        <div class='card'>
            <b>{m['name']}</b><br>
            <span style='color:#777'>{m['tag']}</span>
        </div>
        """, unsafe_allow_html=True)

# -------------------- EVENINGS --------------------

def evenings():
    st.markdown("<div class='title'>evenings</div><br>", unsafe_allow_html=True)

    for e in st.session_state.evenings:
        st.markdown(f"""
        <div class='card'>
            <b>{e['name']}</b><br>
            <span style='color:#777'>{e['vibe']}</span>
        </div>
        """, unsafe_allow_html=True)

# -------------------- INSIGHTS --------------------

def insights():
    st.markdown("<div class='title'>insights</div><br>", unsafe_allow_html=True)

    st.markdown("""
    <div class='card'>
        system trend: quieter groups show higher retention<br>
        recommendation: reduce group size
    </div>
    """, unsafe_allow_html=True)

# -------------------- ROUTING --------------------

if page == "control":
    control()
elif page == "people":
    people()
elif page == "evenings":
    evenings()
elif page == "insights":
    insights()
