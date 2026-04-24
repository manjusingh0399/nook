import json
from copy import deepcopy
from datetime import date, datetime
from pathlib import Path
from typing import Dict, List, Optional
from uuid import uuid4

import streamlit as st


APP_DIR = Path(__file__).resolve().parent
DATA_FILE = APP_DIR / "nook_data.json"

KLEIN_BLUE = "#4100F5"
CITRIC = "#CDF54E"
AQUAMARINE = "#9BF0E7"
FUCHSIA = "#E637A5"
TANGERINE = "#FF463B"
NOOK_BLACK = "#191414"
ORANGE = TANGERINE
BG = NOOK_BLACK
SURFACE = "#231C1B"
SURFACE_ALT = "#2D2423"
BORDER = "rgba(155,240,231,0.18)"
TEXT = "#FFFDF7"
MUTED = "#DDD5CE"

USERS = [
    {"id": "manju", "name": "Manju Singh", "role": "founder", "password": "founder2026"},
    {"id": "riya.fac", "name": "Riya Kapoor", "role": "facilitator", "password": "riya123", "fac_id": "f1"},
    {"id": "aryan.fac", "name": "Aryan Mehta", "role": "facilitator", "password": "aryan123", "fac_id": "f2"},
    {"id": "sneha.fac", "name": "Sneha Joshi", "role": "facilitator", "password": "sneha123", "fac_id": "f3"},
    {"id": "rohan.fac", "name": "Rohan Verma", "role": "facilitator", "password": "rohan123", "fac_id": "f4"},
    {"id": "priya.fac", "name": "Priya Sharma", "role": "facilitator", "password": "priya123", "fac_id": "f5"},
]

DEMO_MEMBERS = [
    {
        "id": "m1",
        "name": "Aditi Rao",
        "email": "aditi@example.com",
        "phone": "9876500001",
        "budget": "₹500-₹800",
        "availability": "Friday evenings",
        "activities": "art jam, cafe hopping, storytelling",
        "intent": "I want to meet thoughtful people in Bhopal without loud networking energy.",
        "cafe": "A leafy rooftop cafe",
        "message": "I like small groups and warm energy.",
        "newsletter": "yes",
        "sessions": 3,
        "ts": "2026-04-12 18:20",
    },
    {
        "id": "m2",
        "name": "Kabir Sethi",
        "email": "kabir@example.com",
        "phone": "9876500002",
        "budget": "₹800-₹1200",
        "availability": "Saturday evenings",
        "activities": "board games, live music, dinners",
        "intent": "I want easy social plans where I do not have to organize everything.",
        "cafe": "Quiet music cafe",
        "message": "Would love a premium membership if the curation is strong.",
        "newsletter": "no",
        "sessions": 1,
        "ts": "2026-04-15 11:05",
    },
    {
        "id": "m3",
        "name": "Naina Joseph",
        "email": "naina@example.com",
        "phone": "9876500003",
        "budget": "₹1200+",
        "availability": "Weekends only",
        "activities": "pottery, long conversations, brunches",
        "intent": "Looking for a reliable third place after moving here.",
        "cafe": "Ceramic studio or breakfast place",
        "message": "Okay with being on the waitlist if needed.",
        "newsletter": "yes",
        "sessions": 5,
        "ts": "2026-04-17 09:42",
    },
    {
        "id": "m4",
        "name": "Rahul Jain",
        "email": "rahul@example.com",
        "phone": "9876500004",
        "budget": "₹500-₹800",
        "availability": "Any weekday",
        "activities": "coffee tastings, walks, quiz nights",
        "intent": "I want something intimate and local, not event-company vibes.",
        "cafe": "Open to suggestions",
        "message": "Can also help as volunteer later.",
        "newsletter": "yes",
        "sessions": 0,
        "ts": "2026-04-19 20:10",
    },
]

DEMO_ADMIN = {
    "m1": {"status": "approved", "tier": "wi", "notes": "Warm fit. Could become facilitator later.", "fac": False},
    "m2": {"status": "pending", "tier": "fo", "notes": "", "fac": False},
    "m3": {"status": "approved", "tier": "yhttb", "notes": "Excellent retention candidate.", "fac": True},
    "m4": {"status": "waitlist", "tier": "fo", "notes": "Follow up next month.", "fac": False},
}

DEMO_FACS = [
    {
        "id": "f1",
        "name": "Riya Kapoor",
        "uid": "riya.fac",
        "password": "riya123",
        "email": "riya@example.com",
        "phone": "9876511111",
        "status": "active",
        "access": "wi",
        "refs": 3,
        "sessions": 7,
        "notes": "Great with quieter groups and soft check-ins.",
    },
    {
        "id": "f2",
        "name": "Aryan Mehta",
        "uid": "aryan.fac",
        "password": "aryan123",
        "email": "aryan@example.com",
        "phone": "9876511112",
        "status": "candidate",
        "access": "fo",
        "refs": 2,
        "sessions": 3,
        "notes": "Still being observed across different room dynamics.",
    },
    {
        "id": "f3",
        "name": "Sneha Joshi",
        "uid": "sneha.fac",
        "password": "sneha123",
        "email": "sneha@example.com",
        "phone": "9876511113",
        "status": "active",
        "access": "yhttb",
        "refs": 5,
        "sessions": 11,
        "notes": "Helps shape future formats with Manju.",
    },
    {
        "id": "f4",
        "name": "Rohan Verma",
        "uid": "rohan.fac",
        "password": "rohan123",
        "email": "rohan@example.com",
        "phone": "9876511114",
        "status": "offboarded",
        "access": "fo",
        "refs": 1,
        "sessions": 4,
        "notes": "Stepped away due to travel.",
    },
    {
        "id": "f5",
        "name": "Priya Sharma",
        "uid": "priya.fac",
        "password": "priya123",
        "email": "priya@example.com",
        "phone": "9876511115",
        "status": "active",
        "access": "ibp",
        "refs": 3,
        "sessions": 6,
        "notes": "Strong at opening-circle prompts.",
    },
]

DEMO_EXPERIENCES = [
    {
        "id": "e1",
        "name": "Canvas Night - MP Nagar",
        "tier": "fo",
        "date": "2026-04-27",
        "time": "18:00",
        "max": 8,
        "price": 500,
        "venue": "The Quiet Table, MP Nagar",
        "fac": "f1",
        "transport": "Auto cluster, approx ₹40/person",
        "act1": "Iced tea opener and no-name prompt cards",
        "act2": "Half-and-half canvas painting",
        "act3": "Warm chai and story reveal",
        "notes": "Keep the lighting intimate; new-member heavy room.",
    },
    {
        "id": "e2",
        "name": "Pottery & Pour Over",
        "tier": "wi",
        "date": "2026-05-02",
        "time": "17:30",
        "max": 10,
        "price": 950,
        "venue": "Clay House Studio",
        "fac": "f3",
        "transport": "Cabs shared in pairs",
        "act1": "Table warm-up using object stories",
        "act2": "Paired pottery build",
        "act3": "Coffee tasting unwind",
        "notes": "Good fit for returning members.",
    },
    {
        "id": "e3",
        "name": "Secret Supper Walk",
        "tier": "yhttb",
        "date": "2026-05-09",
        "time": "19:00",
        "max": 6,
        "price": 1500,
        "venue": "Old City route",
        "fac": "f5",
        "transport": "Walkable route",
        "act1": "Mystery ingredient cards",
        "act2": "Shared tasting circuit",
        "act3": "Late-night chai debrief",
        "notes": "Founder may attend quietly.",
    },
]

DEMO_LEAVES = [
    {"id": "l1", "fid": "f2", "from": "2026-04-24", "to": "2026-04-28", "reason": "Travel", "notes": "Back after family wedding."}
]

DEMO_MESSAGES = [
    {
        "id": "msg1",
        "from": "manju",
        "to": "riya.fac",
        "subject": "Session reminder",
        "body": "Please arrive 10 minutes early for Canvas Night and check in with new members quietly.",
        "ts": "2026-04-23 20:10",
        "read": False,
    },
    {
        "id": "msg2",
        "from": "riya.fac",
        "to": "manju",
        "subject": "Post-session update",
        "body": "Aditi felt like a strong community fit. I can share fuller notes after tomorrow.",
        "ts": "2026-04-23 22:40",
        "read": True,
    },
]

DEMO_PAYMENTS = [
    {"id": "p1", "member_id": "m1", "label": "Worth It monthly", "amount": 1499, "status": "paid"},
    {"id": "p2", "member_id": "m3", "label": "YHTTB monthly", "amount": 2499, "status": "paid"},
    {"id": "p3", "member_id": "m2", "label": "First Out trial", "amount": 499, "status": "pending"},
]


def default_data() -> Dict:
    return {
        "members": deepcopy(DEMO_MEMBERS),
        "facs": deepcopy(DEMO_FACS),
        "exps": deepcopy(DEMO_EXPERIENCES),
        "leaves": deepcopy(DEMO_LEAVES),
        "msgs": deepcopy(DEMO_MESSAGES),
        "payments": deepcopy(DEMO_PAYMENTS),
        "admin": deepcopy(DEMO_ADMIN),
    }


def load_data() -> Dict:
    if DATA_FILE.exists():
        return json.loads(DATA_FILE.read_text(encoding="utf-8"))
    data = default_data()
    save_data(data)
    return data


def save_data(data: Dict) -> None:
    DATA_FILE.write_text(json.dumps(data, indent=2), encoding="utf-8")


def auto_tier(sessions: int) -> str:
    if sessions >= 5:
        return "yhttb"
    if sessions >= 3:
        return "wi"
    if sessions >= 2:
        return "ibp"
    return "fo"


def tier_label(code: str) -> str:
    return {
        "fo": "First Out",
        "ibp": "In Between Plans",
        "wi": "Worth It",
        "yhttb": "YHTTB",
    }.get(code, code.upper())


def status_badge(status: str) -> str:
    styles = {
        "pending": (CITRIC, NOOK_BLACK, "rgba(205,245,78,0.45)"),
        "approved": (AQUAMARINE, NOOK_BLACK, "rgba(155,240,231,0.42)"),
        "declined": (TANGERINE, NOOK_BLACK, "rgba(255,70,59,0.45)"),
        "waitlist": (FUCHSIA, TEXT, "rgba(230,55,165,0.38)"),
        "active": (AQUAMARINE, NOOK_BLACK, "rgba(155,240,231,0.42)"),
        "candidate": (CITRIC, NOOK_BLACK, "rgba(205,245,78,0.45)"),
        "offboarded": (NOOK_BLACK, TEXT, "rgba(255,253,247,0.16)"),
    }
    bg, fg, border = styles.get(status, (TANGERINE, NOOK_BLACK, "rgba(255,70,59,0.45)"))
    return (
        f"<span style='padding:4px 10px;border-radius:999px;"
        f"background:{bg};color:{fg};border:1px solid {border};"
        f"font-size:12px;font-weight:700;letter-spacing:0.02em'>{status.title()}</span>"
    )


def pill_html(text: str, tone: str = "aqua") -> str:
    tone_map = {
        "klein": (KLEIN_BLUE, TEXT, "rgba(255,255,255,0.12)"),
        "citric": (CITRIC, NOOK_BLACK, "rgba(205,245,78,0.45)"),
        "aqua": (AQUAMARINE, NOOK_BLACK, "rgba(155,240,231,0.42)"),
        "fuchsia": (FUCHSIA, TEXT, "rgba(230,55,165,0.38)"),
        "tangerine": (TANGERINE, NOOK_BLACK, "rgba(255,70,59,0.45)"),
        "black": (NOOK_BLACK, TEXT, "rgba(255,253,247,0.16)"),
    }
    bg, fg, border = tone_map[tone]
    return (
        f"<span class='pill' style='background:{bg};color:{fg};border:1px solid {border};'>"
        f"{text}</span>"
    )


def tier_badge(code: str) -> str:
    tone = {
        "fo": "klein",
        "ibp": "aqua",
        "wi": "citric",
        "yhttb": "fuchsia",
    }.get(code, "tangerine")
    return pill_html(tier_label(code), tone=tone)


def current_user() -> Optional[Dict]:
    return st.session_state.get("current_user")


def data_store() -> Dict:
    if "data" not in st.session_state:
        st.session_state.data = load_data()
    return st.session_state.data


def persist() -> None:
    save_data(st.session_state.data)


def get_admin(member_id: str) -> Dict:
    data = data_store()
    member = next((m for m in data["members"] if m["id"] == member_id), None)
    fallback_tier = auto_tier(member.get("sessions", 0) if member else 0)
    return data["admin"].setdefault(member_id, {"status": "pending", "tier": fallback_tier, "notes": "", "fac": False})


def get_fac(fid: str) -> Optional[Dict]:
    return next((f for f in data_store()["facs"] if f["id"] == fid), None)


def on_leave(fid: str) -> bool:
    today = date.today().isoformat()
    return any(l["fid"] == fid and l["from"] <= today <= l["to"] for l in data_store()["leaves"])


def authenticate(username: str, password: str) -> Optional[Dict]:
    for user in USERS:
        if user["id"] == username and user["password"] == password:
            return user
    return None


def inject_css() -> None:
    st.markdown(
        f"""
        <style>
        :root {{
            --klein-blue: {KLEIN_BLUE};
            --citric: {CITRIC};
            --aquamarine: {AQUAMARINE};
            --fuchsia: {FUCHSIA};
            --tangerine: {TANGERINE};
            --nook-black: {NOOK_BLACK};
            --text-main: {TEXT};
            --text-soft: {MUTED};
            --surface: {SURFACE};
            --surface-alt: {SURFACE_ALT};
        }}
        .stApp {{
            background:
                radial-gradient(circle at top left, rgba(65,0,245,0.28), transparent 26%),
                radial-gradient(circle at top right, rgba(230,55,165,0.16), transparent 24%),
                radial-gradient(circle at bottom left, rgba(255,70,59,0.16), transparent 20%),
                linear-gradient(135deg, #191414, #120f16 52%, #1b1715);
            color: {TEXT};
        }}
        [data-testid="stAppViewContainer"] {{
            background: transparent;
        }}
        .block-container {{
            padding-top: 1.5rem;
            padding-bottom: 3rem;
        }}
        [data-testid="stSidebar"] {{
            background:
                radial-gradient(circle at top, rgba(65,0,245,0.25), transparent 32%),
                linear-gradient(180deg, #191414, #130f14 50%, #0f0c12);
            border-right: 1px solid {BORDER};
        }}
        [data-testid="stSidebar"] * {{
            color: {TEXT} !important;
        }}
        [data-testid="stMetric"] {{
            background: {SURFACE};
            border: 1px solid {BORDER};
            padding: 18px;
            border-radius: 18px;
            box-shadow: 0 12px 24px rgba(0,0,0,0.16);
        }}
        [data-testid="stMetricLabel"],
        [data-testid="stMetricValue"],
        [data-testid="stMetricDelta"] {{
            color: {TEXT} !important;
        }}
        h1, h2, h3, p, li, label, .stMarkdown, .stCaption, .stAlert {{
            color: {TEXT};
        }}
        div[data-baseweb="input"] > div,
        div[data-baseweb="select"] > div,
        div[data-baseweb="textarea"] > div,
        .stTextInput input,
        .stTextArea textarea,
        .stDateInput input,
        .stNumberInput input {{
            background: {SURFACE_ALT};
            color: {TEXT};
            border: 1px solid rgba(155,240,231,0.24);
        }}
        div[data-baseweb="input"] input,
        div[data-baseweb="select"] * ,
        div[data-baseweb="textarea"] textarea,
        .stDateInput * ,
        .stNumberInput input {{
            color: {TEXT} !important;
        }}
        div[data-baseweb="select"] > div,
        div[data-baseweb="input"] > div,
        div[data-baseweb="textarea"] > div {{
            background: {SURFACE_ALT};
            border-radius: 14px;
        }}
        .stTextInput label,
        .stTextArea label,
        .stDateInput label,
        .stSelectbox label,
        .stNumberInput label {{
            color: {TEXT} !important;
            font-weight: 600;
        }}
        .stButton > button,
        .stForm [data-testid="stFormSubmitButton"] > button {{
            border-radius: 14px;
            border: 1px solid rgba(255,255,255,0.12);
            min-height: 2.75rem;
            font-weight: 700;
            letter-spacing: 0.01em;
        }}
        .stButton > button[kind="primary"],
        .stForm [data-testid="stFormSubmitButton"] > button[kind="primary"] {{
            background: linear-gradient(135deg, {CITRIC}, {AQUAMARINE});
            color: {NOOK_BLACK};
            border-color: rgba(155,240,231,0.4);
            box-shadow: 0 12px 30px rgba(155,240,231,0.16);
        }}
        .stButton > button[kind="secondary"],
        .stForm [data-testid="stFormSubmitButton"] > button[kind="secondary"] {{
            background: rgba(255,255,255,0.035);
            color: {TEXT};
            border-color: rgba(255,255,255,0.1);
        }}
        .stButton > button:hover,
        .stForm [data-testid="stFormSubmitButton"] > button:hover {{
            border-color: rgba(205,245,78,0.55);
            color: {TEXT};
        }}
        .stExpander {{
            background: rgba(35,28,27,0.94);
            border: 1px solid {BORDER};
            border-radius: 18px;
            overflow: hidden;
        }}
        .stExpander details summary p {{
            color: {TEXT} !important;
            font-weight: 600;
        }}
        .card {{
            background: linear-gradient(180deg, rgba(35,28,27,0.96), rgba(26,20,22,0.96));
            border: 1px solid {BORDER};
            border-radius: 20px;
            padding: 22px;
            margin-bottom: 16px;
            box-shadow: 0 12px 32px rgba(0,0,0,0.22);
        }}
        .eyebrow {{
            color: {CITRIC};
            font-size: 12px;
            letter-spacing: 0.18em;
            text-transform: uppercase;
            margin-bottom: 8px;
            font-weight: 700;
        }}
        .hero {{
            background:
                linear-gradient(115deg, rgba(65,0,245,0.34), rgba(230,55,165,0.18) 38%, rgba(255,70,59,0.2) 70%, rgba(155,240,231,0.14));
            border: 1px solid rgba(155,240,231,0.24);
            border-radius: 24px;
            padding: 28px;
            margin-bottom: 18px;
            box-shadow: 0 18px 44px rgba(0,0,0,0.24);
        }}
        .hero h1 {{
            margin: 0;
            font-size: 46px;
            line-height: 0.95;
        }}
        .muted {{
            color: {MUTED};
        }}
        .session-card {{
            background: linear-gradient(180deg, rgba(29,23,24,0.98), rgba(24,19,21,0.98));
            border: 1px solid {BORDER};
            border-left: 4px solid {AQUAMARINE};
            border-radius: 18px;
            padding: 18px;
            margin-bottom: 14px;
        }}
        .subtle {{
            color: {MUTED};
            font-size: 13px;
        }}
        .pill {{
            display: inline-block;
            padding: 4px 10px;
            border-radius: 999px;
            margin-right: 8px;
            font-weight: 700;
            margin-bottom: 8px;
            font-size: 12px;
        }}
        .sidebar-brand {{
            background: linear-gradient(160deg, rgba(65,0,245,0.26), rgba(25,20,20,0.82) 45%, rgba(255,70,59,0.18));
            border: 1px solid rgba(155,240,231,0.18);
            border-radius: 20px;
            padding: 16px;
            margin-bottom: 14px;
        }}
        .sidebar-brand h3 {{
            margin: 0 0 4px 0;
            color: {TEXT};
        }}
        .swatch-row {{
            display: flex;
            gap: 8px;
            margin-top: 12px;
        }}
        .swatch {{
            width: 18px;
            height: 18px;
            border-radius: 999px;
            border: 1px solid rgba(255,255,255,0.16);
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )


def login_screen() -> None:
    inject_css()
    left, right = st.columns([1.25, 1], gap="large")
    with left:
        st.markdown(
            f"""
            <div class="hero">
              <div class="eyebrow">Nook Control Room</div>
              <h1>Your<br><span style="color:{CITRIC}">third</span><br>place.</h1>
              <p class="muted" style="margin-top:14px;font-size:15px;max-width:540px">
                Founder and facilitator operations in one Streamlit control room, with separate access levels,
                planning flows, leave tracking, member review, and internal messaging.
              </p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown(
            """
            <div class="card">
              <div class="eyebrow">Sample Accounts</div>
              <div class="subtle">Founder: <strong>manju / founder2026</strong></div>
              <div class="subtle">Facilitator: <strong>riya.fac / riya123</strong></div>
              <div class="subtle">Facilitator: <strong>aryan.fac / aryan123</strong></div>
              <div class="subtle">Facilitator: <strong>sneha.fac / sneha123</strong></div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with right:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.subheader("Sign in")
        with st.form("login_form"):
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            submitted = st.form_submit_button("Enter Control Room", use_container_width=True, type="primary")
        if submitted:
            user = authenticate(username.strip(), password)
            if user:
                st.session_state.current_user = user
                st.rerun()
            st.error("Wrong credentials. Contact Manju.")
        st.markdown("</div>", unsafe_allow_html=True)


def sidebar_navigation(user: Dict) -> str:
    founder_pages = [
        "Dashboard",
        "Members",
        "Planner",
        "Facilitator Team",
        "Leave",
        "Messages",
        "Docs",
    ]
    facilitator_pages = [
        "Dashboard",
        "My Sessions",
        "My Profile",
        "Leave",
        "Messages",
    ]
    options = founder_pages if user["role"] == "founder" else facilitator_pages
    if st.session_state.get("page") not in options:
        st.session_state.page = options[0]

    with st.sidebar:
        st.markdown(
            f"""
            <div class="sidebar-brand">
              <div class="eyebrow">Logged in</div>
              <h3>{user['name']}</h3>
              <div class="subtle">{user['role'].title()} view</div>
              <div class="swatch-row">
                <div class="swatch" style="background:{KLEIN_BLUE}"></div>
                <div class="swatch" style="background:{CITRIC}"></div>
                <div class="swatch" style="background:{AQUAMARINE}"></div>
                <div class="swatch" style="background:{FUCHSIA}"></div>
                <div class="swatch" style="background:{TANGERINE}"></div>
              </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.caption("Navigation")
        for page in options:
            is_active = st.session_state.page == page
            if st.button(page, key=f"nav_{page}", use_container_width=True, type="primary" if is_active else "secondary"):
                st.session_state.page = page
        st.markdown("---")
        if st.button("Log out", use_container_width=True, type="secondary"):
            st.session_state.pop("current_user", None)
            st.rerun()
    return st.session_state.page


def show_header(title: str, subtitle: str) -> None:
    st.markdown(
        f"""
        <div class="hero">
          <div class="eyebrow">{title}</div>
          <p style="font-size:15px;margin:0;color:{MUTED}">{subtitle}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_dashboard(user: Dict) -> None:
    data = data_store()
    show_header("Dashboard", "Your control centre across members, sessions, facilitators, and internal coordination.")
    if user["role"] == "founder":
        approved = sum(1 for m in data["members"] if get_admin(m["id"])["status"] == "approved")
        pending = sum(1 for m in data["members"] if get_admin(m["id"])["status"] == "pending")
        revenue = sum(p["amount"] for p in data["payments"] if p["status"] == "paid")
        active_facs = sum(1 for f in data["facs"] if f["status"] == "active")
        a, b, c, d = st.columns(4)
        a.metric("Total submissions", len(data["members"]))
        b.metric("Pending review", pending)
        c.metric("Revenue collected", f"₹{revenue:,}")
        d.metric("Active facilitators", active_facs)

        left, right = st.columns([1.15, 0.85], gap="large")
        with left:
            st.markdown("### Recent submissions")
            for member in reversed(data["members"][-4:]):
                admin = get_admin(member["id"])
                st.markdown(
                    f"""
                    <div class="card">
                      <strong>{member["name"]}</strong><br>
                      <span class="subtle">{member["email"]} · {member["ts"]}</span><br><br>
                      {status_badge(admin["status"])}
                      {tier_badge(admin["tier"])}
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
        with right:
            st.markdown("### Upcoming sessions")
            for exp in data["exps"][:3]:
                fac = get_fac(exp["fac"])
                st.markdown(
                    f"""
                    <div class="session-card">
                      {tier_badge(exp["tier"])}
                      <strong>{exp["name"]}</strong><br>
                      <span class="subtle">{exp["date"]} · {exp["time"]} · {exp["venue"]}</span><br>
                      <span class="subtle">Facilitator: {fac["name"] if fac else "Unassigned"}</span>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
    else:
        fac = get_fac(user["fac_id"]) or {}
        my_sessions = [e for e in data["exps"] if e["fac"] == user["fac_id"]]
        unread = sum(1 for m in data["msgs"] if m["to"] == user["id"] and not m["read"])
        a, b, c, d = st.columns(4)
        a.metric("My sessions", len(my_sessions))
        b.metric("My status", fac.get("status", "-").title())
        c.metric("Referral slots", fac.get("refs", 0))
        d.metric("Unread messages", unread)
        st.markdown("### My upcoming sessions")
        if not my_sessions:
            st.info("No sessions assigned yet.")
        for exp in my_sessions:
            st.markdown(
                f"""
                <div class="session-card">
                  {tier_badge(exp["tier"])}
                  <strong>{exp["name"]}</strong><br>
                  <span class="subtle">{exp["date"]} · {exp["time"]} · {exp["venue"]} · Max {exp["max"]}</span>
                  <hr style="border-color:{BORDER}">
                  <div class="subtle"><strong>Act 1:</strong> {exp["act1"]}</div>
                  <div class="subtle"><strong>Act 2:</strong> {exp["act2"]}</div>
                  <div class="subtle"><strong>Act 3:</strong> {exp["act3"]}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )


def render_members() -> None:
    data = data_store()
    show_header("Members", "Review incoming Nook submissions, approve people, set tiers, and identify future facilitators.")
    status_filter = st.selectbox("Filter by status", ["all", "pending", "approved", "waitlist", "declined"])
    for member in data["members"]:
        admin = get_admin(member["id"])
        if status_filter != "all" and admin["status"] != status_filter:
            continue
        with st.expander(f"{member['name']} · {member['email']}"):
            left, right = st.columns([1.2, 1])
            with left:
                st.write(f"Submitted: `{member['ts']}`")
                st.write(f"Budget: {member['budget']}")
                st.write(f"Availability: {member['availability']}")
                st.write(f"Activities: {member['activities']}")
                st.write(f"Intent: {member['intent']}")
                st.write(f"Cafe ideas: {member['cafe']}")
                st.write(f"Newsletter: {'Yes' if member['newsletter'] == 'yes' else 'No'}")
            with right:
                with st.form(f"member_admin_{member['id']}"):
                    new_status = st.selectbox(
                        "Status",
                        ["pending", "approved", "waitlist", "declined"],
                        index=["pending", "approved", "waitlist", "declined"].index(admin["status"]),
                        key=f"status_{member['id']}",
                    )
                    new_tier = st.selectbox(
                        "Tier",
                        ["fo", "ibp", "wi", "yhttb"],
                        index=["fo", "ibp", "wi", "yhttb"].index(admin["tier"]),
                        format_func=tier_label,
                        key=f"tier_{member['id']}",
                    )
                    fac_flag = st.checkbox("Flag as facilitator candidate", value=admin["fac"], key=f"fac_{member['id']}")
                    notes = st.text_area("Admin notes", value=admin["notes"], key=f"notes_{member['id']}")
                    if st.form_submit_button("Save member review", use_container_width=True):
                        data["admin"][member["id"]] = {
                            "status": new_status,
                            "tier": new_tier,
                            "notes": notes,
                            "fac": fac_flag,
                        }
                        persist()
                        st.success("Member updated.")


def render_planner() -> None:
    data = data_store()
    show_header("Planner", "Design and assign Nook experiences across tiers, venues, facilitators, and three-act flows.")
    with st.expander("Add new experience", expanded=False):
        with st.form("new_experience"):
            c1, c2, c3 = st.columns(3)
            name = c1.text_input("Experience name")
            tier = c2.selectbox("Tier", ["fo", "ibp", "wi", "yhttb"], format_func=tier_label)
            fac_map = {"Unassigned": ""}
            for fac in data["facs"]:
                if fac["status"] != "offboarded":
                    fac_map[fac["name"]] = fac["id"]
            fac_name = c3.selectbox("Facilitator", list(fac_map.keys()))
            d1, d2, d3, d4 = st.columns(4)
            exp_date = d1.date_input("Date", value=date.today())
            exp_time = d2.text_input("Time", value="18:00")
            capacity = d3.number_input("Max attendees", min_value=1, value=8)
            price = d4.number_input("Price per person", min_value=0, value=500)
            venue = st.text_input("Venue")
            act1 = st.text_area("Act 1 - Opener")
            act2 = st.text_area("Act 2 - Activity")
            act3 = st.text_area("Act 3 - Unwind")
            transport = st.text_input("Transport")
            notes = st.text_area("Notes / vibe")
            if st.form_submit_button("Save experience", use_container_width=True):
                if not name.strip():
                    st.error("Experience name is required.")
                else:
                    data["exps"].append(
                        {
                            "id": uuid4().hex[:8],
                            "name": name.strip(),
                            "tier": tier,
                            "date": exp_date.isoformat(),
                            "time": exp_time,
                            "max": int(capacity),
                            "price": int(price),
                            "venue": venue,
                            "fac": fac_map[fac_name],
                            "transport": transport,
                            "act1": act1,
                            "act2": act2,
                            "act3": act3,
                            "notes": notes,
                        }
                    )
                    persist()
                    st.success("Experience added.")
                    st.rerun()

    tier_filter = st.selectbox("Filter by tier", ["all", "fo", "ibp", "wi", "yhttb"], format_func=lambda x: "All tiers" if x == "all" else tier_label(x))
    exps = [e for e in data["exps"] if tier_filter == "all" or e["tier"] == tier_filter]
    for exp in exps:
        fac = get_fac(exp["fac"])
        with st.expander(f"{exp['name']} · {exp['date']}"):
            st.markdown(
                f"""
                <div class="session-card">
                  {tier_badge(exp["tier"])}
                  <span class="subtle">{exp["time"]} · {exp["venue"]} · Max {exp["max"]} · ₹{exp["price"]}</span><br>
                  <span class="subtle">Facilitator: {fac["name"] if fac else "Unassigned"}{' · On leave' if fac and on_leave(fac['id']) else ''}</span>
                </div>
                """,
                unsafe_allow_html=True,
            )
            st.write(f"Act 1: {exp['act1']}")
            st.write(f"Act 2: {exp['act2']}")
            st.write(f"Act 3: {exp['act3']}")
            if exp["notes"]:
                st.caption(exp["notes"])
            if st.button("Delete experience", key=f"del_exp_{exp['id']}"):
                data["exps"] = [e for e in data["exps"] if e["id"] != exp["id"]]
                persist()
                st.rerun()


def render_facilitator_team(user: Dict) -> None:
    data = data_store()
    if user["role"] != "founder":
        fac = get_fac(user["fac_id"])
        show_header("My Profile", "Your facilitator profile and operating access inside Nook.")
        if fac:
            st.markdown(
                f"""
                <div class="card">
                  <div class="eyebrow">Facilitator Profile</div>
                  <h3 style="margin-top:0">{fac['name']}</h3>
                  <div class="subtle">{fac['email']} · {fac['phone']}</div><br>
                  {status_badge(fac['status'])}
                  {pill_html(f"{tier_label(fac['access'])} access", tone="klein")}
                  {pill_html(f"{fac['refs']} referral slots", tone="citric")}
                  {pill_html(f"{fac['sessions']} sessions attended", tone="aqua")}
                  <p class="muted" style="margin-top:14px">{fac['notes']}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )
        return

    show_header("Facilitator Team", "Manage who is active, who is in onboarding, and who should only see the facilitator route.")
    candidates = [
        m for m in data["members"]
        if get_admin(m["id"])["fac"] and not any(f.get("member_id") == m["id"] for f in data["facs"])
    ]

    with st.expander("Add facilitator", expanded=False):
        with st.form("add_facilitator"):
            c1, c2 = st.columns(2)
            name = c1.text_input("Full name")
            uid = c2.text_input("Login ID", placeholder="name.fac")
            c3, c4 = st.columns(2)
            email = c3.text_input("Email")
            phone = c4.text_input("Phone")
            c5, c6, c7 = st.columns(3)
            password = c5.text_input("Password", value="nook123")
            status = c6.selectbox("Status", ["candidate", "active", "offboarded"])
            access = c7.selectbox("Tier access", ["fo", "ibp", "wi", "yhttb"], format_func=tier_label)
            refs = st.number_input("Referral slots", min_value=0, value=2)
            notes = st.text_area("Notes")
            if st.form_submit_button("Save facilitator", use_container_width=True):
                data["facs"].append(
                    {
                        "id": f"f{uuid4().hex[:5]}",
                        "name": name,
                        "uid": uid,
                        "password": password,
                        "email": email,
                        "phone": phone,
                        "status": status,
                        "access": access,
                        "refs": int(refs),
                        "sessions": 2,
                        "notes": notes,
                    }
                )
                persist()
                st.success("Facilitator added.")
                st.rerun()

    if candidates:
        st.markdown("### Flagged candidates")
        for member in candidates:
            st.markdown(f"- {member['name']} · {member['email']}")

    st.markdown("### Team")
    for fac in data["facs"]:
        with st.expander(f"{fac['name']} · {fac['status'].title()}"):
            st.markdown(status_badge(fac["status"]), unsafe_allow_html=True)
            st.write(f"Login: `{fac['uid']}`")
            st.write(f"Email: {fac['email']}")
            st.write(f"Phone: {fac['phone']}")
            st.write(f"Tier access: {tier_label(fac['access'])}")
            st.write(f"Referral slots: {fac['refs']}")
            st.write(f"On leave today: {'Yes' if on_leave(fac['id']) else 'No'}")
            new_status = st.selectbox("Update status", ["candidate", "active", "offboarded"], index=["candidate", "active", "offboarded"].index(fac["status"]), key=f"fac_status_{fac['id']}")
            new_notes = st.text_area("Notes", value=fac["notes"], key=f"fac_notes_{fac['id']}")
            left, right = st.columns(2)
            if left.button("Save facilitator", key=f"save_fac_{fac['id']}"):
                fac["status"] = new_status
                fac["notes"] = new_notes
                persist()
                st.success("Facilitator updated.")
                st.rerun()
            if right.button("Offboard", key=f"off_fac_{fac['id']}"):
                fac["status"] = "offboarded"
                persist()
                st.warning("Facilitator offboarded.")
                st.rerun()


def render_leave() -> None:
    data = data_store()
    show_header("Leave & Availability", "See who is available for sessions right now and capture leave history in one place.")
    with st.expander("Mark leave", expanded=False):
        active_facs = [f for f in data["facs"] if f["status"] != "offboarded"]
        fac_names = {f["name"]: f["id"] for f in active_facs}
        with st.form("leave_form"):
            fac_name = st.selectbox("Facilitator", list(fac_names.keys()))
            c1, c2 = st.columns(2)
            from_dt = c1.date_input("From", value=date.today())
            to_dt = c2.date_input("To", value=date.today())
            reason = st.selectbox("Reason", ["Personal leave", "Travel", "Unavailable this weekend", "Health", "Other"])
            notes = st.text_area("Notes")
            if st.form_submit_button("Save leave", use_container_width=True):
                data["leaves"].append(
                    {
                        "id": uuid4().hex[:8],
                        "fid": fac_names[fac_name],
                        "from": from_dt.isoformat(),
                        "to": to_dt.isoformat(),
                        "reason": reason,
                        "notes": notes,
                    }
                )
                persist()
                st.success("Leave saved.")
                st.rerun()
    st.markdown("### Availability today")
    for fac in data["facs"]:
        if fac["status"] == "offboarded":
            continue
        st.markdown(
            f"""
            <div class="card">
              <strong>{fac['name']}</strong><br>
              <span class="subtle">{'On leave' if on_leave(fac['id']) else 'Available for sessions'}</span><br><br>
              {status_badge('offboarded' if fac['status']=='offboarded' else ('candidate' if fac['status']=='candidate' else 'active'))}
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("### Leave history")
    for leave in data["leaves"]:
        fac = get_fac(leave["fid"])
        cols = st.columns([4, 2, 2, 2, 1])
        cols[0].write(fac["name"] if fac else "Unknown")
        cols[1].write(leave["from"])
        cols[2].write(leave["to"])
        cols[3].write(leave["reason"])
        if cols[4].button("Remove", key=f"rm_leave_{leave['id']}"):
            data["leaves"] = [l for l in data["leaves"] if l["id"] != leave["id"]]
            persist()
            st.rerun()


def render_my_sessions(user: Dict) -> None:
    show_header("My Sessions", "Assigned session details for the facilitator route, including the three-act flow and notes.")
    my_sessions = [e for e in data_store()["exps"] if e["fac"] == user["fac_id"]]
    if not my_sessions:
        st.info("No sessions assigned to you yet.")
        return
    for exp in my_sessions:
        st.markdown(
            f"""
            <div class="session-card">
              {tier_badge(exp["tier"])}
              <strong>{exp["name"]}</strong><br>
              <span class="subtle">{exp["date"]} · {exp["time"]} · {exp["venue"]} · ₹{exp["price"]}/person</span><br><br>
              <div class="subtle"><strong>Act 1:</strong> {exp["act1"]}</div>
              <div class="subtle"><strong>Act 2:</strong> {exp["act2"]}</div>
              <div class="subtle"><strong>Act 3:</strong> {exp["act3"]}</div>
              <div class="subtle" style="margin-top:10px"><strong>Transport:</strong> {exp["transport"] or 'Not specified'}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )


def render_messages(user: Dict) -> None:
    data = data_store()
    show_header("Messages", "Team communication between founder and facilitators, stored locally inside this prototype.")
    for msg in data["msgs"]:
        if msg["to"] == user["id"]:
            msg["read"] = True
    persist()

    all_users = [{"id": u["id"], "name": u["name"]} for u in USERS]
    recipient_options = {u["name"]: u["id"] for u in all_users if u["id"] != user["id"]}

    with st.expander("Send a new message", expanded=False):
        with st.form("new_message"):
            recipient = st.selectbox("To", list(recipient_options.keys()))
            subject = st.selectbox("Message type", ["General update", "Session reminder", "Request information from member", "Post-session update"])
            body = st.text_area("Message")
            if st.form_submit_button("Send", use_container_width=True):
                if body.strip():
                    data["msgs"].append(
                        {
                            "id": uuid4().hex[:8],
                            "from": user["id"],
                            "to": recipient_options[recipient],
                            "subject": subject,
                            "body": body.strip(),
                            "ts": datetime.now().strftime("%Y-%m-%d %H:%M"),
                            "read": False,
                        }
                    )
                    persist()
                    st.success("Message sent.")
                    st.rerun()
                st.error("Write a message first.")

    inbox = [m for m in data["msgs"] if m["to"] == user["id"] or m["from"] == user["id"]]
    inbox.sort(key=lambda m: m["ts"], reverse=True)
    for msg in inbox:
        from_name = next((u["name"] for u in USERS if u["id"] == msg["from"]), msg["from"])
        to_name = next((u["name"] for u in USERS if u["id"] == msg["to"]), msg["to"])
        st.markdown(
            f"""
            <div class="card">
              <strong>{msg["subject"]}</strong><br>
              <span class="subtle">From: {from_name} · To: {to_name} · {msg["ts"]}</span>
              <p style="margin-bottom:0">{msg["body"]}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )


def render_docs() -> None:
    show_header("Docs", "How this Streamlit version of the Nook control room is structured.")
    st.markdown(
        """
        <div class="card">
          <div class="eyebrow">What changed from the HTML version</div>
          <p class="muted">
            This version is now a Streamlit app with role-based login, founder and facilitator routes,
            local JSON persistence, experience planning, facilitator management, leave tracking, member review,
            and internal messaging. It keeps the original control-room concept but expresses it in Python.
          </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("### Notes")
    st.write("- Data is stored locally in `nook_data.json`.")
    st.write("- Founder login is `manju / founder2026`.")
    st.write("- Facilitator logins match the seeded accounts from the original HTML.")
    st.write("- This is a strong prototype base; real production auth should move to a backend and database.")


def main() -> None:
    st.set_page_config(page_title="Nook Control Room", page_icon="N", layout="wide", initial_sidebar_state="expanded")
    if current_user() is None:
        login_screen()
        return

    inject_css()
    user = current_user()
    page = sidebar_navigation(user)

    if page == "Dashboard":
        render_dashboard(user)
    elif page == "Members":
        render_members()
    elif page == "Planner":
        render_planner()
    elif page == "Facilitator Team":
        render_facilitator_team(user)
    elif page == "My Profile":
        render_facilitator_team(user)
    elif page == "Leave":
        render_leave()
    elif page == "My Sessions":
        render_my_sessions(user)
    elif page == "Messages":
        render_messages(user)
    elif page == "Docs":
        render_docs()


if __name__ == "__main__":
    main()
