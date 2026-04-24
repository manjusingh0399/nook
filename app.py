# nook control room
# run: streamlit run app.py

import streamlit as st
from datetime import date

st.set_page_config(page_title="nook control room", layout="wide")

# -------------------- STYLES --------------------

st.markdown("""
<style>

/* ---------- ROOT ---------- */
:root {
    --orange: #E44F0A;
    --yellow: #F0A533;
    --red: #BA011A;
    --blue: #0B4B8B;
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

/* ---------- SIDEBAR ---------- */
[data-testid="stSidebar"] {
    background: #0A0A0A;
    border-right: 1px solid rgba(255,255,255,0.05);
}

[data-testid="stSidebar"] * {
    color: #aaa;
}

[data-testid="stRadio"] label {
    font-size: 13px !important;
    padding: 8px 10px !important;
    border-radius: 8px !important;
    transition: all 0.2s;
}

[data-testid="stRadio"] label:hover {
    background: rgba(255,255,255,0.05);
    color: white !important;
}

[data-testid="stRadio"] input:checked + div {
    background: rgba(228,79,10,0.15) !important;
    color: #E44F0A !important;
    border: 1px solid rgba(228,79,10,0.3);
}

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

# -------------------- STATE --------------------

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

def card(content):
    st.markdown(f"<div class='nk-card'>{content}</div>", unsafe_allow_html=True)

# -------------------- SIDEBAR --------------------

with st.sidebar:
    st.markdown("""
    <div style="font-size:22px;font-weight:700;">nook</div>
    <div style="font-size:10px;color:#777;margin-bottom:20px;">
        control system
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="font-size:10px;color:#E44F0A;margin-bottom:10px;">
        founder mode
    </div>
    """, unsafe_allow_html=True)

    page = st.radio(
        "",
        ["control room", "inside", "evenings", "reflections", "insights"],
        label_visibility="collapsed"
    )

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
            card(f"<b>{m['name']}</b><br>sessions: {m['sessions']}")

def evenings():
    section("evenings", "experience design")

    for ev in st.session_state.evenings:
        card(f"""
        <div style='font-size:18px;font-weight:700'>{ev['name']}</div>
        <div style='color:#aaa'>vibe: {ev['vibe']}</div>
        """)

    st.markdown("---")

    st.subheader("create new")

    name = st.text_input("name")
    vibe = st.selectbox("vibe", ["introvert", "social", "mixed"])

    if st.button("add"):
        st.session_state.evenings.append({"name": name, "vibe": vibe})
        st.rerun()

def reflections():
    section("reflections", "what stayed after")

    with st.form("form"):
        member = st.selectbox("member", [m["name"] for m in st.session_state.members])
        evening = st.selectbox("evening", [e["name"] for e in st.session_state.evenings])
        feeling = st.selectbox("feeling", ["seen", "warm", "awkward", "surface", "deep"])
        note = st.text_area("note")

        if st.form_submit_button("save"):
            st.session_state.reflections.append({
                "member": member,
                "evening": evening,
                "feeling": feeling,
                "note": note,
                "date": str(date.today())
            })
            st.rerun()

    for r in st.session_state.reflections[::-1]:
        card(f"""
        <b>{r['member']}</b> · {r['evening']}<br>
        {r['feeling']}<br>
        <span style='color:#888'>{r['note']}</span>
        """)

def insights():
    section("insights", "system learning")

    if not st.session_state.reflections:
        card("no data yet")
        return

    card(f"""
    total reflections: {len(st.session_state.reflections)}<br>
    insight: smaller groups → better engagement
    """)

# -------------------- ROUTING --------------------

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
