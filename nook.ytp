"""
nook control room
─────────────────
streamlit app · run with: streamlit run nook_app.py
built quietly · bhopal
"""
 
import streamlit as st
import pandas as pd
import json
import random
from datetime import datetime, date
from pathlib import Path
 
# ─────────────────────────────────────────────────────────
# CONFIG
# ─────────────────────────────────────────────────────────
st.set_page_config(
    page_title="nook control room",
    page_icon="◎",
    layout="wide",
    initial_sidebar_state="expanded",
)
 
# ─────────────────────────────────────────────────────────
# STYLES
# ─────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;500;600;700;800&family=Syne+Mono&family=DM+Sans:wght@300;400;500&display=swap');
 
/* ── ROOT ── */
:root {
    --o: #FF5A00;
    --ob: rgba(255,90,0,0.08);
    --og: rgba(255,90,0,0.20);
    --bg: #0E0E0E;
    --s1: #141414;
    --s2: #1A1A1A;
    --s3: #202020;
    --b1: rgba(255,255,255,0.05);
    --b2: rgba(255,255,255,0.09);
    --t1: #F4F2ED;
    --t2: #888;
    --t3: #444;
    --g: #22c55e;
    --r: #ef4444;
    --p: #a78bfa;
    --y: #fbbf24;
    --b: #38bdf8;
}
 
/* ── BASE ── */
html, body, [data-testid="stApp"] {
    background-color: #0E0E0E !important;
    color: #F4F2ED !important;
    font-family: 'DM Sans', sans-serif !important;
}
 
/* ── HIDE STREAMLIT DEFAULT ── */
#MainMenu, footer, header { visibility: hidden !important; }
[data-testid="stDecoration"] { display: none !important; }
.block-container { padding: 2rem 2.5rem !important; max-width: 1400px !important; }
 
/* ── SIDEBAR ── */
[data-testid="stSidebar"] {
    background: #111111 !important;
    border-right: 1px solid rgba(255,255,255,0.05) !important;
}
[data-testid="stSidebar"] * { color: #888 !important; }
[data-testid="stSidebarNav"] { display: none !important; }
.sidebar-logo {
    font-family: 'Syne', sans-serif;
    font-weight: 800;
    font-size: 28px;
    color: #F4F2ED !important;
    letter-spacing: -0.5px;
    margin-bottom: 4px;
}
.sidebar-logo span { color: #FF5A00 !important; }
.sidebar-tag {
    font-family: 'Syne Mono', monospace;
    font-size: 9px;
    color: #444 !important;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    margin-bottom: 2rem;
}
.nav-item {
    font-family: 'DM Sans', sans-serif;
    font-size: 13px;
    color: #666 !important;
    padding: 0.5rem 0.75rem;
    border-radius: 8px;
    margin-bottom: 2px;
    cursor: pointer;
    transition: all 0.15s;
}
.nav-item.active {
    background: rgba(255,90,0,0.1) !important;
    color: #FF5A00 !important;
    border: 1px solid rgba(255,90,0,0.2) !important;
}
 
/* ── RADIO NAV ── */
[data-testid="stRadio"] > div { gap: 2px !important; }
[data-testid="stRadio"] label {
    background: transparent !important;
    border: none !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 13px !important;
    color: #666 !important;
    padding: 0.5rem 0.75rem !important;
    border-radius: 8px !important;
    transition: all 0.15s !important;
    width: 100% !important;
}
[data-testid="stRadio"] label:hover {
    background: rgba(255,255,255,0.04) !important;
    color: #F4F2ED !important;
}
[data-testid="stRadio"] label[data-baseweb="radio"]:has(input:checked) {
    background: rgba(255,90,0,0.10) !important;
    color: #FF5A00 !important;
    border: 1px solid rgba(255,90,0,0.20) !important;
}
 
/* ── TYPOGRAPHY ── */
h1, h2, h3 { font-family: 'Syne', sans-serif !important; color: #F4F2ED !important; }
p, span, li { font-family: 'DM Sans', sans-serif !important; }
 
/* ── CARDS ── */
.nk-card {
    background: linear-gradient(135deg, rgba(26,26,26,0.9), rgba(20,20,20,0.95));
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border: 1px solid rgba(255,255,255,0.06);
    border-radius: 16px;
    padding: 1.5rem;
    margin-bottom: 1rem;
    transition: all 0.2s ease;
    position: relative;
    overflow: hidden;
}
.nk-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(255,90,0,0.3), transparent);
}
.nk-card:hover {
    border-color: rgba(255,255,255,0.10);
    transform: translateY(-1px);
    box-shadow: 0 8px 32px rgba(0,0,0,0.4);
}
.nk-card-accent {
    border-left: 2px solid #FF5A00 !important;
}
.nk-card-green { border-left: 2px solid #22c55e !important; }
.nk-card-purple { border-left: 2px solid #a78bfa !important; }
.nk-card-blue { border-left: 2px solid #38bdf8 !important; }
 
/* ── STAT BOXES ── */
.stat-box {
    background: rgba(20,20,20,0.9);
    border: 1px solid rgba(255,255,255,0.05);
    border-radius: 14px;
    padding: 1.5rem;
    text-align: center;
    position: relative;
    overflow: hidden;
    transition: all 0.2s;
}
.stat-box::after {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
    background: var(--accent, #FF5A00);
}
.stat-box:hover { transform: translateY(-2px); box-shadow: 0 8px 24px rgba(0,0,0,0.5); }
.stat-n {
    font-family: 'Syne', sans-serif;
    font-size: 42px;
    font-weight: 800;
    line-height: 1;
    margin-bottom: 6px;
}
.stat-l {
    font-family: 'Syne Mono', monospace;
    font-size: 9px;
    color: #555;
    text-transform: uppercase;
    letter-spacing: 0.12em;
}
 
/* ── SECTION HEADER ── */
.section-head {
    margin-bottom: 2rem;
}
.section-title {
    font-family: 'Syne', sans-serif;
    font-weight: 800;
    font-size: 26px;
    color: #F4F2ED;
    letter-spacing: -0.3px;
    margin-bottom: 4px;
}
.section-sub {
    font-family: 'Syne Mono', monospace;
    font-size: 11px;
    color: #444;
    letter-spacing: 0.06em;
}
 
/* ── BADGES ── */
.badge {
    display: inline-block;
    padding: 2px 9px;
    border-radius: 20px;
    font-family: 'Syne Mono', monospace;
    font-size: 9px;
    font-weight: 700;
    letter-spacing: 0.06em;
    text-transform: uppercase;
}
.badge-o { background: rgba(255,90,0,0.12); color: #FF5A00; border: 1px solid rgba(255,90,0,0.25); }
.badge-g { background: rgba(34,197,94,0.10); color: #22c55e; border: 1px solid rgba(34,197,94,0.20); }
.badge-r { background: rgba(239,68,68,0.10); color: #ef4444; border: 1px solid rgba(239,68,68,0.20); }
.badge-p { background: rgba(167,139,250,0.10); color: #a78bfa; border: 1px solid rgba(167,139,250,0.20); }
.badge-y { background: rgba(251,191,36,0.10); color: #fbbf24; border: 1px solid rgba(251,191,36,0.20); }
.badge-b { background: rgba(56,189,248,0.10); color: #38bdf8; border: 1px solid rgba(56,189,248,0.20); }
 
/* ── PRESENCE TAGS ── */
.tag-quiet { background: rgba(56,189,248,0.08); color: #7dd3fc; border: 1px solid rgba(56,189,248,0.15); border-radius: 20px; padding: 2px 9px; font-family: 'Syne Mono', monospace; font-size: 9px; }
.tag-open { background: rgba(34,197,94,0.08); color: #86efac; border: 1px solid rgba(34,197,94,0.15); border-radius: 20px; padding: 2px 9px; font-family: 'Syne Mono', monospace; font-size: 9px; }
.tag-observing { background: rgba(167,139,250,0.08); color: #c4b5fd; border: 1px solid rgba(167,139,250,0.15); border-radius: 20px; padding: 2px 9px; font-family: 'Syne Mono', monospace; font-size: 9px; }
.tag-expressive { background: rgba(255,90,0,0.08); color: #fb923c; border: 1px solid rgba(255,90,0,0.15); border-radius: 20px; padding: 2px 9px; font-family: 'Syne Mono', monospace; font-size: 9px; }
.tag-easing { background: rgba(251,191,36,0.08); color: #fde68a; border: 1px solid rgba(251,191,36,0.15); border-radius: 20px; padding: 2px 9px; font-family: 'Syne Mono', monospace; font-size: 9px; }
 
/* ── INPUTS ── */
[data-testid="stTextInput"] input,
[data-testid="stTextArea"] textarea,
[data-testid="stSelectbox"] select,
[data-baseweb="select"] {
    background: #1A1A1A !important;
    border: 1px solid rgba(255,255,255,0.08) !important;
    border-radius: 10px !important;
    color: #F4F2ED !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 13px !important;
}
[data-testid="stTextInput"] input:focus,
[data-testid="stTextArea"] textarea:focus {
    border-color: rgba(255,90,0,0.4) !important;
    box-shadow: 0 0 0 2px rgba(255,90,0,0.08) !important;
}
 
/* ── BUTTONS ── */
[data-testid="baseButton-primary"],
.stButton button {
    background: #FF5A00 !important;
    color: white !important;
    border: none !important;
    border-radius: 9px !important;
    font-family: 'Syne', sans-serif !important;
    font-weight: 700 !important;
    font-size: 11px !important;
    letter-spacing: 0.06em !important;
    text-transform: uppercase !important;
    transition: all 0.2s !important;
    padding: 0.5rem 1rem !important;
}
.stButton button:hover {
    background: #cc4800 !important;
    transform: translateY(-1px) !important;
    box-shadow: 0 4px 16px rgba(255,90,0,0.3) !important;
}
.stButton button[kind="secondary"] {
    background: rgba(255,255,255,0.05) !important;
    border: 1px solid rgba(255,255,255,0.10) !important;
    color: #888 !important;
}
.stButton button[kind="secondary"]:hover {
    background: rgba(255,255,255,0.08) !important;
    color: #F4F2ED !important;
    box-shadow: none !important;
    transform: none !important;
}
 
/* ── DIVIDER ── */
hr { border-color: rgba(255,255,255,0.05) !important; }
 
/* ── DATAFRAME ── */
[data-testid="stDataFrame"] {
    border: 1px solid rgba(255,255,255,0.06) !important;
    border-radius: 12px !important;
    overflow: hidden !important;
}
 
/* ── EXPANDER ── */
[data-testid="stExpander"] {
    background: rgba(20,20,20,0.9) !important;
    border: 1px solid rgba(255,255,255,0.06) !important;
    border-radius: 12px !important;
}
[data-testid="stExpander"]:hover {
    border-color: rgba(255,255,255,0.10) !important;
}
 
/* ── LABEL ── */
[data-testid="stWidgetLabel"] p {
    font-family: 'Syne Mono', monospace !important;
    font-size: 10px !important;
    color: #555 !important;
    text-transform: uppercase !important;
    letter-spacing: 0.1em !important;
}
 
/* ── TABS ── */
[data-testid="stTabs"] [data-baseweb="tab"] {
    font-family: 'Syne Mono', monospace !important;
    font-size: 10px !important;
    color: #666 !important;
    text-transform: uppercase !important;
    letter-spacing: 0.08em !important;
}
[data-testid="stTabs"] [data-baseweb="tab"][aria-selected="true"] {
    color: #FF5A00 !important;
    border-bottom-color: #FF5A00 !important;
}
 
/* ── SELECT SLIDER ── */
[data-testid="stSlider"] [data-baseweb="slider"] [data-testid="stThumbValue"] {
    background: #FF5A00 !important;
}
 
/* ── METRICS ── */
[data-testid="stMetric"] { background: transparent !important; }
[data-testid="stMetricValue"] {
    font-family: 'Syne', sans-serif !important;
    font-weight: 800 !important;
    color: #FF5A00 !important;
}
 
/* ── ACT CARD ── */
.act-card {
    background: rgba(255,90,0,0.05);
    border: 1px solid rgba(255,90,0,0.15);
    border-left: 3px solid #FF5A00;
    border-radius: 0 12px 12px 0;
    padding: 1rem 1.25rem;
    margin-bottom: 8px;
}
.act-label {
    font-family: 'Syne Mono', monospace;
    font-size: 9px;
    color: #FF5A00;
    text-transform: uppercase;
    letter-spacing: 0.14em;
    margin-bottom: 6px;
    font-weight: 700;
}
 
/* ── PERSON CARD ── */
.person-card {
    background: rgba(20,20,20,0.9);
    border: 1px solid rgba(255,255,255,0.06);
    border-radius: 14px;
    padding: 1.25rem;
    margin-bottom: 8px;
    transition: all 0.2s;
}
.person-card:hover {
    border-color: rgba(255,255,255,0.10);
    background: rgba(26,26,26,0.95);
}
.person-name {
    font-family: 'Syne', sans-serif;
    font-weight: 700;
    font-size: 15px;
    color: #F4F2ED;
    margin-bottom: 4px;
}
.person-detail {
    font-family: 'Syne Mono', monospace;
    font-size: 10px;
    color: #555;
    margin-bottom: 8px;
    line-height: 1.6;
}
 
/* ── PULSE ── */
.room-pulse {
    background: linear-gradient(135deg, rgba(255,90,0,0.06), rgba(14,14,14,0.9));
    border: 1px solid rgba(255,90,0,0.15);
    border-radius: 16px;
    padding: 1.5rem;
    margin-bottom: 1rem;
}
 
/* ── FOOTER ── */
.nk-footer {
    font-family: 'Syne Mono', monospace;
    font-size: 10px;
    color: #2a2a2a;
    text-align: center;
    margin-top: 4rem;
    letter-spacing: 0.1em;
}
 
/* ── GLOW ── */
.glow-o { box-shadow: 0 0 20px rgba(255,90,0,0.08); }
.glow-g { box-shadow: 0 0 20px rgba(34,197,94,0.08); }
 
/* ── NOTICE ── */
.notice {
    background: rgba(255,90,0,0.06);
    border: 1px solid rgba(255,90,0,0.18);
    border-radius: 10px;
    padding: 0.875rem 1rem;
    font-family: 'Syne Mono', monospace;
    font-size: 11px;
    color: #888;
    line-height: 1.7;
    margin-bottom: 1rem;
}
.notice-dim {
    background: rgba(255,255,255,0.02);
    border: 1px solid rgba(255,255,255,0.06);
    border-radius: 10px;
    padding: 0.875rem 1rem;
    font-family: 'Syne Mono', monospace;
    font-size: 11px;
    color: #555;
    line-height: 1.7;
    margin-bottom: 1rem;
}
</style>
""", unsafe_allow_html=True)
 
 
# ─────────────────────────────────────────────────────────
# SESSION STATE
# ─────────────────────────────────────────────────────────
def init_state():
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
        st.session_state.user_role = None
        st.session_state.user_name = None
 
    if "members" not in st.session_state:
        st.session_state.members = generate_demo_members()
 
    if "facilitators" not in st.session_state:
        st.session_state.facilitators = generate_demo_facilitators()
 
    if "evenings" not in st.session_state:
        st.session_state.evenings = generate_demo_evenings()
 
    if "payments" not in st.session_state:
        st.session_state.payments = generate_demo_payments()
 
    if "messages" not in st.session_state:
        st.session_state.messages = []
 
    if "reflections" not in st.session_state:
        st.session_state.reflections = []
 
 
# ─────────────────────────────────────────────────────────
# DEMO DATA
# ─────────────────────────────────────────────────────────
PRESENCE_TAGS = ["quiet energy", "open to new", "observing", "expressive", "needs easing"]
TAG_COLORS = {
    "quiet energy": "tag-quiet",
    "open to new": "tag-open",
    "observing": "tag-observing",
    "expressive": "tag-expressive",
    "needs easing": "tag-easing",
}
 
NAMES = [
    "Kabir Anand", "Ishita Rao", "Dev Sharma", "Naina Gupta", "Vikram Tiwari",
    "Ananya Singh", "Raj Mehta", "Pooja Verma", "Aditya Kumar", "Meera Joshi",
    "Siddharth Nair", "Kavya Reddy", "Arjun Patel", "Simran Kaur", "Rahul Gupta",
    "Divya Sharma", "Karan Malhotra", "Priyanka Bose", "Aakash Mishra", "Shruti Agarwal",
    "Rohan Das", "Neha Kapoor", "Varun Sinha", "Tanvi Mehta", "Ayaan Khan",
    "Riya Shah", "Manav Choudhary", "Kiara Pillai", "Abhishek Rao", "Sana Qureshi",
    "Dhruv Banerjee", "Alia Rathore", "Parth Desai", "Shreya Pandey", "Nikhil Jain",
    "Avni Saxena", "Kartik Oberoi", "Disha Thakur", "Yash Chopra", "Ritu Menon",
]
 
INTENTS = [
    "moved here two months ago. wanted something real.",
    "tired of the same four people and same three cafés.",
    "introvert trying to push myself. the format feels safer.",
    "new to the city. want to build a circle that actually fits.",
    "something is missing from my social life but i can't name it.",
    "socially confident but my existing circle has become a loop.",
    "looking for evenings that feel different from the usual.",
    "want to meet people who are actually curious about things.",
    "i like people but not parties. this sounds right.",
    "my college group scattered. starting fresh felt easier here.",
]
 
BUDGETS = ["₹400–₹600", "₹600–₹1000", "under ₹400", "₹600–₹1000", "₹400–₹600"]
AVAILS = ["weekend evenings", "saturday evenings", "flexible", "sunday afternoons", "both weekend days"]
STATUSES = ["approved", "approved", "approved", "pending", "pending", "waitlist", "waitlist", "declined"]
COMFORT = [3, 4, 5, 2, 3, 4, 5, 3, 2, 4]
NEWSLETTER = ["yes", "yes", "no", "yes", "yes", "no", "yes", "yes"]
 
 
def auto_presence_tag(comfort: int, intent: str) -> str:
    intent_l = intent.lower()
    if comfort <= 2 and "introvert" in intent_l:
        return "needs easing"
    elif comfort <= 2:
        return "quiet energy"
    elif "observ" in intent_l or "watch" in intent_l:
        return "observing"
    elif comfort >= 4 and ("confid" in intent_l or "social" in intent_l):
        return "expressive"
    else:
        return "open to new"
 
 
def auto_tier(sessions: int) -> str:
    if sessions >= 4:
        return "in between plans"
    return "first out"
 
 
def generate_demo_members():
    members = []
    session_counts = [0,0,1,2,3,4,0,1,2,0,3,1,0,2,4,1,0,2,3,0,1,4,2,0,3,1,2,0,1,3,0,2,1,4,0,3,1,2,0,1]
    for i, name in enumerate(NAMES):
        comfort = COMFORT[i % len(COMFORT)]
        intent = INTENTS[i % len(INTENTS)]
        sessions = session_counts[i] if i < len(session_counts) else 0
        tag = auto_presence_tag(comfort, intent)
        members.append({
            "id": f"m{i+1}",
            "name": name,
            "email": f"{name.lower().replace(' ', '.')}{i*3}@gmail.com",
            "phone": f"98{str(76543210 + i * 111111)[:8]}",
            "intent": intent,
            "budget": BUDGETS[i % len(BUDGETS)],
            "availability": AVAILS[i % len(AVAILS)],
            "comfort_level": comfort,
            "presence_tag": tag,
            "status": STATUSES[i % len(STATUSES)],
            "sessions": sessions,
            "tier": auto_tier(sessions),
            "newsletter": NEWSLETTER[i % len(NEWSLETTER)],
            "ready_for_invite": sessions > 0,
            "notes": "",
            "joined": f"2026-04-{str(15 + i % 10).zfill(2)}",
        })
    return members
 
 
def generate_demo_facilitators():
    return [
        {"id": "f1", "name": "Riya Kapoor", "uid": "riya.fac", "style": "calm", "status": "holding",
         "sessions_run": 5, "access": "worth it", "refs": 3, "on_leave": False,
         "notes": "natural at reading the room. makes shy people feel seen immediately."},
        {"id": "f2", "name": "Aryan Mehta", "uid": "aryan.fac", "style": "energetic", "status": "holding",
         "sessions_run": 4, "access": "in between plans", "refs": 2, "on_leave": False,
         "notes": "high energy, great storyteller. keeps conversation alive effortlessly."},
        {"id": "f3", "name": "Sneha Joshi", "uid": "sneha.fac", "style": "calm", "status": "noticing",
         "sessions_run": 6, "access": "yhttb", "refs": 4, "on_leave": False,
         "notes": "most empathetic on the team. zero exclusion energy. natural leader."},
        {"id": "f4", "name": "Rohan Verma", "uid": "rohan.fac", "style": "calm", "status": "noticing",
         "sessions_run": 2, "access": "first out", "refs": 2, "on_leave": False,
         "notes": "still being observed. promising — funny and warm."},
        {"id": "f5", "name": "Priya Sharma", "uid": "priya.fac", "style": "energetic", "status": "holding",
         "sessions_run": 3, "access": "in between plans", "refs": 2, "on_leave": False,
         "notes": "creative and structured. great at activity facilitation."},
        {"id": "f6", "name": "Dev Bhatia", "uid": "dev.fac", "style": "calm", "status": "holding",
         "sessions_run": 4, "access": "in between plans", "refs": 2, "on_leave": False,
         "notes": "grounding presence. good at defusing awkwardness naturally."},
        {"id": "f7", "name": "Tanya Mishra", "uid": "tanya.fac", "style": "energetic", "status": "stepped away",
         "sessions_run": 3, "access": "first out", "refs": 2, "on_leave": True,
         "notes": "energetic and creative. members always mention her in feedback."},
    ]
 
 
def generate_demo_evenings():
    return [
        {"id": "e1", "name": "canvas night — mp nagar", "tier": "first out",
         "date": "2026-04-26", "time": "18:00", "venue": "bhopal bytes café",
         "capacity": 8, "price": 499, "vibe": "mixed",
         "act1": "homemade iced tea. no names. anonymous fun-fact prompt cards.",
         "act2": "half-and-half canvas painting. two people share one canvas without speaking about what they're painting.",
         "act3": "warm chai at private corner. name reveal. canvas discussion.",
         "facilitator": "f1", "transport": "e-rickshaw pre-booked, ₹30/person",
         "notes": "keep it playful. the mess is the point.",
         "confirmed": ["m2", "m3", "m5"], "invited": ["m1", "m2", "m3", "m4", "m5", "m6"],
         "no_show": []},
        {"id": "e2", "name": "after dark walk — upper lake", "tier": "first out",
         "date": "2026-05-03", "time": "19:00", "venue": "upper lake promenade",
         "capacity": 10, "price": 299, "vibe": "introvert",
         "act1": "first name only. one word for current mood.",
         "act2": "45-minute walk with 5 prompt stops. prompt cards distributed.",
         "act3": "chai at nearby dhaba. full names. open conversation.",
         "facilitator": "f2", "transport": "walk the entire route together.",
         "notes": "pace slow. the prompts are everything here.",
         "confirmed": ["m7", "m8"], "invited": ["m7", "m8", "m9", "m10"],
         "no_show": []},
        {"id": "e3", "name": "pottery evening — arera colony", "tier": "in between plans",
         "date": "2026-05-10", "time": "17:00", "venue": "clay studio, arera colony",
         "capacity": 6, "price": 899, "vibe": "social",
         "act1": "welcome mocktail. clay stations ready. just begin.",
         "act2": "45-min pottery session. facilitator circulates quietly.",
         "act3": "display all pieces. names. chai and honest reviews.",
         "facilitator": "f3", "transport": "own transport. central location.",
         "notes": "intimate group. handle energy carefully.",
         "confirmed": ["m11", "m12", "m13"], "invited": ["m11", "m12", "m13", "m14", "m15"],
         "no_show": []},
    ]
 
 
def generate_demo_payments():
    return [
        {"id": "p1", "member": "Ishita Rao", "evening": "canvas night — mp nagar", "amount": 499, "method": "razorpay", "status": "paid", "date": "2026-04-24"},
        {"id": "p2", "member": "Dev Sharma", "evening": "canvas night — mp nagar", "amount": 499, "method": "upi", "status": "paid", "date": "2026-04-24"},
        {"id": "p3", "member": "Naina Gupta", "evening": "after dark walk — upper lake", "amount": 299, "method": "razorpay", "status": "pending", "date": "2026-04-25"},
        {"id": "p4", "member": "Vikram Tiwari", "evening": "after dark walk — upper lake", "amount": 299, "method": "cash", "status": "paid", "date": "2026-04-25"},
        {"id": "p5", "member": "Raj Mehta", "evening": "pottery evening — arera colony", "amount": 899, "method": "upi", "status": "pending", "date": "2026-04-26"},
    ]
 
 
# ─────────────────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────────────────
def html(content: str):
    st.markdown(content, unsafe_allow_html=True)
 
 
def section_header(title: str, sub: str):
    html(f"""
    <div class="section-head">
        <div class="section-title">{title}</div>
        <div class="section-sub">{sub}</div>
    </div>
    """)
 
 
def card(content: str, variant: str = ""):
    html(f'<div class="nk-card {variant}">{content}</div>')
 
 
def badge(text: str, color: str = "o") -> str:
    return f'<span class="badge badge-{color}">{text}</span>'
 
 
def presence_tag_html(tag: str) -> str:
    css = TAG_COLORS.get(tag, "tag-quiet")
    return f'<span class="{css}">{tag}</span>'
 
 
def tier_badge(tier: str) -> str:
    if tier == "in between plans":
        return badge("IBP", "p")
    elif tier == "worth it":
        return badge("Worth It", "g")
    elif tier == "yhttb":
        return badge("YHTTB", "y")
    return badge("First Out", "o")
 
 
def status_badge(status: str) -> str:
    colors = {"approved": "g", "pending": "y", "waitlist": "p", "declined": "r"}
    return badge(status, colors.get(status, "o"))
 
 
def smart_match_score(member: dict, evening: dict) -> int:
    """score 0–100 for how well a member fits an evening"""
    score = 50
    tag = member.get("presence_tag", "")
    vibe = evening.get("vibe", "mixed")
    comfort = member.get("comfort_level", 3)
 
    if vibe == "introvert" and tag in ["quiet energy", "observing", "needs easing"]:
        score += 20
    elif vibe == "social" and tag in ["expressive", "open to new"]:
        score += 20
    elif vibe == "mixed":
        score += 10
 
    if comfort >= 4:
        score += 15
    elif comfort <= 2:
        score -= 10
 
    if member.get("status") == "approved":
        score += 15
 
    return min(100, max(0, score))
 
 
# ─────────────────────────────────────────────────────────
# LOGIN
# ─────────────────────────────────────────────────────────
CREDENTIALS = {
    "manju": {"pass": "founder2026", "role": "founder", "name": "Manju Singh"},
    "riya.fac": {"pass": "riya123", "role": "facilitator", "name": "Riya Kapoor"},
    "aryan.fac": {"pass": "aryan123", "role": "facilitator", "name": "Aryan Mehta"},
    "sneha.fac": {"pass": "sneha123", "role": "facilitator", "name": "Sneha Joshi"},
    "rohan.fac": {"pass": "rohan123", "role": "facilitator", "name": "Rohan Verma"},
    "priya.fac": {"pass": "priya123", "role": "facilitator", "name": "Priya Sharma"},
    "dev.fac": {"pass": "dev123", "role": "facilitator", "name": "Dev Bhatia"},
    "tanya.fac": {"pass": "tanya123", "role": "facilitator", "name": "Tanya Mishra"},
}
 
 
def render_login():
    st.markdown("""
    <style>
    [data-testid="stApp"] { background: #0E0E0E !important; }
    .login-wrap { max-width: 420px; margin: 8vh auto 0; }
    .login-logo { font-family: 'Syne', sans-serif; font-weight: 800; font-size: 52px; 
                  letter-spacing: -1px; color: #F4F2ED; margin-bottom: 4px; }
    .login-logo em { color: #FF5A00; font-style: normal; }
    .login-tagline { font-family: 'Syne Mono', monospace; font-size: 10px; color: #333; 
                     letter-spacing: 0.18em; text-transform: uppercase; margin-bottom: 3rem; }
    .login-card { background: rgba(20,20,20,0.95); border: 1px solid rgba(255,255,255,0.07);
                  border-radius: 20px; padding: 2.5rem; backdrop-filter: blur(20px); }
    .login-title { font-family: 'Syne', sans-serif; font-weight: 700; font-size: 22px;
                   color: #F4F2ED; margin-bottom: 4px; }
    .login-sub { font-family: 'Syne Mono', monospace; font-size: 10px; color: #444;
                 margin-bottom: 2rem; letter-spacing: 0.04em; }
    </style>
    <div class="login-wrap">
        <div class="login-logo">N<em>**</em>K</div>
        <div class="login-tagline">// your third place · control room</div>
        <div class="login-card">
            <div class="login-title">welcome back.</div>
            <div class="login-sub">// credentials shared by manju only</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
 
    with st.container():
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.markdown("<br>", unsafe_allow_html=True)
            username = st.text_input("username", placeholder="enter username", key="login_user")
            password = st.text_input("password", placeholder="••••••••", type="password", key="login_pass")
            if st.button("enter →", use_container_width=True, key="login_btn"):
                if username in CREDENTIALS and CREDENTIALS[username]["pass"] == password:
                    st.session_state.logged_in = True
                    st.session_state.user_role = CREDENTIALS[username]["role"]
                    st.session_state.user_name = CREDENTIALS[username]["name"]
                    st.rerun()
                else:
                    st.error("// invalid credentials. contact manju.")
 
    html('<div class="nk-footer">built quietly · bhopal</div>')
 
 
# ─────────────────────────────────────────────────────────
# SIDEBAR
# ─────────────────────────────────────────────────────────
def render_sidebar():
    with st.sidebar:
        html(f"""
        <div style="padding: 0.5rem 0 1.5rem">
            <div class="sidebar-logo">N<span>**</span>K</div>
            <div class="sidebar-tag">// control room · bhopal</div>
            <div style="background: rgba(255,90,0,0.08); border: 1px solid rgba(255,90,0,0.18);
                        border-radius: 20px; padding: 3px 10px; display: inline-flex; align-items: center;
                        gap: 5px; margin-bottom: 0.5rem;">
                <div style="width: 5px; height: 5px; border-radius: 50%; background: #FF5A00;
                             animation: pulse 2s infinite;"></div>
                <span style="font-family: 'Syne Mono', monospace; font-size: 9px; color: #FF5A00;
                              text-transform: uppercase; letter-spacing: 0.08em;">
                    {st.session_state.user_role}
                </span>
            </div>
        </div>
        """)
 
        is_founder = st.session_state.user_role == "founder"
 
        if is_founder:
            nav_options = [
                "◎  control room",
                "→  incoming",
                "·  inside",
                "✦  experience builder",
                "◈  evenings",
                "★  space holders",
                "◇  notes",
                "₹  contributions",
                "~  insights",
            ]
        else:
            nav_options = [
                "◎  control room",
                "◈  evenings",
                "★  space holders",
                "◇  notes",
            ]
 
        selection = st.radio(
            "navigation",
            nav_options,
            label_visibility="collapsed",
            key="nav",
        )
 
        st.markdown("<br>" * 4, unsafe_allow_html=True)
 
        # user info
        html(f"""
        <div style="border-top: 1px solid rgba(255,255,255,0.05); padding-top: 1rem;">
            <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 10px;">
                <div style="width: 34px; height: 34px; border-radius: 50%; 
                            background: rgba(255,90,0,0.1); border: 2px solid #FF5A00;
                            display: flex; align-items: center; justify-content: center;
                            font-family: 'Syne', sans-serif; font-weight: 800; 
                            font-size: 13px; color: #FF5A00;">
                    {st.session_state.user_name[0]}
                </div>
                <div>
                    <div style="font-size: 13px; font-weight: 700; font-family: 'Syne', sans-serif;
                                color: #F4F2ED;">{st.session_state.user_name}</div>
                    <div style="font-size: 10px; color: #444; font-family: 'Syne Mono', monospace;">
                        {st.session_state.user_role}
                    </div>
                </div>
            </div>
        </div>
        """)
 
        if st.button("→ sign out", use_container_width=True, key="logout"):
            st.session_state.logged_in = False
            st.session_state.user_role = None
            st.session_state.user_name = None
            st.rerun()
 
    return selection.split("  ")[1].strip() if "  " in selection else selection.strip()
 
 
# ─────────────────────────────────────────────────────────
# PAGES
# ─────────────────────────────────────────────────────────
 
def page_control_room():
    section_header("control room", "not a dashboard. just where things come together.")
 
    members = st.session_state.members
    facs = st.session_state.facilitators
    evenings = st.session_state.evenings
    payments = st.session_state.payments
 
    approved = [m for m in members if m["status"] == "approved"]
    pending = [m for m in members if m["status"] in ["pending", "waitlist"]]
    active_facs = [f for f in facs if f["status"] != "stepped away"]
    total_rev = sum(p["amount"] for p in payments if p["status"] == "paid")
    nl_subs = [m for m in members if m.get("newsletter") == "yes"]
 
    # stats
    cols = st.columns(6)
    stats = [
        ("total people", len(members), "#FF5A00"),
        ("incoming", len(pending), "#fbbf24"),
        ("inside", len(approved), "#22c55e"),
        ("evenings planned", len(evenings), "#a78bfa"),
        ("space holders", len(active_facs), "#38bdf8"),
        ("contributions", f"₹{total_rev:,}", "#22c55e"),
    ]
    for i, (label, val, color) in enumerate(stats):
        with cols[i]:
            html(f"""
            <div class="stat-box" style="--accent: {color};">
                <div class="stat-n" style="color: {color};">{val}</div>
                <div class="stat-l">{label}</div>
            </div>
            """)
 
    st.markdown("<br>", unsafe_allow_html=True)
 
    col1, col2 = st.columns([1, 1])
 
    with col1:
        html('<div style="font-family: Bebas Neue, Syne, sans-serif; font-size: 16px; letter-spacing: 1px; color: #F4F2ED; margin-bottom: 1rem; display: flex; align-items: center; gap: 10px;">room pulse <div style="flex: 1; height: 1px; background: rgba(255,255,255,0.05);"></div></div>')
 
        # tag distribution
        all_tags = [m["presence_tag"] for m in approved]
        tag_counts = {t: all_tags.count(t) for t in PRESENCE_TAGS if all_tags.count(t) > 0}
 
        html('<div class="room-pulse">')
        for tag, count in sorted(tag_counts.items(), key=lambda x: -x[1]):
            pct = int(count / max(len(all_tags), 1) * 100)
            css = TAG_COLORS.get(tag, "tag-quiet")
            html(f"""
            <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 10px;">
                <span class="{css}" style="min-width: 110px;">{tag}</span>
                <div style="flex: 1; background: rgba(255,255,255,0.04); border-radius: 4px; height: 4px; overflow: hidden;">
                    <div style="width: {pct}%; height: 100%; background: rgba(255,90,0,0.5); border-radius: 4px;"></div>
                </div>
                <span style="font-family: 'Syne Mono', monospace; font-size: 10px; color: #444;">{count}</span>
            </div>
            """)
 
        # room vibe signals
        introvert_count = tag_counts.get("quiet energy", 0) + tag_counts.get("needs easing", 0) + tag_counts.get("observing", 0)
        creative_count = tag_counts.get("expressive", 0) + tag_counts.get("open to new", 0)
        signals = []
        if introvert_count > creative_count:
            signals.append(("introvert heavy", "badge-b"))
        else:
            signals.append(("creative leaning", "badge-o"))
        if len(approved) < 10:
            signals.append(("low energy", "badge-y"))
        else:
            signals.append(("ready to grow", "badge-g"))
 
        html('<div style="display: flex; gap: 8px; margin-top: 1rem; flex-wrap: wrap;">' + "".join([f'<span class="badge {c}">{s}</span>' for s, c in signals]) + '</div>')
        html('</div>')
 
        # upcoming evenings
        html('<div style="font-family: Bebas Neue, Syne, sans-serif; font-size: 16px; letter-spacing: 1px; color: #F4F2ED; margin: 1.5rem 0 1rem; display: flex; align-items: center; gap: 10px;">upcoming <div style="flex: 1; height: 1px; background: rgba(255,255,255,0.05);"></div></div>')
        for ev in evenings[:3]:
            f = next((x for x in facs if x["id"] == ev["facilitator"]), None)
            html(f"""
            <div class="nk-card nk-card-accent" style="margin-bottom: 8px;">
                <div style="font-family: 'Syne', sans-serif; font-weight: 700; font-size: 14px; margin-bottom: 4px;">{ev['name']}</div>
                <div style="font-family: 'Syne Mono', monospace; font-size: 10px; color: #555; line-height: 1.7;">
                    {ev['date']} · {ev['time']} · {ev['venue']}<br>
                    capacity {ev['capacity']} · ₹{ev['price']} · {f['name'] if f else 'unassigned'}
                </div>
            </div>
            """)
 
    with col2:
        html('<div style="font-family: Bebas Neue, Syne, sans-serif; font-size: 16px; letter-spacing: 1px; color: #F4F2ED; margin-bottom: 1rem; display: flex; align-items: center; gap: 10px;">recent arrivals <div style="flex: 1; height: 1px; background: rgba(255,255,255,0.05);"></div></div>')
 
        for m in members[-8:][::-1]:
            a = m.get("status", "pending")
            html(f"""
            <div class="nk-card" style="margin-bottom: 6px; padding: 1rem 1.25rem;">
                <div style="display: flex; align-items: center; justify-content: space-between;">
                    <div>
                        <div style="font-family: 'Syne', sans-serif; font-weight: 700; font-size: 13px;">{m['name']}</div>
                        <div style="font-family: 'Syne Mono', monospace; font-size: 9px; color: #444; margin-top: 2px;">{m['joined']} · {m['budget']}</div>
                    </div>
                    <div style="display: flex; gap: 6px; align-items: center;">
                        {presence_tag_html(m['presence_tag'])}
                        {status_badge(a)}
                    </div>
                </div>
            </div>
            """)
 
    html('<div class="nk-footer">built quietly · bhopal</div>')
 
 
def page_incoming():
    section_header("incoming", "people who paused long enough to say yes.")
 
    members = st.session_state.members
    pending = [m for m in members if m["status"] in ["pending", "waitlist"]]
 
    col1, col2, col3 = st.columns(3)
    with col1:
        html(f'<div class="stat-box" style="--accent:#fbbf24;"><div class="stat-n" style="color:#fbbf24;">{len([m for m in members if m["status"]=="pending"])}</div><div class="stat-l">waiting</div></div>')
    with col2:
        html(f'<div class="stat-box" style="--accent:#a78bfa;"><div class="stat-n" style="color:#a78bfa;">{len([m for m in members if m["status"]=="waitlist"])}</div><div class="stat-l">on hold</div></div>')
    with col3:
        html(f'<div class="stat-box" style="--accent:#22c55e;"><div class="stat-n" style="color:#22c55e;">{len([m for m in members if m["status"]=="approved"])}</div><div class="stat-l">inside</div></div>')
 
    st.markdown("<br>", unsafe_allow_html=True)
 
    filt_col1, filt_col2 = st.columns([3, 1])
    with filt_col2:
        filt = st.selectbox("filter", ["all incoming", "waiting", "on hold"], label_visibility="collapsed")
 
    if filt == "waiting":
        pending = [m for m in pending if m["status"] == "pending"]
    elif filt == "on hold":
        pending = [m for m in pending if m["status"] == "waitlist"]
 
    for m in pending:
        with st.expander(f"{m['name']}  ·  {m['presence_tag']}", expanded=False):
            col1, col2 = st.columns([2, 1])
            with col1:
                html(f"""
                <div class="person-card">
                    <div class="person-name">{m['name']}</div>
                    <div class="person-detail">
                        {m['email']} · {m['phone']}<br>
                        budget: {m['budget']} · availability: {m['availability']}<br>
                        joined: {m['joined']}
                    </div>
                    <div style="font-size: 13px; color: #888; line-height: 1.7; font-style: italic; 
                                margin-bottom: 1rem; border-left: 2px solid rgba(255,90,0,0.3); padding-left: 1rem;">
                        "{m['intent']}"
                    </div>
                    <div style="display: flex; gap: 8px; flex-wrap: wrap;">
                        {presence_tag_html(m['presence_tag'])}
                        {status_badge(m['status'])}
                        {tier_badge(m['tier'])}
                    </div>
                </div>
                """)
            with col2:
                html(f"""
                <div class="nk-card" style="text-align: center;">
                    <div style="font-family: 'Syne Mono', monospace; font-size: 10px; color: #555; 
                                text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 1rem;">
                        comfort level
                    </div>
                    <div style="font-family: 'Syne', sans-serif; font-size: 36px; font-weight: 800; 
                                color: #FF5A00; margin-bottom: 4px;">
                        {m['comfort_level']}/5
                    </div>
                    <div style="font-family: 'Syne Mono', monospace; font-size: 10px; color: #444;">
                        newsletter: {m['newsletter']}
                    </div>
                </div>
                """)
 
            c1, c2, c3, c4 = st.columns(4)
            idx = next(i for i, x in enumerate(st.session_state.members) if x["id"] == m["id"])
            with c1:
                if st.button("invite in", key=f"approve_{m['id']}", use_container_width=True):
                    st.session_state.members[idx]["status"] = "approved"
                    st.rerun()
            with c2:
                if st.button("not this time", key=f"decline_{m['id']}", use_container_width=True):
                    st.session_state.members[idx]["status"] = "declined"
                    st.rerun()
            with c3:
                if st.button("hold for now", key=f"hold_{m['id']}", use_container_width=True):
                    st.session_state.members[idx]["status"] = "waitlist"
                    st.rerun()
            with c4:
                if st.button("feels like a space holder", key=f"fac_{m['id']}", use_container_width=True):
                    st.session_state.members[idx]["notes"] = (st.session_state.members[idx].get("notes", "") + " [flagged as potential space holder]").strip()
                    st.rerun()
 
    html('<div class="nk-footer">built quietly · bhopal</div>')
 
 
def page_inside():
    section_header("inside", "not users. just people who stayed.")
 
    members = st.session_state.members
    approved = [m for m in members if m["status"] == "approved"]
 
    html(f"""
    <div class="notice-dim">
        {len(approved)} people inside · 
        {len([m for m in approved if m['sessions'] >= 4])} in between plans · 
        {len([m for m in approved if m.get('ready_for_invite')])} ready for next invite
    </div>
    """)
 
    search = st.text_input("search", placeholder="search by name or presence tag...", label_visibility="collapsed")
 
    if search:
        approved = [m for m in approved if search.lower() in m["name"].lower() or search.lower() in m["presence_tag"].lower()]
 
    tab1, tab2 = st.tabs(["everyone", "ready for invite"])
 
    with tab1:
        for m in approved:
            idx = next(i for i, x in enumerate(st.session_state.members) if x["id"] == m["id"])
            col1, col2, col3 = st.columns([3, 1, 1])
            with col1:
                html(f"""
                <div class="person-card">
                    <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 6px;">
                        <div class="person-name">{m['name']}</div>
                        <div style="display: flex; gap: 6px;">
                            {presence_tag_html(m['presence_tag'])}
                            {tier_badge(m['tier'])}
                        </div>
                    </div>
                    <div class="person-detail">
                        {m['sessions']} sessions attended · {m['budget']} · {m['availability']}<br>
                        newsletter: {m['newsletter']} · joined: {m['joined']}
                    </div>
                    <div style="font-size: 12px; color: #555; font-style: italic;">"{m['intent']}"</div>
                </div>
                """)
            with col2:
                ready = st.toggle("ready for invite", value=m.get("ready_for_invite", False), key=f"ready_{m['id']}")
                if ready != m.get("ready_for_invite", False):
                    st.session_state.members[idx]["ready_for_invite"] = ready
                    st.rerun()
            with col3:
                note = st.text_input("note", value=m.get("notes", ""), key=f"note_{m['id']}", label_visibility="collapsed", placeholder="add a note...")
                if note != m.get("notes", ""):
                    st.session_state.members[idx]["notes"] = note
 
    with tab2:
        ready_members = [m for m in approved if m.get("ready_for_invite")]
        if ready_members:
            for m in ready_members:
                html(f"""
                <div class="nk-card nk-card-green" style="margin-bottom: 8px;">
                    <div style="display: flex; align-items: center; justify-content: space-between;">
                        <div>
                            <div style="font-family: 'Syne', sans-serif; font-weight: 700;">{m['name']}</div>
                            <div class="person-detail" style="margin-bottom: 0;">{m['sessions']} sessions · {m['tier']}</div>
                        </div>
                        <div style="display: flex; gap: 6px;">
                            {presence_tag_html(m['presence_tag'])}
                        </div>
                    </div>
                </div>
                """)
        else:
            html('<div class="notice-dim">// no one marked as ready yet. toggle in the everyone tab.</div>')
 
    html('<div class="nk-footer">built quietly · bhopal</div>')
 
 
def page_experience_builder():
    section_header("experience builder", "not events. just evenings that feel different.")
 
    html('<div class="notice">// don\'t design too much. leave space for it to happen.</div>')
 
    with st.form("exp_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("evening name", placeholder="canvas night — mp nagar")
            venue = st.text_input("location", placeholder="bhopal bytes café, mp nagar")
            date_val = st.date_input("date", value=date.today())
            time_val = st.time_input("time", value=datetime.strptime("18:00", "%H:%M").time())
        with col2:
            tier = st.selectbox("tier", ["first out", "in between plans", "worth it", "yhttb"])
            capacity = st.slider("capacity", 4, 12, 8)
            price = st.number_input("price per person (₹)", min_value=0, value=499, step=50)
            vibe = st.selectbox("vibe", ["introvert", "social", "mixed"])
 
        st.markdown("---")
        html("""
        <div style="font-family: 'Syne Mono', monospace; font-size: 10px; color: #555; 
                    text-transform: uppercase; letter-spacing: 0.12em; margin-bottom: 1rem;">
            the three acts
        </div>
        """)
 
        col_a1, col_a2, col_a3 = st.columns(3)
        with col_a1:
            html('<div class="act-label">act 1 — arrival</div>')
            act1 = st.text_area("act1", placeholder="how do people arrive? what's the first thing they feel?", label_visibility="collapsed", height=100)
        with col_a2:
            html('<div class="act-label">act 2 — shared activity</div>')
            act2 = st.text_area("act2", placeholder="what do they do together? how does connection happen?", label_visibility="collapsed", height=100)
        with col_a3:
            html('<div class="act-label">act 3 — unwind</div>')
            act3 = st.text_area("act3", placeholder="chai + cookies + conversation. how does the evening close?", label_visibility="collapsed", height=100)
 
        col_t, col_n = st.columns(2)
        with col_t:
            transport = st.text_input("transport", placeholder="e.g. e-rickshaw pre-booked, ₹30/person")
        with col_n:
            notes = st.text_area("vibe notes", placeholder="anything specific about the energy or flow...", height=68)
 
        fac_options = {f["name"]: f["id"] for f in st.session_state.facilitators if f["status"] != "stepped away"}
        fac_name = st.selectbox("assign space holder", ["unassigned"] + list(fac_options.keys()))
        fac_id = fac_options.get(fac_name, "")
 
        submitted = st.form_submit_button("save evening →", use_container_width=True)
        if submitted and name:
            new_ev = {
                "id": f"e{len(st.session_state.evenings)+1}",
                "name": name.lower(), "tier": tier, "date": str(date_val),
                "time": str(time_val)[:5], "venue": venue.lower(), "capacity": capacity,
                "price": price, "vibe": vibe, "act1": act1, "act2": act2, "act3": act3,
                "facilitator": fac_id, "transport": transport, "notes": notes,
                "confirmed": [], "invited": [], "no_show": [],
            }
            st.session_state.evenings.append(new_ev)
            st.success(f"// {name.lower()} added to evenings.")
 
    html('<div class="nk-footer">built quietly · bhopal</div>')
 
 
def page_evenings():
    section_header("evenings", "where everything becomes real.")
 
    evenings = st.session_state.evenings
    members = st.session_state.members
    facs = st.session_state.facilitators
 
    approved = [m for m in members if m["status"] == "approved"]
 
    for ev in evenings:
        fac = next((f for f in facs if f["id"] == ev["facilitator"]), None)
        confirmed_count = len(ev.get("confirmed", []))
        invited_count = len(ev.get("invited", []))
        no_show_count = len(ev.get("no_show", []))
 
        with st.expander(f"{ev['name']}  ·  {ev['date']}  ·  {ev['tier']}", expanded=True):
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                html(f'<div class="stat-box" style="--accent:#FF5A00;padding:1rem;"><div class="stat-n" style="color:#FF5A00;font-size:28px;">{invited_count}</div><div class="stat-l">invited</div></div>')
            with col2:
                html(f'<div class="stat-box" style="--accent:#22c55e;padding:1rem;"><div class="stat-n" style="color:#22c55e;font-size:28px;">{confirmed_count}</div><div class="stat-l">confirmed</div></div>')
            with col3:
                html(f'<div class="stat-box" style="--accent:#ef4444;padding:1rem;"><div class="stat-n" style="color:#ef4444;font-size:28px;">{no_show_count}</div><div class="stat-l">no show</div></div>')
            with col4:
                html(f'<div class="stat-box" style="--accent:#a78bfa;padding:1rem;"><div class="stat-n" style="color:#a78bfa;font-size:28px;">{ev["capacity"]}</div><div class="stat-l">capacity</div></div>')
 
            st.markdown("<br>", unsafe_allow_html=True)
 
            col_detail, col_acts = st.columns([1, 2])
            with col_detail:
                html(f"""
                <div class="nk-card">
                    <div style="font-family: 'Syne Mono', monospace; font-size: 10px; color: #555; line-height: 1.8;">
                        date: {ev['date']} · {ev['time']}<br>
                        venue: {ev['venue']}<br>
                        tier: {ev['tier']}<br>
                        vibe: {ev['vibe']}<br>
                        price: ₹{ev['price']}/person<br>
                        transport: {ev.get('transport', '—')}<br>
                        space holder: {fac['name'] if fac else 'unassigned'}<br>
                    </div>
                    {f'<div style="margin-top: 10px; font-size: 12px; color: #555; font-style: italic;">// {ev["notes"]}</div>' if ev.get('notes') else ''}
                </div>
                """)
 
                # assign facilitator
                fac_options = {f["name"]: f["id"] for f in facs if f["status"] != "stepped away"}
                current_fac = fac["name"] if fac else "unassigned"
                new_fac_name = st.selectbox("reassign space holder", ["unassigned"] + list(fac_options.keys()),
                                            index=0 if current_fac == "unassigned" else list(fac_options.keys()).index(current_fac) + 1 if current_fac in fac_options else 0,
                                            key=f"fac_{ev['id']}")
                if new_fac_name != "unassigned":
                    ev_idx = next(i for i, x in enumerate(st.session_state.evenings) if x["id"] == ev["id"])
                    st.session_state.evenings[ev_idx]["facilitator"] = fac_options[new_fac_name]
 
            with col_acts:
                html(f"""
                <div class="act-card"><div class="act-label">act 1 — arrival</div>
                    <div style="font-size: 12px; color: #888; line-height: 1.6; margin-top: 4px;">{ev.get('act1', '—')}</div>
                </div>
                <div class="act-card"><div class="act-label">act 2 — shared activity</div>
                    <div style="font-size: 12px; color: #888; line-height: 1.6; margin-top: 4px;">{ev.get('act2', '—')}</div>
                </div>
                <div class="act-card"><div class="act-label">act 3 — unwind</div>
                    <div style="font-size: 12px; color: #888; line-height: 1.6; margin-top: 4px;">{ev.get('act3', '—')}</div>
                </div>
                """)
 
            st.markdown("---")
 
            # smart suggestions
            html(f'<div style="font-family: \'Syne Mono\', monospace; font-size: 10px; color: #555; text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 0.75rem;">// smart suggestions for this evening</div>')
 
            ready = [m for m in approved if m.get("ready_for_invite") and m["id"] not in ev.get("invited", [])]
            scored = sorted([(m, smart_match_score(m, ev)) for m in ready], key=lambda x: -x[1])[:5]
 
            if scored:
                for m, score in scored:
                    col_s1, col_s2, col_s3 = st.columns([3, 1, 1])
                    with col_s1:
                        html(f"""
                        <div style="display: flex; align-items: center; gap: 10px; padding: 0.75rem 0; 
                                    border-bottom: 1px solid rgba(255,255,255,0.04);">
                            <div>
                                <div style="font-family: 'Syne', sans-serif; font-weight: 700; font-size: 13px;">{m['name']}</div>
                                <div style="font-family: 'Syne Mono', monospace; font-size: 9px; color: #444; margin-top: 2px;">{m['presence_tag']} · {m['sessions']} sessions</div>
                            </div>
                        </div>
                        """)
                    with col_s2:
                        html(f'<div style="font-family: \'Syne\', sans-serif; font-weight: 800; font-size: 20px; color: #FF5A00; padding-top: 0.75rem;">{score}</div>')
                    with col_s3:
                        ev_idx = next(i for i, x in enumerate(st.session_state.evenings) if x["id"] == ev["id"])
                        if st.button("invite", key=f"inv_{ev['id']}_{m['id']}", use_container_width=True):
                            if m["id"] not in st.session_state.evenings[ev_idx]["invited"]:
                                st.session_state.evenings[ev_idx]["invited"].append(m["id"])
                                st.rerun()
            else:
                html('<div class="notice-dim">// no ready members available. mark people as ready in the inside tab.</div>')
 
    html('<div class="nk-footer">built quietly · bhopal</div>')
 
 
def page_space_holders():
    section_header("space holders", "present, but never in the way.")
 
    facs = st.session_state.facilitators
 
    status_colors = {"holding": "g", "noticing": "y", "stepped away": "r"}
    style_colors = {"calm": "b", "energetic": "o"}
 
    tab1, tab2, tab3 = st.tabs(["the team", "onboard someone", "reflections"])
 
    with tab1:
        active = [f for f in facs if f["status"] != "stepped away"]
        away = [f for f in facs if f["status"] == "stepped away"]
 
        cols = st.columns(2)
        for i, f in enumerate(active):
            with cols[i % 2]:
                html(f"""
                <div class="nk-card nk-card-accent" style="margin-bottom: 10px;">
                    <div style="display: flex; align-items: flex-start; gap: 14px;">
                        <div style="width: 44px; height: 44px; border-radius: 50%; 
                                    background: rgba(255,90,0,0.08); border: 2px solid #FF5A00;
                                    display: flex; align-items: center; justify-content: center;
                                    font-family: 'Syne', sans-serif; font-weight: 800; 
                                    font-size: 16px; color: #FF5A00; flex-shrink: 0;">
                            {f['name'][0]}
                        </div>
                        <div style="flex: 1;">
                            <div style="font-family: 'Syne', sans-serif; font-weight: 700; font-size: 14px; margin-bottom: 4px;">
                                {f['name']}
                                <span class="badge badge-{status_colors.get(f['status'],'o')}" style="margin-left: 6px;">{f['status']}</span>
                                <span class="badge badge-{style_colors.get(f['style'],'o')}" style="margin-left: 4px;">{f['style']}</span>
                            </div>
                            <div style="font-family: 'Syne Mono', monospace; font-size: 10px; color: #555; line-height: 1.6;">
                                login: {f['uid']} · {f['sessions_run']} sessions run<br>
                                access: {f['access']} · {f['refs']} referral slots
                            </div>
                            <div style="font-size: 12px; color: #555; margin-top: 8px; font-style: italic;">
                                "{f['notes']}"
                            </div>
                        </div>
                    </div>
                </div>
                """)
 
        if away:
            html('<div style="font-family: \'Syne Mono\', monospace; font-size: 10px; color: #333; text-transform: uppercase; letter-spacing: 0.12em; margin: 1.5rem 0 0.75rem;">stepped away</div>')
            for f in away:
                html(f"""
                <div class="nk-card" style="opacity: 0.4; margin-bottom: 6px;">
                    <div style="font-family: 'Syne', sans-serif; font-weight: 700;">{f['name']} <span class="badge badge-r">stepped away</span></div>
                    <div style="font-family: 'Syne Mono', monospace; font-size: 10px; color: #444;">{f['uid']}</div>
                </div>
                """)
 
    with tab2:
        html('<div class="notice-dim">// every space holder starts as someone who showed up twice and made the room feel easier. observe first. ask later.</div>')
 
        with st.form("onboard_form", clear_on_submit=True):
            col1, col2 = st.columns(2)
            with col1:
                ob_name = st.text_input("name")
                ob_email = st.text_input("email")
                ob_phone = st.text_input("phone")
                ob_uid = st.text_input("login id", placeholder="name.fac")
            with col2:
                ob_style = st.selectbox("facilitation style", ["calm", "energetic"])
                ob_sessions = st.number_input("sessions attended before onboarding", 1, 20, 2)
                ob_access = st.selectbox("tier access (reward)", ["first out", "in between plans", "worth it", "yhttb"])
                ob_refs = st.number_input("referral slots", 0, 10, 2)
            ob_notes = st.text_area("what makes them good in a room?", height=80)
 
            if st.form_submit_button("bring them in →", use_container_width=True):
                if ob_name:
                    new_fac = {
                        "id": f"f{len(st.session_state.facilitators)+1}",
                        "name": ob_name, "uid": ob_uid, "style": ob_style,
                        "status": "noticing", "sessions_run": 0,
                        "access": ob_access, "refs": ob_refs,
                        "on_leave": False, "notes": ob_notes,
                    }
                    st.session_state.facilitators.append(new_fac)
                    st.success(f"// {ob_name} added as a space holder candidate.")
 
    with tab3:
        html('<div class="notice-dim">// after every evening, the space holder fills this. not a report. just what they noticed.</div>')
 
        with st.form("reflection_form", clear_on_submit=True):
            fac_names = [f["name"] for f in facs if f["status"] != "stepped away"]
            ref_fac = st.selectbox("which space holder?", fac_names)
            ref_evening = st.selectbox("which evening?", [ev["name"] for ev in st.session_state.evenings])
            ref_worked = st.text_area("what worked?", height=80, placeholder="what felt right about the evening...")
            ref_shifted = st.text_area("what shifted?", height=80, placeholder="a moment that changed the energy...")
            ref_notes = st.text_area("anything else?", height=60, placeholder="notes for next time...")
 
            if st.form_submit_button("save reflection →", use_container_width=True):
                st.session_state.reflections.append({
                    "facilitator": ref_fac, "evening": ref_evening,
                    "worked": ref_worked, "shifted": ref_shifted,
                    "notes": ref_notes, "date": str(date.today()),
                })
                st.success("// reflection saved.")
 
        if st.session_state.reflections:
            st.markdown("---")
            html('<div style="font-family: \'Syne Mono\', monospace; font-size: 10px; color: #555; text-transform: uppercase; letter-spacing: 0.12em; margin-bottom: 1rem;">past reflections</div>')
            for r in reversed(st.session_state.reflections):
                html(f"""
                <div class="nk-card nk-card-purple" style="margin-bottom: 8px;">
                    <div style="font-family: 'Syne', sans-serif; font-weight: 700; margin-bottom: 4px;">{r['facilitator']} · {r['evening']}</div>
                    <div style="font-family: 'Syne Mono', monospace; font-size: 9px; color: #444; margin-bottom: 10px;">{r['date']}</div>
                    {f'<div style="font-size: 12px; color: #777; line-height: 1.6; margin-bottom: 6px;"><span style="color: #555; font-family: Syne Mono, monospace; font-size: 9px; text-transform: uppercase;">worked //</span> {r["worked"]}</div>' if r.get('worked') else ''}
                    {f'<div style="font-size: 12px; color: #777; line-height: 1.6;"><span style="color: #555; font-family: Syne Mono, monospace; font-size: 9px; text-transform: uppercase;">shifted //</span> {r["shifted"]}</div>' if r.get('shifted') else ''}
                </div>
                """)
 
    html('<div class="nk-footer">built quietly · bhopal</div>')
 
 
def page_notes():
    section_header("notes", "words that feel right.")
 
    members = st.session_state.members
    approved = [m for m in members if m["status"] == "approved"]
 
    TEMPLATES = {
        "invite": "hey —\n\nwe're putting together a small nook evening, and we thought of you.\n\nit's just a handful of people, a shared activity, and some time to unwind.\nyou don't need to know anyone. you don't need to bring anyone.\njust yourself, and an evening free.\n\ndetails to follow if you're in.\n\n—",
        "reminder": "hey —\n\njust a quiet nudge for today's evening.\n\nwe're looking forward to it. see you there.\n\n—",
        "post-session": "hey —\n\nthank you for being part of that evening.\n\nsomething felt right about the room. we noticed.\n\nmore soon.\n\n—",
        "custom request": "",
    }
 
    col1, col2 = st.columns([1, 2])
 
    with col1:
        msg_type = st.selectbox("message type", list(TEMPLATES.keys()))
        to_options = ["everyone (approved)"] + [m["name"] for m in approved]
        to_person = st.selectbox("to", to_options)
 
    with col2:
        body = st.text_area(
            "message",
            value=TEMPLATES.get(msg_type, ""),
            height=200,
            placeholder="write something that feels right...",
        )
        if st.button("save message →", use_container_width=True):
            st.session_state.messages.append({
                "type": msg_type,
                "to": to_person,
                "body": body,
                "date": str(date.today()),
                "from": st.session_state.user_name,
            })
            st.success("// message saved.")
 
    if st.session_state.messages:
        st.markdown("---")
        html('<div style="font-family: \'Syne Mono\', monospace; font-size: 10px; color: #555; text-transform: uppercase; letter-spacing: 0.12em; margin-bottom: 1rem;">saved messages</div>')
        for msg in reversed(st.session_state.messages):
            html(f"""
            <div class="nk-card" style="margin-bottom: 8px; border-left: 2px solid rgba(255,90,0,0.3);">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                    <div style="font-family: 'Syne', sans-serif; font-weight: 700; font-size: 13px;">{msg['type']}</div>
                    <div style="font-family: 'Syne Mono', monospace; font-size: 9px; color: #444;">to: {msg['to']} · {msg['date']}</div>
                </div>
                <div style="font-size: 12px; color: #666; line-height: 1.7; white-space: pre-line; font-family: 'DM Sans', sans-serif;">{msg['body'][:200]}{'...' if len(msg['body']) > 200 else ''}</div>
            </div>
            """)
 
    html('<div class="nk-footer">built quietly · bhopal</div>')
 
 
def page_contributions():
    section_header("contributions", "what keeps nook moving.")
 
    payments = st.session_state.payments
    evenings = st.session_state.evenings
    members = st.session_state.members
    nl_subs = len([m for m in members if m.get("newsletter") == "yes" and m["status"] == "approved"])
 
    paid = [p for p in payments if p["status"] == "paid"]
    pending = [p for p in payments if p["status"] == "pending"]
    total = sum(p["amount"] for p in paid)
    nl_rev = nl_subs * 99
 
    cols = st.columns(4)
    with cols[0]:
        html(f'<div class="stat-box" style="--accent:#22c55e;"><div class="stat-n" style="color:#22c55e;">₹{total:,}</div><div class="stat-l">collected</div></div>')
    with cols[1]:
        html(f'<div class="stat-box" style="--accent:#fbbf24;"><div class="stat-n" style="color:#fbbf24;">{len(pending)}</div><div class="stat-l">pending</div></div>')
    with cols[2]:
        html(f'<div class="stat-box" style="--accent:#38bdf8;"><div class="stat-n" style="color:#38bdf8;">₹{nl_rev:,}</div><div class="stat-l">newsletter MRR</div></div>')
    with cols[3]:
        html(f'<div class="stat-box" style="--accent:#FF5A00;"><div class="stat-n" style="color:#FF5A00;">{nl_subs}</div><div class="stat-l">nl subscribers</div></div>')
 
    st.markdown("<br>", unsafe_allow_html=True)
 
    # by evening
    html('<div style="font-family: Bebas Neue, Syne, sans-serif; font-size: 16px; letter-spacing: 1px; color: #F4F2ED; margin-bottom: 1rem; display: flex; align-items: center; gap: 10px;">by evening <div style="flex: 1; height: 1px; background: rgba(255,255,255,0.05);"></div></div>')
 
    for ev in evenings:
        ev_pays = [p for p in payments if p["evening"] == ev["name"]]
        ev_total = sum(p["amount"] for p in ev_pays if p["status"] == "paid")
        html(f"""
        <div class="nk-card" style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 8px; padding: 1rem 1.25rem;">
            <div>
                <div style="font-family: 'Syne', sans-serif; font-weight: 700; font-size: 13px;">{ev['name']}</div>
                <div style="font-family: 'Syne Mono', monospace; font-size: 10px; color: #444;">{len(ev_pays)} payments</div>
            </div>
            <div style="font-family: 'Syne', sans-serif; font-weight: 800; font-size: 22px; color: #22c55e;">₹{ev_total:,}</div>
        </div>
        """)
 
    st.markdown("---")
 
    html('<div style="font-family: Bebas Neue, Syne, sans-serif; font-size: 16px; letter-spacing: 1px; color: #F4F2ED; margin-bottom: 1rem; display: flex; align-items: center; gap: 10px;">all records <div style="flex: 1; height: 1px; background: rgba(255,255,255,0.05);"></div></div>')
 
    for p in payments:
        col1, col2, col3, col4, col5 = st.columns([2, 2, 1, 1, 1])
        with col1:
            html(f'<div style="font-family: Syne, sans-serif; font-weight: 700; font-size: 13px; padding: 0.5rem 0;">{p["member"]}</div>')
        with col2:
            html(f'<div style="font-size: 12px; color: #555; padding: 0.5rem 0;">{p["evening"]}</div>')
        with col3:
            html(f'<div style="font-family: Syne Mono, monospace; color: #FF5A00; font-size: 13px; padding: 0.5rem 0;">₹{p["amount"]}</div>')
        with col4:
            status_color = "g" if p["status"] == "paid" else "y"
            html(f'<div style="padding: 0.5rem 0;">{badge(p["status"], status_color)}</div>')
        with col5:
            if p["status"] == "pending":
                p_idx = next(i for i, x in enumerate(st.session_state.payments) if x["id"] == p["id"])
                if st.button("mark paid", key=f"pay_{p['id']}", use_container_width=True):
                    st.session_state.payments[p_idx]["status"] = "paid"
                    st.rerun()
 
    st.markdown("<br>")
    with st.expander("add a payment"):
        with st.form("add_pay", clear_on_submit=True):
            col1, col2, col3 = st.columns(3)
            with col1:
                pay_member = st.text_input("member name")
            with col2:
                pay_evening = st.selectbox("evening", [ev["name"] for ev in evenings])
            with col3:
                pay_amount = st.number_input("amount (₹)", min_value=0, value=499)
            pay_method = st.selectbox("method", ["razorpay", "upi", "cash", "manual"])
            if st.form_submit_button("add →"):
                st.session_state.payments.append({
                    "id": f"p{len(payments)+1}", "member": pay_member, "evening": pay_evening,
                    "amount": pay_amount, "method": pay_method, "status": "pending",
                    "date": str(date.today()),
                })
                st.rerun()
 
    html('<div class="nk-footer">built quietly · bhopal</div>')
 
 
def page_insights():
    section_header("insights", "what the numbers quietly say.")
 
    members = st.session_state.members
    payments = st.session_state.payments
    evenings = st.session_state.evenings
 
    approved = [m for m in members if m["status"] == "approved"]
    total_sessions_run = sum(ev.get("capacity", 0) for ev in evenings)
 
    # show rate
    confirmed_total = sum(len(ev.get("confirmed", [])) for ev in evenings)
    invited_total = sum(len(ev.get("invited", [])) for ev in evenings)
    show_rate = int(confirmed_total / max(invited_total, 1) * 100)
 
    repeat_users = [m for m in approved if m["sessions"] >= 2]
    nl_subs = [m for m in members if m.get("newsletter") == "yes"]
 
    cols = st.columns(5)
    metrics = [
        ("show rate", f"{show_rate}%", "#FF5A00"),
        ("repeat visitors", len(repeat_users), "#22c55e"),
        ("newsletter subs", len(nl_subs), "#38bdf8"),
        ("evenings run", len(evenings), "#a78bfa"),
        ("avg comfort", f"{sum(m['comfort_level'] for m in approved) / max(len(approved), 1):.1f}/5", "#fbbf24"),
    ]
    for i, (label, val, color) in enumerate(metrics):
        with cols[i]:
            html(f'<div class="stat-box" style="--accent:{color};"><div class="stat-n" style="color:{color};font-size:32px;">{val}</div><div class="stat-l">{label}</div></div>')
 
    st.markdown("<br>", unsafe_allow_html=True)
 
    col1, col2 = st.columns(2)
 
    with col1:
        html('<div style="font-family: Bebas Neue, Syne, sans-serif; font-size: 16px; letter-spacing: 1px; color: #F4F2ED; margin-bottom: 1rem; display: flex; align-items: center; gap: 10px;">presence tag distribution <div style="flex: 1; height: 1px; background: rgba(255,255,255,0.05);"></div></div>')
        all_tags = [m["presence_tag"] for m in approved]
        tag_data = pd.DataFrame({
            "tag": PRESENCE_TAGS,
            "count": [all_tags.count(t) for t in PRESENCE_TAGS],
        })
        st.bar_chart(tag_data.set_index("tag"), color="#FF5A00", height=250)
 
    with col2:
        html('<div style="font-family: Bebas Neue, Syne, sans-serif; font-size: 16px; letter-spacing: 1px; color: #F4F2ED; margin-bottom: 1rem; display: flex; align-items: center; gap: 10px;">session attendance <div style="flex: 1; height: 1px; background: rgba(255,255,255,0.05);"></div></div>')
        session_counts = [0, 1, 2, 3, 4, 5, 6]
        session_data = pd.DataFrame({
            "sessions": [str(s) for s in session_counts],
            "people": [len([m for m in approved if m["sessions"] == s]) for s in session_counts],
        })
        st.bar_chart(session_data.set_index("sessions"), color="#FF5A00", height=250)
 
    st.markdown("<br>", unsafe_allow_html=True)
 
    html('<div style="font-family: Bebas Neue, Syne, sans-serif; font-size: 16px; letter-spacing: 1px; color: #F4F2ED; margin-bottom: 1rem; display: flex; align-items: center; gap: 10px;">tier breakdown <div style="flex: 1; height: 1px; background: rgba(255,255,255,0.05);"></div></div>')
 
    fo = len([m for m in approved if m["tier"] == "first out"])
    ibp = len([m for m in approved if m["tier"] == "in between plans"])
    wi = len([m for m in approved if m["tier"] == "worth it"])
 
    col1, col2, col3 = st.columns(3)
    with col1:
        html(f"""
        <div class="nk-card nk-card-accent">
            <div style="font-family: 'Syne Mono', monospace; font-size: 9px; color: #FF5A00; text-transform: uppercase; letter-spacing: 0.12em; margin-bottom: 8px;">first out</div>
            <div style="font-family: 'Syne', sans-serif; font-weight: 800; font-size: 36px; color: #FF5A00;">{fo}</div>
            <div style="font-size: 12px; color: #444; margin-top: 4px;">{int(fo/max(len(approved),1)*100)}% of people inside</div>
        </div>
        """)
    with col2:
        html(f"""
        <div class="nk-card nk-card-purple">
            <div style="font-family: 'Syne Mono', monospace; font-size: 9px; color: #a78bfa; text-transform: uppercase; letter-spacing: 0.12em; margin-bottom: 8px;">in between plans</div>
            <div style="font-family: 'Syne', sans-serif; font-weight: 800; font-size: 36px; color: #a78bfa;">{ibp}</div>
            <div style="font-size: 12px; color: #444; margin-top: 4px;">{int(ibp/max(len(approved),1)*100)}% of people inside</div>
        </div>
        """)
    with col3:
        html(f"""
        <div class="nk-card nk-card-green">
            <div style="font-family: 'Syne Mono', monospace; font-size: 9px; color: #22c55e; text-transform: uppercase; letter-spacing: 0.12em; margin-bottom: 8px;">worth it +</div>
            <div style="font-family: 'Syne', sans-serif; font-weight: 800; font-size: 36px; color: #22c55e;">{wi}</div>
            <div style="font-size: 12px; color: #444; margin-top: 4px;">{int(wi/max(len(approved),1)*100)}% of people inside</div>
        </div>
        """)
 
    html('<div class="nk-footer">built quietly · bhopal</div>')
 
 
# ─────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────
def main():
    init_state()
 
    if not st.session_state.logged_in:
        render_login()
        return
 
    page = render_sidebar()
 
    page_map = {
        "control room": page_control_room,
        "incoming": page_incoming,
        "inside": page_inside,
        "experience builder": page_experience_builder,
        "evenings": page_evenings,
        "space holders": page_space_holders,
        "notes": page_notes,
        "contributions": page_contributions,
        "insights": page_insights,
    }
 
    fn = page_map.get(page, page_control_room)
    fn()
 
 
if __name__ == "__main__":
    main()
 
