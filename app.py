# nook control room
# run: streamlit run nook_app.py

import streamlit as st
from datetime import date
import random

st.set_page_config(page_title="nook control room", layout="wide")

# -------------------- STYLE --------------------

st.markdown("""
<style>

/* ---------- ROOT ---------- */
:root {
    --orange: #E44F0A;
    --yellow: #F0A533;
    --red: #BA011A;
    --blue: #0B4B8B;
    --cream: #FCF5AF;
    --bg: #0E0E0E;
    --card: #141414;
    --text: #F4F2ED;
}

/* ---------- BASE ---------- */
html, body, [data-testid="stApp"] {
    background: radial-gradient(circle at top, rgba(228,79,10,0.08), #0E0E0E 60%);
    color: var(--text);
    font-family: system-ui;
}

/* REMOVE DEFAULT */
#MainMenu, header, footer {visibility: hidden;}
.block-container {padding: 2rem; max-width: 1300px;}

/* ---------- CARD ---------- */
.nk-card {
    background: linear-gradient(135deg, #141414, #0E0E0E);
    border: 1px solid rgba(255,255,255,0.06);
    border-radius: 16px;
    padding: 1.5rem;
    margin-bottom: 12px;
    position: relative;
}

.nk-card::after {
    content: '';
    position: absolute;
    inset: 0;
    background: radial-gradient(circle at top left, rgba(228,79,10,0.15), transparent 40%);
}

/* ---------- TEXT ---------- */
.title {
    font-size: 26px;
    font-weight: 700;
}

.sub {
    font-size: 12px;
    color: #777;
}

/* ---------- BUTTON ---------- */
.stButton button {
    background: linear-gradient(135deg, #E44F0A, #BA011A);
    border-radius: 10px;
    border: none;
    color: white;
    font-weight: 600;
}

.stButton button:hover {
    transform: scale(1.03);
    box-shadow: 0 0 15px rgba(228,79,10,0.4);
}

/* ---------- TAG ---------- */
.tag {
    padding: 4px 10px;
    border-radius: 20px;
    font-size: 10px;
    background: rgba(255,255,255,0.05);
}

/* ---------- STAT ---------- */
.stat {
    font-size: 28px;
    font-weight: 700;
}
.stat-label {
    font-size: 10px;
    color: #777;
}

</style>
""", unsafe_allow_html=True)

# -------------------- DATA --------------------

if "members" not in st.session_state:
    st.session_state.members = [
        {"name": "Ishita", "tag": "quiet energy", "sessions": 2},
        {"name": "Kabir", "tag": "expressive", "sessions": 4},
        {"name": "Dev", "tag": "open to new", "sessions": 1},
    ]

if "evenings" not in st.session_state:
    st.session_state.evenings = [
        {"name": "canvas night", "vibe": "mixed"},
        {"name": "lake walk", "vibe": "introvert"}
    ]

if "reflections" not in st.session_state:
    st.session_state.reflections = []

# -------------------- HELPERS --------------------

def section(title, sub):
    st.markdown(f"<div class='title'>{title}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='sub'>{sub}</div><br>", unsafe_allow_html=True)

def card(html):
    st.markdown(f"<div class='nk-card'>{html}</div>", unsafe_allow_html=True)

def match_label(score):
    if score > 80: return "high alignment"
    if score > 60: return "good fit"
    if score > 40: return "possible"
    return "low match"

# -------------------- PAGES --------------------

def control_room():
    section("control room", "system overview")

    card("""
    <div style='font-size:20px;font-weight:700'>
        signal: quiet energy dominant
    </div>
    <div style='font-size:13px;color:#aaa'>
        recommendation: slower, low-pressure evenings
    </div>
    """)

    cols = st.columns(3)
    stats = [
        ("people", len(st.session_state.members)),
        ("evenings", len(st.session_state.evenings)),
        ("reflections", len(st.session_state.reflections))
    ]

    for i, (label, val) in enumerate(stats):
        with cols[i]:
            st.markdown(f"<div class='stat'>{val}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='stat-label'>{label}</div>", unsafe_allow_html=True)

def inside():
    section("inside", "active members")

    grouped = {}

    for m in st.session_state.members:
        grouped.setdefault(m["tag"], []).append(m)

    for tag, people in grouped.items():
        st.markdown(f"### {tag}")
        for m in people:
            card(f"""
            <b>{m['name']}</b><br>
            sessions: {m['sessions']}
            """)

def evenings():
    section("evenings", "experience design")

    for ev in st.session_state.evenings:
        card(f"""
        <div style='font-size:18px;font-weight:700'>{ev['name']}</div>
        <div style='color:#aaa'>vibe: {ev['vibe']}</div>
        """)

    st.markdown("---")

    st.subheader("create new evening")

    name = st.text_input("name")
    vibe = st.selectbox("vibe", ["introvert", "social", "mixed"])

    if st.button("add evening"):
        st.session_state.evenings.append({"name": name, "vibe": vibe})
        st.rerun()

def reflections():
    section("reflections", "what stayed after")

    with st.form("reflection"):
        member = st.selectbox("member", [m["name"] for m in st.session_state.members])
        evening = st.selectbox("evening", [e["name"] for e in st.session_state.evenings])
        feeling = st.selectbox("feeling", [
            "felt seen",
            "warm",
            "awkward",
            "surface",
            "deep"
        ])
        note = st.text_area("note")

        if st.form_submit_button("save"):
            st.session_state.reflections.append({
                "member": member,
                "evening": evening,
                "feeling": feeling,
                "note": note,
                "date": str(date.today())
            })
            st.success("saved")
            st.rerun()

    for r in st.session_state.reflections[::-1]:
        card(f"""
        <b>{r['member']}</b> · {r['evening']}<br>
        {r['feeling']}<br>
        <span style='color:#888'>{r['note']}</span>
        """)

def insights():
    section("insights", "system intelligence")

    if not st.session_state.reflections:
        card("no data yet")
        return

    expressive = sum(1 for m in st.session_state.members if m["tag"] == "expressive")

    card(f"""
    expressive users: {expressive}<br>
    total reflections: {len(st.session_state.reflections)}<br>
    pattern: smaller groups → better feedback
    """)

# -------------------- NAV --------------------

page = st.sidebar.radio("", [
    "control room",
    "inside",
    "evenings",
    "reflections",
    "insights"
])

if page == "control room":
    control_room()
elif page == "inside":
    inside()
elif page == "evenings":
    evenings()
elif page == "reflections":
    reflections()
elif page == "insights":
    insights()
