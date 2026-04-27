import json
from datetime import date, datetime
from pathlib import Path

import pandas as pd
import streamlit as st


st.set_page_config(
    page_title="nook control room",
    page_icon="N",
    layout="wide",
    initial_sidebar_state="expanded",
)


PALETTE = {
    "cream": "#F2F0E4",
    "paper": "#FFFAF0",
    "soft": "#F7EDDC",
    "gold": "#FFAC00",
    "orange": "#F28705",
    "deep_orange": "#F25C05",
    "red_orange": "#F24405",
    "black": "#000000",
    "muted": "#5E5146",
}


FOUNDER = {"uid": "manju", "pass": "founder2026", "role": "founder", "name": "Manju Singh"}
FACILITATOR_LOGINS = [
    ("riya.fac", "riya123", "Riya Kapoor", "calm", "holding", "worth it", 5, 3),
    ("aryan.fac", "aryan123", "Aryan Mehta", "energetic", "holding", "in between plans", 4, 3),
    ("sneha.fac", "sneha123", "Sneha Ali", "calm", "noticing", "worth it", 7, 4),
    ("rohan.fac", "rohan123", "Rohan Jain", "energetic", "holding", "first out", 3, 2),
    ("priya.fac", "priya123", "Priya Nair", "calm", "stepped away", "in between plans", 2, 3),
    ("dev.fac", "dev123", "Dev Sharma", "energetic", "holding", "you had to be there", 9, 5),
    ("tanya.fac", "tanya123", "Tanya Bose", "calm", "noticing", "worth it", 6, 4),
]

TIER_RANK = {
    "first out": 1,
    "in between plans": 2,
    "worth it": 3,
    "you had to be there": 4,
}

DATA_PATH = Path(__file__).with_name("nook_data.json")


def inject_css():
    st.markdown(
        f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;500;600;700;800&family=Syne+Mono&display=swap');

        :root {{
            --cream: {PALETTE["cream"]};
            --paper: {PALETTE["paper"]};
            --soft: {PALETTE["soft"]};
            --gold: {PALETTE["gold"]};
            --orange: {PALETTE["orange"]};
            --deep-orange: {PALETTE["deep_orange"]};
            --red-orange: {PALETTE["red_orange"]};
            --black: {PALETTE["black"]};
            --muted: {PALETTE["muted"]};
        }}

        html, body, [data-testid="stAppViewContainer"] {{
            background: linear-gradient(180deg, #f7f3e7 0%, var(--cream) 420px) !important;
            color: var(--black);
            font-family: Syne, system-ui, sans-serif;
        }}

        [data-testid="stSidebar"] {{
            background: var(--paper);
            border-right: 2px solid var(--black);
        }}

        [data-testid="stSidebar"] * {{
            font-family: Syne, system-ui, sans-serif;
        }}

        h1, h2, h3 {{
            font-family: Syne, system-ui, sans-serif !important;
            font-weight: 800 !important;
            letter-spacing: 0 !important;
            color: var(--black);
        }}

        .block-container {{
            padding-top: 1.4rem;
            max-width: 1280px;
        }}

        .nook-title {{
            background: var(--paper);
            border: 2px solid var(--black);
            border-left: 14px solid var(--black);
            border-radius: 28px;
            padding: 1.2rem 1.35rem;
            margin-bottom: 1rem;
        }}

        .nook-title p {{
            margin: 0;
            color: var(--muted);
            font-family: "Syne Mono", monospace;
            font-size: 0.68rem;
            letter-spacing: 0.12em;
            text-transform: uppercase;
        }}

        .nook-title h1 {{
            margin: 0.15rem 0 0;
            font-size: clamp(2.4rem, 5vw, 4.7rem);
            line-height: 0.9;
            text-transform: lowercase;
        }}

        .metric-grid {{
            display: grid;
            grid-template-columns: repeat(6, minmax(0, 1fr));
            gap: 0.85rem;
            margin-bottom: 1rem;
        }}

        .metric-card {{
            min-height: 126px;
            border: 1px solid rgba(0,0,0,0.18);
            border-radius: 24px;
            background: var(--paper);
            padding: 1rem;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }}

        .metric-card.feature {{
            grid-column: span 2;
            background: var(--orange);
            border: 2px solid var(--black);
        }}

        .metric-card.dark {{
            background: var(--black);
            color: var(--cream);
        }}

        .metric-card.gold {{ background: var(--gold); }}
        .metric-card.deep {{ background: var(--deep-orange); }}

        .metric-label {{
            color: rgba(0,0,0,0.58);
            font-family: "Syne Mono", monospace;
            font-size: 0.66rem;
            letter-spacing: 0.12em;
            text-transform: uppercase;
        }}

        .metric-card.dark .metric-label {{
            color: rgba(242,240,228,0.54);
        }}

        .metric-value {{
            font-size: clamp(2rem, 4vw, 3.4rem);
            font-weight: 800;
            line-height: 0.9;
            word-break: break-word;
        }}

        .panel {{
            background: var(--paper);
            border: 1px solid rgba(0,0,0,0.14);
            border-radius: 24px;
            padding: 1.1rem;
            margin-bottom: 1rem;
        }}

        .panel.black-accent {{
            border-left: 10px solid var(--black);
        }}

        .panel h3 {{
            margin: 0 0 0.8rem;
            font-size: 1.35rem;
            line-height: 1;
            text-transform: lowercase;
        }}

        .badge {{
            display: inline-block;
            border: 1px solid var(--black);
            border-radius: 999px;
            padding: 0.22rem 0.55rem;
            margin: 0.12rem 0.15rem 0.12rem 0;
            background: var(--soft);
            color: var(--black);
            font-family: "Syne Mono", monospace;
            font-size: 0.68rem;
            white-space: nowrap;
        }}

        .badge.orange {{ background: var(--orange); }}
        .badge.gold {{ background: var(--gold); }}
        .badge.black {{ background: var(--black); color: var(--cream); }}

        .list-row {{
            border-radius: 18px;
            padding: 0.75rem 0.85rem;
            background: rgba(255,255,255,0.38);
            border: 1px solid rgba(0,0,0,0.08);
            margin-bottom: 0.45rem;
        }}

        .list-row strong {{
            display: block;
            font-weight: 800;
        }}

        .list-row span {{
            color: var(--muted);
            font-size: 0.86rem;
        }}

        div[data-testid="stDataFrame"] {{
            border: 1px solid rgba(0,0,0,0.14);
            border-radius: 18px;
            overflow: hidden;
        }}

        .stButton button, .stDownloadButton button {{
            border: 2px solid var(--black);
            border-radius: 999px;
            background: var(--orange);
            color: var(--black);
            font-weight: 800;
        }}

        .stButton button:hover, .stDownloadButton button:hover {{
            border-color: var(--black);
            background: var(--gold);
            color: var(--black);
        }}

        .stTextInput input, .stTextArea textarea, .stSelectbox div[data-baseweb="select"] > div,
        .stNumberInput input, .stDateInput input, .stTimeInput input {{
            border-radius: 16px !important;
            border-color: rgba(0,0,0,0.18) !important;
            background: #fffdf5 !important;
        }}

        html, body, [data-testid="stAppViewContainer"] {{
            background:
                radial-gradient(circle at 84% 8%, rgba(255,172,0,0.24), transparent 18rem),
                radial-gradient(circle at 14% 14%, rgba(242,92,5,0.12), transparent 20rem),
                linear-gradient(180deg, #fff8e7 0%, var(--cream) 540px) !important;
        }}

        .block-container {{
            padding-top: 1rem;
            padding-bottom: 3rem;
        }}

        .nook-title {{
            position: relative;
            overflow: hidden;
            border-radius: 34px;
            border: 2px solid var(--black);
            border-left: 0;
            background:
                linear-gradient(90deg, var(--black) 0 16px, transparent 16px),
                linear-gradient(135deg, #fffaf0 0%, #fff4d8 52%, #ffe1b5 100%);
            box-shadow: 0 12px 0 rgba(0,0,0,0.07);
            min-height: 142px;
        }}

        .nook-title::after {{
            content: "";
            position: absolute;
            right: -58px;
            top: -62px;
            width: 210px;
            height: 210px;
            border: 28px solid rgba(242,92,5,0.24);
            border-radius: 50%;
        }}

        .title-row {{
            position: relative;
            z-index: 1;
            display: flex;
            justify-content: space-between;
            align-items: flex-end;
            gap: 1rem;
        }}

        .title-chips {{
            display: flex;
            gap: 0.45rem;
            flex-wrap: wrap;
            justify-content: flex-end;
            min-width: 180px;
        }}

        .title-chip {{
            display: inline-block;
            width: 44px;
            height: 18px;
            border: 2px solid var(--black);
            border-radius: 999px;
        }}

        .title-chip.gold {{ background: var(--gold); }}
        .title-chip.orange {{ background: var(--orange); }}
        .title-chip.deep {{ background: var(--deep-orange); }}
        .title-chip.black {{ background: var(--black); }}

        .metric-grid {{
            gap: 1rem;
        }}

        .metric-card {{
            position: relative;
            overflow: hidden;
            border: 2px solid rgba(0,0,0,0.16);
            border-radius: 30px;
            box-shadow: 0 8px 0 rgba(0,0,0,0.05);
        }}

        .metric-card::after {{
            content: "";
            position: absolute;
            right: -18px;
            bottom: -22px;
            width: 74px;
            height: 74px;
            border: 14px solid rgba(0,0,0,0.08);
            border-radius: 50%;
        }}

        .metric-card.feature {{
            border-color: var(--black);
            box-shadow: 8px 8px 0 rgba(0,0,0,0.12);
        }}

        .metric-card.deep .metric-label,
        .metric-card.deep .metric-value {{
            color: var(--cream);
        }}

        .metric-card.dark {{
            box-shadow: 8px 8px 0 rgba(242,135,5,0.28);
        }}

        .panel {{
            border-radius: 30px;
            border: 1px solid rgba(0,0,0,0.12);
            box-shadow: 0 10px 28px rgba(0,0,0,0.045);
        }}

        .panel.black-accent {{
            border-left: 12px solid var(--black);
        }}

        .fun-strip {{
            display: grid;
            grid-template-columns: repeat(4, minmax(0, 1fr));
            gap: 0.75rem;
            margin-bottom: 1rem;
        }}

        .fun-card {{
            min-height: 94px;
            border: 2px solid var(--black);
            border-radius: 26px;
            padding: 0.9rem;
            background: var(--paper);
            position: relative;
            overflow: hidden;
        }}

        .fun-card strong {{
            display: block;
            font-size: 1.02rem;
            line-height: 1;
        }}

        .fun-card span {{
            color: var(--muted);
            font-size: 0.84rem;
        }}

        .fun-card.orange {{ background: var(--orange); }}
        .fun-card.gold {{ background: var(--gold); }}
        .fun-card.soft {{ background: var(--soft); }}
        .fun-card.black {{ background: var(--black); color: var(--cream); }}
        .fun-card.black span {{ color: rgba(242,240,228,0.68); }}

        .list-row {{
            border-radius: 22px;
            background: #fff8e7;
            transition: transform 120ms ease, background 120ms ease, border-color 120ms ease;
        }}

        .list-row:hover {{
            transform: translateY(-1px);
            background: #ffefc9;
            border-color: rgba(0,0,0,0.2);
        }}

        .badge {{
            border-width: 1.5px;
            padding: 0.28rem 0.62rem;
        }}

        [data-testid="stSidebar"] {{
            background:
                linear-gradient(180deg, #fffaf0 0%, #fff3d6 100%);
            border-right: 2px solid var(--black);
        }}

        .sidebar-brand {{
            border: 2px solid var(--black);
            border-radius: 28px;
            padding: 1rem;
            background: var(--orange);
            box-shadow: 6px 6px 0 rgba(0,0,0,0.12);
            margin-bottom: 0.8rem;
        }}

        .sidebar-brand h2 {{
            margin: 0;
            line-height: 0.9;
            font-size: 2rem;
        }}

        .sidebar-brand p {{
            margin: 0.25rem 0 0;
            font-family: "Syne Mono", monospace;
            font-size: 0.68rem;
            letter-spacing: 0.1em;
            text-transform: uppercase;
        }}

        .sidebar-account {{
            border: 1px solid rgba(0,0,0,0.14);
            border-radius: 22px;
            padding: 0.85rem;
            background: var(--paper);
            margin-top: 1rem;
        }}

        div[role="radiogroup"] label {{
            border-radius: 999px;
            padding: 0.2rem 0.5rem;
            margin-bottom: 0.15rem;
        }}

        div[role="radiogroup"] label:hover {{
            background: rgba(242,135,5,0.16);
        }}

        [data-testid="stVerticalBlockBorderWrapper"] {{
            border-radius: 30px !important;
            border-color: rgba(0,0,0,0.15) !important;
            background: rgba(255,250,240,0.58);
            box-shadow: 0 10px 28px rgba(0,0,0,0.045);
        }}

        .login-card {{
            position: relative;
            overflow: hidden;
            border: 2px solid var(--black);
            border-radius: 34px;
            padding: 1.4rem;
            background: linear-gradient(145deg, #fffaf0 0%, #ffe7bd 100%);
            box-shadow: 10px 10px 0 rgba(0,0,0,0.12);
            margin-bottom: 1rem;
        }}

        .login-card::after {{
            content: "";
            position: absolute;
            right: -42px;
            top: -42px;
            width: 150px;
            height: 150px;
            background: var(--orange);
            border: 2px solid var(--black);
            border-radius: 50%;
        }}

        .login-card > * {{
            position: relative;
            z-index: 1;
        }}

        .login-logo {{
            display: inline-grid;
            place-items: center;
            width: 78px;
            height: 78px;
            border: 2px solid var(--black);
            border-radius: 50%;
            background: var(--black);
            color: var(--cream);
            font-weight: 800;
        }}

        .experience-note {{
            display: grid;
            grid-template-columns: repeat(3, minmax(0, 1fr));
            gap: 0.75rem;
            margin: 0.75rem 0;
        }}

        .act-note {{
            border-radius: 20px;
            padding: 0.85rem;
            background: var(--soft);
            border: 1px solid rgba(0,0,0,0.12);
            min-height: 110px;
        }}

        .act-note strong {{
            display: block;
            margin-bottom: 0.3rem;
        }}

        @media (max-width: 980px) {{
            .metric-grid {{
                grid-template-columns: repeat(2, minmax(0, 1fr));
            }}
            .metric-card.feature {{
                grid-column: span 2;
            }}
            .fun-strip, .experience-note {{
                grid-template-columns: 1fr 1fr;
            }}
        }}

        @media (max-width: 620px) {{
            .metric-grid {{
                grid-template-columns: 1fr;
            }}
            .metric-card.feature {{
                grid-column: auto;
            }}
            .fun-strip, .experience-note {{
                grid-template-columns: 1fr;
            }}
            .title-row {{
                display: block;
            }}
            .title-chips {{
                justify-content: flex-start;
                margin-top: 0.85rem;
            }}
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )


def seed_members():
    names = [
        "Kabir Anand", "Ishita Rao", "Meera Sethi", "Aarav Khan", "Naina Verma", "Aditya Sen",
        "Zoya Mirza", "Vivaan Batra", "Tara Joshi", "Rehan Malik", "Anvi Gupta", "Neil Thomas",
        "Diya Kapoor", "Yash Bhandari", "Sana Qureshi", "Om Patil", "Mira Dutta", "Arjun Menon",
        "Kiara Shah", "Sahil Sinha", "Pihu Saxena", "Rhea Paul", "Kunal Rao", "Aisha Khan",
    ]
    tags = ["quiet energy", "open to new", "observing", "expressive", "needs easing"]
    statuses = ["approved", "pending", "approved", "waitlist", "approved", "pending", "approved", "declined"]
    members = []
    for i, name in enumerate(names):
        sessions = i % 7
        phone = f"98765012{30 + i:02d}"
        members.append(
            {
                "id": f"m{i + 1}",
                "name": name,
                "email": f"{name.split()[0].lower()}@gmail.com",
                "phone": phone,
                "budget": "rs 400-rs 600" if i % 3 == 0 else "rs 700-rs 1500",
                "availability": "weekday evenings" if i % 2 else "weekend evenings",
                "activities": "board games, chai walks" if i % 2 else "painting, music, slow dinners",
                "intent": "moved here recently and want a softer way to meet people"
                if i % 4 == 0
                else "looking for intentional evenings with new people",
                "newsletter": "yes" if i % 3 == 0 else "no",
                "sessions": sessions,
                "tier": "in between plans" if sessions >= 4 else "first out",
                "presence_tag": tags[i % len(tags)],
                "comfort_level": (i % 5) + 1,
                "referral_code": referral_code(name, phone),
                "referrals_used": 1 if i % 4 == 0 else 0,
                "joined": f"2026-04-{1 + (i % 24):02d}",
                "status": statuses[i % len(statuses)],
                "ready_for_invite": i % 2 == 0,
                "notes": "",
                "fac_flag": i == 8,
            }
        )
    return members


def seed_data():
    facilitators = [
        {
            "id": f"f{i + 1}",
            "uid": uid,
            "pass": password,
            "name": name,
            "style": style,
            "status": status,
            "access": access,
            "sessions_run": sessions,
            "refs": refs,
            "notes": "natural at reading the room",
        }
        for i, (uid, password, name, style, status, access, sessions, refs) in enumerate(FACILITATOR_LOGINS)
    ]
    return {
        "members": seed_members(),
        "facilitators": facilitators,
        "experiences": [
            {
                "id": "e1",
                "name": "canvas night - mp nagar",
                "tier": "first out",
                "date": "2026-05-03",
                "time": "18:00",
                "venue": "bhopal bytes cafe",
                "capacity": 8,
                "price": 499,
                "vibe": "mixed",
                "act1": "homemade iced tea, no names, prompt cards",
                "act2": "half-and-half canvas painting",
                "act3": "warm chai, name reveal, canvas discussion",
                "facilitator": "f1",
                "transport": "e-rickshaw, rs 30/person",
                "notes": "keep it playful",
                "invited": ["m1", "m2", "m4"],
                "confirmed": ["m2"],
                "no_show": [],
            },
            {
                "id": "e2",
                "name": "quiet board game table",
                "tier": "in between plans",
                "date": "2026-05-10",
                "time": "17:30",
                "venue": "old city cafe",
                "capacity": 6,
                "price": 899,
                "vibe": "introvert",
                "act1": "slow arrival with chai and small question cards",
                "act2": "cooperative board games in pairs",
                "act3": "cookies, soft recap, optional name reveal",
                "facilitator": "f3",
                "transport": "cab pooling optional",
                "notes": "low noise corner",
                "invited": ["m5", "m7"],
                "confirmed": ["m5", "m7"],
                "no_show": [],
            },
        ],
        "leaves": [{"fid": "f5", "from": "2026-04-26", "to": "2026-04-29", "reason": "travel", "notes": ""}],
        "messages": [
            {
                "id": "msg1",
                "from": "manju",
                "to": "riya.fac",
                "type": "session reminder",
                "subject": "canvas night",
                "body": "just a quiet nudge for the upcoming evening. keep the first act soft.",
                "ts": datetime.now().strftime("%d/%m/%Y, %H:%M"),
                "read": False,
            }
        ],
        "payments": [
            {"id": "p1", "member": "Ishita Rao", "evening": "canvas night - mp nagar", "amount": 499, "method": "razorpay", "status": "paid", "date": "2026-04-24"},
            {"id": "p2", "member": "Kabir Anand", "evening": "quiet board game table", "amount": 899, "method": "upi", "status": "pending", "date": "2026-04-25"},
        ],
        "suggestions": [],
        "config": {"sheet_url": "", "last_sync": ""},
    }


def load_data():
    if not DATA_PATH.exists():
        return seed_data()
    try:
        with DATA_PATH.open("r", encoding="utf-8") as file:
            data = json.load(file)
        base = seed_data()
        for key, value in base.items():
            data.setdefault(key, value)
        return data
    except (json.JSONDecodeError, OSError):
        return seed_data()


def save_data():
    with DATA_PATH.open("w", encoding="utf-8") as file:
        json.dump(st.session_state.data, file, indent=2, ensure_ascii=False)


def replace_data(data):
    st.session_state.data = data
    save_data()


def new_id(prefix, records):
    return f"{prefix}{len(records) + 1}"


def referral_code(name, phone):
    return f"{name[:3].upper()}{phone[-3:]}"


def init_state():
    if "data" not in st.session_state:
        st.session_state.data = load_data()
    if "user" not in st.session_state:
        st.session_state.user = None


def authenticate(uid, password):
    if uid == FOUNDER["uid"] and password == FOUNDER["pass"]:
        return FOUNDER
    for fac in st.session_state.data["facilitators"]:
        if uid == fac["uid"] and password == fac["pass"]:
            return {"uid": fac["uid"], "role": "facilitator", "name": fac["name"], "fid": fac["id"]}
    for member in st.session_state.data["members"]:
        if uid == member["email"] and password == member["referral_code"] and member["status"] == "approved":
            return {"uid": member["email"], "role": "member", "name": member["name"], "mid": member["id"]}
    return None


def login_page():
    _, middle, _ = st.columns([1, 1.1, 1])
    with middle:
        st.markdown(
            """
            <div class="login-card">
                <div class="login-logo">nook</div>
                <h1 style="margin-top:1rem">sign in</h1>
                <p style="color:#5E5146; max-width: 24rem">step into the control room for people, evenings, and the little details that make the room work.</p>
                <span class="badge orange">founder</span>
                <span class="badge gold">facilitators</span>
                <span class="badge black">members</span>
            </div>
            """,
            unsafe_allow_html=True,
        )
        with st.form("login"):
            uid = st.text_input("login id")
            password = st.text_input("password", type="password")
            submitted = st.form_submit_button("sign in", use_container_width=True)
        if submitted:
            user = authenticate(uid.strip(), password.strip())
            if user:
                st.session_state.user = user
                st.rerun()
            st.error("invalid login details.")
        with st.expander("test login"):
            st.code("manju / founder2026")


def title(kicker, title_text):
    st.markdown(
        f"""
        <div class="nook-title">
            <div class="title-row">
                <div>
                    <p>{kicker}</p>
                    <h1>{title_text}</h1>
                </div>
                <div class="title-chips">
                    <span class="title-chip gold"></span>
                    <span class="title-chip orange"></span>
                    <span class="title-chip deep"></span>
                    <span class="title-chip black"></span>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def metric(label, value, cls=""):
    return f"""
    <div class="metric-card {cls}">
        <div class="metric-label">{label}</div>
        <div class="metric-value">{value}</div>
    </div>
    """


def badge(text, cls=""):
    return f'<span class="badge {cls}">{text}</span>'


def money(amount):
    return f"rs {int(amount):,}"


def member_df(members):
    return pd.DataFrame(members)[
        ["name", "status", "presence_tag", "comfort_level", "tier", "newsletter", "sessions", "ready_for_invite"]
    ]


def get_facilitator(fid):
    return next((f for f in st.session_state.data["facilitators"] if f["id"] == fid), None)


def get_member(mid):
    return next((m for m in st.session_state.data["members"] if m["id"] == mid), None)


def auto_tag(comfort, intent):
    text = intent.lower()
    if comfort <= 2 and "introvert" in text:
        return "needs easing"
    if comfort <= 2:
        return "quiet energy"
    if any(word in text for word in ["observ", "watch", "see"]):
        return "observing"
    if comfort >= 4 and any(word in text for word in ["confid", "social", "people"]):
        return "expressive"
    return "open to new"


def tier_from_referral(code):
    if not code:
        return "first out", None
    referrer = next((m for m in st.session_state.data["members"] if m["referral_code"].lower() == code.lower()), None)
    if not referrer:
        return "first out", None
    if referrer["tier"] == "first out":
        return "in between plans", referrer["id"]
    if referrer["tier"] == "in between plans":
        return "worth it", referrer["id"]
    return "you had to be there", referrer["id"]


def create_member(name, email, phone, intent, comfort, newsletter, status="pending", referral=""):
    tier, referrer_id = tier_from_referral(referral)
    member = {
        "id": new_id("m", st.session_state.data["members"]),
        "name": name.strip() or "new member",
        "email": email.strip().lower(),
        "phone": phone.strip(),
        "budget": "",
        "availability": "",
        "activities": "",
        "intent": intent.strip(),
        "newsletter": newsletter,
        "sessions": 0,
        "tier": tier,
        "presence_tag": auto_tag(int(comfort), intent),
        "comfort_level": int(comfort),
        "referral_code": referral_code(name.strip() or "new member", phone.strip() or "000"),
        "referred_by": referrer_id,
        "referrals_used": 0,
        "joined": date.today().isoformat(),
        "status": status,
        "ready_for_invite": False,
        "notes": "",
        "fac_flag": False,
    }
    st.session_state.data["members"].append(member)
    if referrer_id:
        referrer = get_member(referrer_id)
        if referrer:
            referrer["referrals_used"] = min(3, int(referrer.get("referrals_used", 0)) + 1)
    save_data()
    return member


def sync_sheet_url(url):
    df = pd.read_csv(url)
    inserted = 0
    updated = 0
    existing_by_email = {m["email"].lower(): m for m in st.session_state.data["members"]}
    for _, row in df.fillna("").iterrows():
        name = str(row.get("name", row.get("Name", ""))).strip()
        email = str(row.get("email", row.get("Email", ""))).strip().lower()
        if not name or not email:
            continue
        phone = str(row.get("phone", row.get("Phone", ""))).strip()
        intent = str(row.get("intent", row.get("message", row.get("Message", "")))).strip()
        newsletter = str(row.get("newsletter", row.get("Newsletter", "no"))).strip().lower()
        referral = str(row.get("referral_code", row.get("Referral Code", ""))).strip()
        if email in existing_by_email:
            member = existing_by_email[email]
            member.update(
                {
                    "name": name,
                    "phone": phone or member.get("phone", ""),
                    "intent": intent or member.get("intent", ""),
                    "newsletter": "yes" if newsletter in ["yes", "y", "true", "1"] else "no",
                }
            )
            updated += 1
        else:
            create_member(
                name=name,
                email=email,
                phone=phone,
                intent=intent or "signed up from intake form",
                comfort=3,
                newsletter="yes" if newsletter in ["yes", "y", "true", "1"] else "no",
                referral=referral,
            )
            inserted += 1
    st.session_state.data["config"]["last_sync"] = datetime.now().strftime("%d/%m/%Y, %H:%M")
    save_data()
    return inserted, updated


def match_score(member, evening):
    score = 50
    tag = member["presence_tag"]
    vibe = evening["vibe"]
    if vibe == "introvert" and tag in ["quiet energy", "observing", "needs easing"]:
        score += 20
    elif vibe == "social" and tag in ["expressive", "open to new"]:
        score += 20
    elif vibe == "mixed":
        score += 10
    if member["comfort_level"] >= 4:
        score += 15
    elif member["comfort_level"] <= 2:
        score -= 10
    if member.get("ready_for_invite"):
        score += 15
    return min(100, max(0, score))


def eligible(member, evening):
    return TIER_RANK[member["tier"]] >= TIER_RANK[evening["tier"]]


def dashboard():
    data = st.session_state.data
    approved = [m for m in data["members"] if m["status"] == "approved"]
    incoming = [m for m in data["members"] if m["status"] in ["pending", "waitlist"]]
    revenue = sum(p["amount"] for p in data["payments"] if p["status"] == "paid")
    newsletter_mrr = len([m for m in approved if m["newsletter"] == "yes"]) * 99

    title("workspace", "dashboard")
    st.markdown(
        f"""
        <div class="fun-strip">
            <div class="fun-card orange"><strong>{len(incoming)} people waiting</strong><span>review the incoming list</span></div>
            <div class="fun-card gold"><strong>{len([m for m in approved if m["ready_for_invite"]])} ready</strong><span>invite-friendly members</span></div>
            <div class="fun-card soft"><strong>{len([f for f in data["facilitators"] if f["status"] != "stepped away"])} holding</strong><span>active space holders</span></div>
            <div class="fun-card black"><strong>{len(data["suggestions"])} suggestions</strong><span>from the community portal</span></div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        f"""
        <div class="metric-grid">
            {metric("total people", len(data["members"]), "feature")}
            {metric("incoming", len(incoming), "gold")}
            {metric("upcoming", len(data["experiences"]), "deep")}
            {metric("space holders", len(data["facilitators"]))}
            {metric("revenue", money(revenue), "dark")}
            {metric("newsletter mrr", money(newsletter_mrr))}
        </div>
        """,
        unsafe_allow_html=True,
    )

    left, right = st.columns([1.35, 0.65])
    with left:
        st.markdown('<div class="panel black-accent"><h3>room pulse</h3>', unsafe_allow_html=True)
        tag_counts = pd.Series([m["presence_tag"] for m in approved]).value_counts()
        st.bar_chart(tag_counts)
        st.markdown("</div>", unsafe_allow_html=True)
    with right:
        st.markdown(
            """
            <div class="panel">
                <h3>vibe signals</h3>
                <span class="badge orange">introvert heavy</span>
                <span class="badge gold">creative leaning</span>
                <span class="badge">low energy</span>
                <span class="badge black">ready to grow</span>
            </div>
            """,
            unsafe_allow_html=True,
        )

    left, right = st.columns(2)
    with left:
        st.markdown('<div class="panel"><h3>recent arrivals</h3>', unsafe_allow_html=True)
        for member in data["members"][-8:][::-1]:
            st.markdown(
                f'<div class="list-row"><strong>{member["name"]}</strong><span>{member["status"]}  -  {member["presence_tag"]}</span></div>',
                unsafe_allow_html=True,
            )
        st.markdown("</div>", unsafe_allow_html=True)
    with right:
        st.markdown('<div class="panel"><h3>upcoming experiences</h3>', unsafe_allow_html=True)
        for evening in data["experiences"][:4]:
            st.markdown(
                f'<div class="list-row"><strong>{evening["name"]}</strong><span>{evening["date"]}  -  {evening["venue"]}</span></div>',
                unsafe_allow_html=True,
            )
        st.markdown("</div>", unsafe_allow_html=True)


def incoming_page():
    title("members", "incoming")
    members = [m for m in st.session_state.data["members"] if m["status"] in ["pending", "waitlist", "declined"]]
    with st.expander("add applicant", expanded=False):
        with st.form("add_applicant"):
            c1, c2 = st.columns(2)
            name = c1.text_input("name")
            email = c2.text_input("email")
            phone = c1.text_input("phone")
            comfort = c2.slider("comfort level", 1, 5, 3)
            newsletter = c1.selectbox("newsletter", ["no", "yes"])
            referral = c2.text_input("referral code")
            intent = st.text_area("intent")
            if st.form_submit_button("add to incoming"):
                create_member(name, email, phone, intent or "new applicant", comfort, newsletter, referral=referral)
                st.success("applicant added.")
                st.rerun()

    query = st.text_input("search", placeholder="search name or presence tag")
    if query:
        members = [m for m in members if query.lower() in f'{m["name"]} {m["presence_tag"]}'.lower()]

    st.markdown('<div class="panel black-accent"><h3>waitlist</h3>', unsafe_allow_html=True)
    st.dataframe(member_df(members), use_container_width=True, hide_index=True)
    st.markdown("</div>", unsafe_allow_html=True)

    if members:
        st.subheader("review member")
        names = {m["name"]: m for m in members}
        selected = st.selectbox("select applicant", list(names))
        member = names[selected]
        c1, c2, c3, c4 = st.columns(4)
        if c1.button("approve"):
            member["status"] = "approved"
            save_data()
            st.rerun()
        if c2.button("decline"):
            member["status"] = "declined"
            save_data()
            st.rerun()
        if c3.button("hold"):
            member["status"] = "waitlist"
            save_data()
            st.rerun()
        if c4.button("flag space holder"):
            member["fac_flag"] = True
            save_data()
            st.rerun()
        with st.form("incoming_detail"):
            member["tier"] = st.selectbox("tier", list(TIER_RANK), index=list(TIER_RANK).index(member["tier"]))
            member["comfort_level"] = st.slider("comfort", 1, 5, int(member["comfort_level"]))
            member["presence_tag"] = st.selectbox(
                "presence tag",
                ["quiet energy", "open to new", "observing", "expressive", "needs easing"],
                index=["quiet energy", "open to new", "observing", "expressive", "needs easing"].index(member["presence_tag"]),
            )
            member["notes"] = st.text_area("admin notes", member.get("notes", ""))
            if st.form_submit_button("save member"):
                save_data()
                st.success("member saved.")


def inside_page():
    title("members", "inside")
    members = [m for m in st.session_state.data["members"] if m["status"] == "approved"]
    tier = st.selectbox("filter", ["all", "ready for invite", *TIER_RANK.keys()])
    if tier == "ready for invite":
        members = [m for m in members if m["ready_for_invite"]]
    elif tier != "all":
        members = [m for m in members if m["tier"] == tier]
    st.markdown('<div class="panel black-accent"><h3>approved directory</h3>', unsafe_allow_html=True)
    st.dataframe(member_df(members), use_container_width=True, hide_index=True)
    st.markdown("</div>", unsafe_allow_html=True)

    if members:
        selected = st.selectbox("edit ready status", [m["name"] for m in members])
        member = next(m for m in members if m["name"] == selected)
        with st.form("inside_member"):
            member["ready_for_invite"] = st.checkbox("ready for next invite", member["ready_for_invite"])
            member["tier"] = st.selectbox("tier", list(TIER_RANK), index=list(TIER_RANK).index(member["tier"]))
            member["sessions"] = st.number_input("sessions attended", min_value=0, value=int(member["sessions"]))
            member["newsletter"] = st.selectbox("newsletter", ["no", "yes"], index=["no", "yes"].index(member["newsletter"]))
            member["notes"] = st.text_area("member note", member.get("notes", ""))
            if st.form_submit_button("save member"):
                save_data()
                st.success("member saved.")


def builder_page():
    title("experiences", "builder")
    with st.form("experience_builder"):
        name = st.text_input("evening name")
        c1, c2, c3 = st.columns(3)
        event_date = c1.date_input("date", value=date.today())
        event_time = c2.time_input("time")
        tier = c3.selectbox("tier", list(TIER_RANK))
        venue = st.text_input("venue")
        c1, c2, c3 = st.columns(3)
        capacity = c1.slider("capacity", 4, 12, 8)
        price = c2.number_input("price", min_value=0, value=499)
        vibe = c3.selectbox("vibe", ["introvert", "social", "mixed"])
        fac_lookup = {f["name"]: f["id"] for f in st.session_state.data["facilitators"]}
        facilitator_name = st.selectbox("space holder", list(fac_lookup))
        act1 = st.text_area("act 1 - arrival", "soft arrival, no forced intros, one tiny prompt")
        act2 = st.text_area("act 2 - shared activity", "simple shared activity with rotating pairs")
        act3 = st.text_area("act 3 - unwind", "chai, cookies, name reveal, gentle closing question")
        transport = st.text_input("transport notes")
        notes = st.text_area("vibe notes")
        saved = st.form_submit_button("save evening")
    if saved:
        st.session_state.data["experiences"].append(
            {
                "id": f"e{len(st.session_state.data['experiences']) + 1}",
                "name": name or "small nook evening",
                "tier": tier,
                "date": event_date.isoformat(),
                "time": event_time.strftime("%H:%M"),
                "venue": venue or "nook venue",
                "capacity": capacity,
                "price": int(price),
                "vibe": vibe,
                "act1": act1,
                "act2": act2,
                "act3": act3,
                "facilitator": fac_lookup[facilitator_name],
                "transport": transport,
                "notes": notes,
                "invited": [],
                "confirmed": [],
                "no_show": [],
            }
        )
        save_data()
        st.success("evening saved.")


def evenings_page():
    title("experiences", "evenings")
    for evening in st.session_state.data["experiences"]:
        fac = get_facilitator(evening["facilitator"])
        with st.container(border=True):
            st.subheader(evening["name"])
            st.caption(f'{evening["date"]}  -  {evening["time"]}  -  {evening["venue"]}  -  {evening["vibe"]}')
            if st.session_state.user["role"] == "founder":
                fac_lookup = {f["name"]: f["id"] for f in st.session_state.data["facilitators"]}
                fac_names = list(fac_lookup)
                current_fac_name = next((name for name, fid in fac_lookup.items() if fid == evening["facilitator"]), fac_names[0])
                new_fac_name = st.selectbox(
                    "space holder",
                    fac_names,
                    index=fac_names.index(current_fac_name),
                    key=f'fac-{evening["id"]}',
                )
                if fac_lookup[new_fac_name] != evening["facilitator"]:
                    evening["facilitator"] = fac_lookup[new_fac_name]
                    save_data()
                    st.rerun()
            st.markdown(
                f'{badge(evening["tier"], "orange")} {badge(str(len(evening["invited"])) + " invited")} '
                f'{badge(str(len(evening["confirmed"])) + " confirmed", "gold")} {badge(money(evening["price"]), "black")}',
                unsafe_allow_html=True,
            )
            st.markdown(
                f"""
                <div class="experience-note">
                    <div class="act-note"><strong>act 1</strong>{evening["act1"]}</div>
                    <div class="act-note"><strong>act 2</strong>{evening["act2"]}</div>
                    <div class="act-note"><strong>act 3</strong>{evening["act3"]}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
            st.caption(f"space holder: {fac['name'] if fac else 'unassigned'}  -  capacity {evening['capacity']}")

            suggestions = [
                (m, match_score(m, evening))
                for m in st.session_state.data["members"]
                if m["status"] == "approved" and eligible(m, evening) and m["id"] not in evening["invited"]
            ]
            suggestions = sorted(suggestions, key=lambda item: item[1], reverse=True)[:5]
            st.markdown("**smart matches**")
            for member, score in suggestions:
                cols = st.columns([3, 1])
                cols[0].write(f'{member["name"]}  -  {member["presence_tag"]}  -  {score}/100')
                if cols[1].button("invite", key=f'invite-{evening["id"]}-{member["id"]}'):
                    evening["invited"].append(member["id"])
                    save_data()
                    st.rerun()
            invited_members = [get_member(mid) for mid in evening["invited"] if get_member(mid)]
            if invited_members:
                with st.expander("attendance"):
                    for member in invited_members:
                        cols = st.columns([3, 1, 1])
                        cols[0].write(member["name"])
                        if cols[1].button("confirm", key=f'confirm-{evening["id"]}-{member["id"]}'):
                            if member["id"] not in evening["confirmed"]:
                                evening["confirmed"].append(member["id"])
                                member["sessions"] = int(member.get("sessions", 0)) + 1
                                member["tier"] = "in between plans" if member["sessions"] >= 4 else member["tier"]
                            save_data()
                            st.rerun()
                        if cols[2].button("no-show", key=f'noshow-{evening["id"]}-{member["id"]}'):
                            if member["id"] not in evening["no_show"]:
                                evening["no_show"].append(member["id"])
                            save_data()
                            st.rerun()


def space_holders_page():
    title("team", "space holders")
    flagged = [m for m in st.session_state.data["members"] if m.get("fac_flag")]
    if flagged:
        st.markdown('<div class="panel black-accent"><h3>flagged candidates</h3>', unsafe_allow_html=True)
        for member in flagged:
            cols = st.columns([3, 1])
            cols[0].write(f'{member["name"]}  -  {member["presence_tag"]}  -  {member["sessions"]} sessions')
            if cols[1].button("onboard", key=f'onboard-{member["id"]}'):
                st.session_state.data["facilitators"].append(
                    {
                        "id": new_id("f", st.session_state.data["facilitators"]),
                        "uid": f'{member["name"].split()[0].lower()}.fac',
                        "pass": "change123",
                        "name": member["name"],
                        "style": "calm",
                        "status": "holding",
                        "access": "first out",
                        "sessions_run": 0,
                        "refs": 2,
                        "notes": "onboarded from flagged member",
                    }
                )
                member["fac_flag"] = False
                save_data()
                st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    with st.expander("add space holder"):
        with st.form("add_facilitator"):
            c1, c2 = st.columns(2)
            name = c1.text_input("name")
            uid = c2.text_input("login id")
            password = c1.text_input("temporary password", type="password")
            style = c2.selectbox("style", ["calm", "energetic"])
            access = c1.selectbox("tier access", list(TIER_RANK))
            refs = c2.number_input("referral slots", min_value=0, value=2)
            notes = st.text_area("notes")
            if st.form_submit_button("create facilitator"):
                st.session_state.data["facilitators"].append(
                    {
                        "id": new_id("f", st.session_state.data["facilitators"]),
                        "uid": uid,
                        "pass": password,
                        "name": name,
                        "style": style,
                        "status": "holding",
                        "access": access,
                        "sessions_run": 0,
                        "refs": int(refs),
                        "notes": notes,
                    }
                )
                save_data()
                st.success("facilitator created.")
                st.rerun()

    cols = st.columns(2)
    for i, fac in enumerate(st.session_state.data["facilitators"]):
        with cols[i % 2]:
            st.markdown(
                f"""
                <div class="panel">
                    <h3>{fac["name"]}</h3>
                    {badge(fac["status"], "black")} {badge(fac["style"], "orange")}
                    <p>{fac["sessions_run"]} sessions run  -  {fac["access"]} access  -  {fac["refs"]} referral slots</p>
                </div>
                """,
                unsafe_allow_html=True,
            )
            with st.expander(f"manage {fac['name']}"):
                with st.form(f"fac-{fac['id']}"):
                    fac["status"] = st.selectbox("status", ["holding", "noticing", "stepped away"], index=["holding", "noticing", "stepped away"].index(fac["status"]))
                    fac["style"] = st.selectbox("style", ["calm", "energetic"], index=["calm", "energetic"].index(fac["style"]))
                    fac["access"] = st.selectbox("access", list(TIER_RANK), index=list(TIER_RANK).index(fac["access"]))
                    fac["sessions_run"] = st.number_input("sessions run", min_value=0, value=int(fac["sessions_run"]))
                    fac["refs"] = st.number_input("referral slots", min_value=0, value=int(fac["refs"]))
                    fac["notes"] = st.text_area("notes", fac.get("notes", ""))
                    c1, c2 = st.columns(2)
                    save = c1.form_submit_button("save")
                    offboard = c2.form_submit_button("offboard")
                    if save:
                        save_data()
                        st.success("facilitator saved.")
                    if offboard:
                        fac["status"] = "stepped away"
                        save_data()
                        st.rerun()


def conduct_page():
    title("guide", "code of conduct")
    st.markdown(
        """
        <div class="panel black-accent">
        <h3>facilitator promise</h3>
        <p>hold the room before you hold the plan.</p>
        <p>notice energy, comfort, exits, silence, and small signals.</p>
        <p>never force disclosure, romance, alcohol, touch, or performance.</p>
        <p>keep member context confidential.</p>
        <p>guide the three acts: arrival, shared activity, unwind.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def onboarding_page():
    title("team", "onboarding")
    onboarding = [
        "understand nook's promise",
        "read code of conduct",
        "shadow one evening",
        "learn silent headcount",
        "practice latecomer messages",
        "review safety rules",
        "run one supported session",
        "submit reflection",
        "unlock reward level",
    ]
    offboarding = ["confirm reason", "archive access", "reassign sessions", "save reflection", "retain member profile", "close message loop", "mark status"]
    c1, c2 = st.columns(2)
    with c1:
        st.markdown('<div class="panel black-accent"><h3>onboarding checklist</h3>', unsafe_allow_html=True)
        for i, item in enumerate(onboarding, 1):
            st.write(f"{i}. {item}")
        st.markdown("</div>", unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="panel"><h3>offboarding process</h3>', unsafe_allow_html=True)
        for i, item in enumerate(offboarding, 1):
            st.write(f"{i}. {item}")
        st.markdown("</div>", unsafe_allow_html=True)


def leave_page():
    title("team", "leave")
    st.dataframe(pd.DataFrame(st.session_state.data["leaves"]), use_container_width=True, hide_index=True)
    with st.form("leave"):
        fac_lookup = {f["name"]: f["id"] for f in st.session_state.data["facilitators"]}
        name = st.selectbox("facilitator", list(fac_lookup))
        c1, c2 = st.columns(2)
        start = c1.date_input("from")
        end = c2.date_input("to")
        reason = st.text_input("reason")
        notes = st.text_area("notes")
        if st.form_submit_button("save leave"):
            st.session_state.data["leaves"].append({"fid": fac_lookup[name], "from": start.isoformat(), "to": end.isoformat(), "reason": reason, "notes": notes})
            save_data()
            st.rerun()
    if st.session_state.user["role"] == "founder" and st.session_state.data["leaves"]:
        remove_idx = st.selectbox("remove leave record", ["none", *[f'{i + 1}. {leave["reason"]} ({leave["from"]})' for i, leave in enumerate(st.session_state.data["leaves"])]])
        if remove_idx != "none" and st.button("remove selected leave"):
            index = int(remove_idx.split(".", 1)[0]) - 1
            st.session_state.data["leaves"].pop(index)
            save_data()
            st.rerun()


def messages_page():
    title("team", "messages")
    user = st.session_state.user
    inbox = [m for m in st.session_state.data["messages"] if m["to"] == user["uid"] or m["from"] == user["uid"]]
    c1, c2 = st.columns([0.8, 1.2])
    with c1:
        with st.form("message"):
            users = [{"uid": "manju", "name": "Manju Singh"}] + [
                {"uid": f["uid"], "name": f["name"]} for f in st.session_state.data["facilitators"]
            ]
            users = [u for u in users if u["uid"] != user["uid"]]
            lookup = {u["name"]: u["uid"] for u in users}
            to_name = st.selectbox("to", list(lookup))
            msg_type = st.selectbox("type", ["general", "invite", "reminder", "post-session", "urgent", "custom request"])
            subject = st.text_input("subject")
            body = st.text_area("body")
            if st.form_submit_button("send"):
                st.session_state.data["messages"].append(
                    {
                        "id": f"msg{len(st.session_state.data['messages']) + 1}",
                        "from": user["uid"],
                        "to": lookup[to_name],
                        "type": msg_type,
                        "subject": subject,
                        "body": body,
                        "ts": datetime.now().strftime("%d/%m/%Y, %H:%M"),
                        "read": False,
                    }
                )
                save_data()
                st.rerun()
    with c2:
        for message in inbox[::-1]:
            st.markdown(
                f"""
                <div class="list-row">
                    <strong>{message["subject"] or "message"}</strong>
                    <span>{message["type"]}  -  {message["ts"]}</span>
                    <p>{message["body"]}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )


def newsletter_page():
    title("founder", "newsletter")
    approved = [m for m in st.session_state.data["members"] if m["status"] == "approved"]
    subscribers = [m for m in approved if m["newsletter"] == "yes"]
    st.markdown(
        f"""
        <div class="metric-grid">
            {metric("subscribers", len(subscribers), "feature")}
            {metric("non-subscribers", len(approved) - len(subscribers), "gold")}
            {metric("mrr", money(len(subscribers) * 99), "dark")}
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.dataframe(member_df(subscribers), use_container_width=True, hide_index=True)


def payments_page():
    title("founder", "payments")
    payments = st.session_state.data["payments"]
    collected = sum(p["amount"] for p in payments if p["status"] == "paid")
    pending = len([p for p in payments if p["status"] == "pending"])
    st.markdown(
        f"""
        <div class="metric-grid">
            {metric("collected", money(collected), "feature")}
            {metric("pending", pending, "gold")}
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.dataframe(pd.DataFrame(payments), use_container_width=True, hide_index=True)
    pending = [p for p in payments if p["status"] == "pending"]
    if pending:
        selected = st.selectbox("mark payment paid", [f'{p["id"]}  -  {p["member"]}  -  {money(p["amount"])}' for p in pending])
        if st.button("mark selected as paid"):
            payment_id = selected.split("  -  ", 1)[0]
            next(p for p in payments if p["id"] == payment_id)["status"] = "paid"
            save_data()
            st.rerun()
    with st.form("payment"):
        member = st.text_input("member")
        evening = st.text_input("evening")
        amount = st.number_input("amount", min_value=0, value=499)
        method = st.selectbox("method", ["razorpay", "upi", "cash", "manual"])
        status = st.selectbox("status", ["paid", "pending"])
        if st.form_submit_button("add payment"):
            payments.append({"id": f"p{len(payments) + 1}", "member": member, "evening": evening, "amount": int(amount), "method": method, "status": status, "date": date.today().isoformat()})
            save_data()
            st.rerun()


def insights_page():
    title("founder", "insights")
    data = st.session_state.data
    approved = [m for m in data["members"] if m["status"] == "approved"]
    invited = sum(len(e["invited"]) for e in data["experiences"])
    confirmed = sum(len(e["confirmed"]) for e in data["experiences"])
    show_rate = round((confirmed / max(invited, 1)) * 100)
    st.markdown(
        f"""
        <div class="metric-grid">
            {metric("show rate", f"{show_rate}%", "feature")}
            {metric("repeat visitors", len([m for m in approved if m["sessions"] >= 2]), "gold")}
            {metric("evenings", len(data["experiences"]), "deep")}
            {metric("avg comfort", round(sum(m["comfort_level"] for m in approved) / max(len(approved), 1), 1), "dark")}
        </div>
        """,
        unsafe_allow_html=True,
    )
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("presence tags")
        st.bar_chart(pd.Series([m["presence_tag"] for m in approved]).value_counts())
    with c2:
        st.subheader("tiers")
        st.bar_chart(pd.Series([m["tier"] for m in approved]).value_counts())


def settings_page():
    title("founder", "settings")
    data = st.session_state.data
    with st.form("sheet_settings"):
        sheet_url = st.text_input("google sheet csv url", data["config"].get("sheet_url", ""))
        c1, c2 = st.columns(2)
        save_url = c1.form_submit_button("save url")
        sync_now = c2.form_submit_button("sync now")
        if save_url:
            data["config"]["sheet_url"] = sheet_url
            save_data()
            st.success("sheet url saved.")
        if sync_now:
            data["config"]["sheet_url"] = sheet_url
            if not sheet_url:
                st.warning("add a published csv url first.")
            else:
                try:
                    inserted, updated = sync_sheet_url(sheet_url)
                    st.success(f"sync complete: {inserted} new, {updated} updated.")
                except Exception as exc:
                    st.error(f"sync failed: {exc}")
    st.caption(f"last sync: {data['config'].get('last_sync') or 'never'}")

    st.download_button(
        "export json",
        data=json.dumps(data, indent=2),
        file_name="nook-data.json",
        mime="application/json",
    )

    imported = st.text_area("import json")
    if st.button("import data") and imported:
        try:
            replace_data(json.loads(imported))
            st.success("data imported.")
            st.rerun()
        except json.JSONDecodeError:
            st.error("invalid json.")

    confirm = st.text_input("type reset to reset demo data")
    if st.button("reset demo data") and confirm == "reset":
        replace_data(seed_data())
        st.rerun()


def community_page():
    title("community", "member portal")
    user = st.session_state.user
    member = get_member(user.get("mid")) if user["role"] == "member" else next(m for m in st.session_state.data["members"] if m["status"] == "approved")
    st.markdown(
        f"""
        <div class="metric-grid">
            {metric(member["name"], member["tier"], "feature")}
            {metric("sessions", member["sessions"], "gold")}
            {metric("referral slots", f"{3 - member['referrals_used']}/3", "deep")}
            {metric("code", member["referral_code"], "dark")}
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.subheader("eligible experiences")
    for evening in st.session_state.data["experiences"]:
        if eligible(member, evening):
            cols = st.columns([4, 1])
            cols[0].write(f'{evening["name"]}  -  {evening["date"]}  -  {money(evening["price"])}')
            if cols[1].button("sign up", key=f'community-{evening["id"]}'):
                if member["id"] not in evening["confirmed"]:
                    evening["confirmed"].append(member["id"])
                    save_data()
                st.success("signed up.")
    with st.form("community_suggestion"):
        st.subheader("suggest an interest")
        name = st.text_input("name")
        suggestion_type = st.selectbox("type", ["activity", "cafe", "walk", "other"])
        description = st.text_area("description")
        if st.form_submit_button("send suggestion"):
            st.session_state.data["suggestions"].append(
                {
                    "id": new_id("s", st.session_state.data["suggestions"]),
                    "member": member["id"],
                    "name": name,
                    "type": suggestion_type,
                    "description": description,
                    "created": date.today().isoformat(),
                }
            )
            save_data()
            st.success("suggestion saved.")


PAGES = {
    "dashboard": (dashboard, ["founder", "facilitator"]),
    "incoming": (incoming_page, ["founder"]),
    "inside": (inside_page, ["founder"]),
    "experience builder": (builder_page, ["founder"]),
    "evenings": (evenings_page, ["founder", "facilitator"]),
    "space holders": (space_holders_page, ["founder", "facilitator"]),
    "code of conduct": (conduct_page, ["founder", "facilitator"]),
    "onboarding": (onboarding_page, ["founder", "facilitator"]),
    "leave": (leave_page, ["founder", "facilitator"]),
    "messages": (messages_page, ["founder", "facilitator"]),
    "newsletter": (newsletter_page, ["founder"]),
    "payments": (payments_page, ["founder"]),
    "insights": (insights_page, ["founder"]),
    "settings": (settings_page, ["founder"]),
    "community portal": (community_page, ["member", "founder", "facilitator"]),
}


def sidebar():
    user = st.session_state.user
    with st.sidebar:
        st.markdown(
            """
            <div class="sidebar-brand">
                <h2>nook</h2>
                <p>control room</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        allowed_pages = [name for name, (_, roles) in PAGES.items() if user["role"] in roles]
        if user["role"] != "member" and "community portal" in allowed_pages:
            allowed_pages.remove("community portal")
        page = st.radio("navigate", allowed_pages, label_visibility="collapsed")
        st.markdown("---")
        st.markdown(
            f"""
            <div class="sidebar-account">
                <strong>{user["name"]}</strong><br>
                <span style="color:#5E5146">{user["role"]}</span>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if st.button("log out", use_container_width=True):
            st.session_state.user = None
            st.rerun()
    return page


def main():
    inject_css()
    init_state()
    if not st.session_state.user:
        login_page()
        return
    page = sidebar()
    PAGES[page][0]()
    st.caption("nook control room")


if __name__ == "__main__":
    main()


