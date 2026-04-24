import json
from copy import deepcopy
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional
from uuid import uuid4

import streamlit as st


APP_DIR = Path(__file__).resolve().parent
DATA_FILE = APP_DIR / "nook_data.json"

FRAME_RED = "#D85C1A"
PAPER = "#F2E7D8"
PAPER_ALT = "#FBF4EC"
INK = "#11100E"
SOFT_INK = "#6A5D52"
LINE = "#D7BDA0"
KLEIN_BLUE = "#11100E"
CITRIC = "#E8D7C2"
AQUAMARINE = "#F7EEE3"
FUCHSIA = "#B14B1C"
TANGERINE = "#D85C1A"
NOOK_BLACK = "#11100E"
ORANGE = TANGERINE
BG = FRAME_RED
SURFACE = PAPER_ALT
SURFACE_ALT = "#FFFDF8"
BORDER = "rgba(17,16,14,0.10)"
TEXT = INK
MUTED = SOFT_INK

FOUNDER_ACCOUNT = {"id": "manju", "name": "Manju Singh", "role": "founder", "password": "founder2026"}

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
    seed = build_large_demo_seed()
    return {
        "members": deepcopy(seed["members"]),
        "facs": deepcopy(DEMO_FACS),
        "exps": deepcopy(DEMO_EXPERIENCES),
        "leaves": deepcopy(DEMO_LEAVES),
        "msgs": deepcopy(DEMO_MESSAGES),
        "payments": deepcopy(seed["payments"]),
        "admin": deepcopy(seed["admin"]),
        "referrals": deepcopy(seed["referrals"]),
        "private_entries": deepcopy(seed["private_entries"]),
        "settings": {
            "razorpay_key_id": "",
            "razorpay_key_secret": "",
            "payment_link_base": "",
            "preferred_ai_api": "OpenAI or Groq",
            "ops_note": "",
        },
    }


def load_data() -> Dict:
    if DATA_FILE.exists():
        try:
            raw = json.loads(DATA_FILE.read_text(encoding="utf-8"))
            return hydrate_data(raw)
        except json.JSONDecodeError:
            pass
    data = default_data()
    save_data(data)
    return data


def save_data(data: Dict) -> None:
    DATA_FILE.write_text(json.dumps(data, indent=2), encoding="utf-8")


def hydrate_data(raw: Dict) -> Dict:
    data = default_data()
    for key, value in raw.items():
        if key not in data:
            data[key] = value
            continue
        if isinstance(data[key], dict) and isinstance(value, dict):
            data[key].update(value)
        elif isinstance(data[key], list) and isinstance(value, list):
            data[key] = value
        else:
            data[key] = value
    if len(data["members"]) < 40:
        seed = build_large_demo_seed()
        data["members"] = deepcopy(seed["members"])
        data["admin"] = deepcopy(seed["admin"])
        data["referrals"] = deepcopy(seed["referrals"])
        if len(data["payments"]) < 8:
            data["payments"] = deepcopy(seed["payments"])
    if "private_entries" not in data or not data["private_entries"]:
        data["private_entries"] = deepcopy(build_large_demo_seed()["private_entries"])
    if "settings" not in data:
        data["settings"] = default_data()["settings"]
    return data


def auto_tier(sessions: int) -> str:
    if sessions >= 5:
        return "yhttb"
    if sessions >= 3:
        return "wi"
    if sessions >= 2:
        return "ibp"
    return "fo"


def build_large_demo_seed() -> Dict[str, object]:
    names = [
        "Aditi Rao", "Kabir Sethi", "Naina Joseph", "Rahul Jain", "Ira Sharma", "Vihaan Kapoor", "Mahi Menon", "Arjun Batra",
        "Samaira Das", "Laksh Malhotra", "Tanya Ghosh", "Raghav Khanna", "Ananya Sen", "Harshita Mehra", "Yash Vora", "Sana Rizvi",
        "Pranav Iyer", "Kashish Bedi", "Devika Nair", "Aman Arora", "Ishita Bose", "Neel Chawla", "Ritika Dutta", "Aarav Grover",
        "Suhani Bansal", "Manan Tiwari", "Rhea Thomas", "Kunal Roy", "Pihu Oberoi", "Darsh Patel", "Niharika Ahuja", "Eshan Mathur",
        "Zoya Mirza", "Ritvik Soni", "Myra Kamat", "Siddhant Kohli", "Ishaan Lamba", "Prisha Anand", "Tara Chhabra", "Rohan Kulkarni",
    ]
    budgets = ["Rs 500-800", "Rs 800-1200", "Rs 1200+", "Rs 700-1000"]
    availability = ["Friday evening", "Saturday evening", "Sunday brunch", "Weekday evening", "Weekend only"]
    activities = [
        "art nights, long conversations, cafe hopping",
        "slow dinners, storytelling, walks",
        "pottery, sketching, coffee tastings",
        "board games, city walks, music listening",
        "quiet brunches, journaling, shared making",
    ]
    intents = [
        "Looking for a warm third place with thoughtful people and better conversation.",
        "I want curated social plans without loud networking energy.",
        "Would love a smaller room where I can meet people gradually and come back often.",
        "Searching for a community that feels aesthetic, calm, and emotionally safe.",
        "I want something intentional instead of generic event-company vibes.",
    ]
    cafes = ["Leafy rooftop cafe", "Ceramic studio", "Old city walk route", "Minimal coffee bar", "Hidden supper spot"]
    messages = [
        "Happy to start with a simple beginner session.",
        "I can also be considered for premium experiences later.",
        "Usually more comfortable in smaller groups.",
        "Would love something creative or conversation-first.",
        "Open to being on the waitlist if it is a good fit.",
    ]
    members: List[Dict] = []
    admin: Dict[str, Dict] = {}
    for idx, name in enumerate(names, start=1):
        first = name.split(" ")[0].lower()
        member_id = f"m{idx:02d}"
        sessions = idx % 6
        source = "referral" if idx % 5 == 0 else "organic"
        members.append(
            {
                "id": member_id,
                "name": name,
                "email": f"{first}{idx}@example.com",
                "phone": f"98765{idx:05d}",
                "budget": budgets[idx % len(budgets)],
                "availability": availability[idx % len(availability)],
                "activities": activities[idx % len(activities)],
                "intent": intents[idx % len(intents)],
                "cafe": cafes[idx % len(cafes)],
                "message": messages[idx % len(messages)],
                "newsletter": "yes" if idx % 3 else "no",
                "sessions": sessions,
                "ts": f"2026-04-{(idx % 28) + 1:02d} {10 + (idx % 9):02d}:{(idx * 7) % 60:02d}",
                "source": source,
                "referred_by": ["riya.fac", "sneha.fac", "priya.fac"][idx % 3] if source == "referral" else "",
            }
        )
        if idx <= 12:
            status = "approved"
        elif idx <= 28:
            status = "pending"
        elif idx <= 36:
            status = "waitlist"
        else:
            status = "declined"
        admin[member_id] = {
            "status": status,
            "tier": auto_tier(sessions),
            "notes": "Strong demo lead." if idx % 4 == 0 else "",
            "fac": idx in {3, 8, 14, 22, 31},
        }

    referrals = []
    referral_targets = [member for member in members if member["source"] == "referral"][:9]
    for idx, member in enumerate(referral_targets, start=1):
        status = ["pending", "approved", "waitlist"][idx % 3]
        if idx in {2, 5}:
            status = "rejected"
        referrals.append(
            {
                "id": f"r{idx:02d}",
                "fac_id": member["referred_by"] or "riya.fac",
                "member_id": member["id"],
                "candidate_name": member["name"],
                "email": member["email"],
                "phone": member["phone"],
                "experience_name": ["Canvas Night", "Secret Supper Walk", "Pottery & Pour Over"][idx % 3],
                "reason": "Feels like a strong aesthetic and community fit for Nook.",
                "created_at": f"2026-04-{(idx * 2) + 2:02d} 18:00",
                "month": "2026-04",
                "status": status,
                "founder_note": "High-trust referral." if status == "approved" else "",
            }
        )

    private_entries = [
        {
            "id": "n1",
            "owner_id": "manju",
            "title": "Founder reminders",
            "body": "Revisit Friday applications, confirm next month's premium calendar, and tighten referral review cadence.",
            "kind": "note",
            "created_at": "2026-04-23 09:10",
        },
        {
            "id": "n2",
            "owner_id": "riya.fac",
            "title": "Session read",
            "body": "Aditi and Tara opened up after Act 2. Keep pairing introverts with hands-on moments.",
            "kind": "update",
            "created_at": "2026-04-23 22:10",
        },
        {
            "id": "n3",
            "owner_id": "sneha.fac",
            "title": "Venue note",
            "body": "Clay House works best when we keep the opener standing, not seated.",
            "kind": "note",
            "created_at": "2026-04-22 18:45",
        },
        {
            "id": "n4",
            "owner_id": "priya.fac",
            "title": "Referral watch",
            "body": "Two of my April referrals feel premium-tier ready if approved.",
            "kind": "update",
            "created_at": "2026-04-21 16:20",
        },
    ]

    payments = [
        {"id": "p01", "member_id": "m01", "label": "Worth It monthly", "amount": 1499, "status": "paid", "method": "UPI"},
        {"id": "p02", "member_id": "m03", "label": "YHTTB monthly", "amount": 2499, "status": "paid", "method": "Card"},
        {"id": "p03", "member_id": "m05", "label": "First Out trial", "amount": 499, "status": "pending", "method": "Razorpay link"},
        {"id": "p04", "member_id": "m08", "label": "Worth It monthly", "amount": 1499, "status": "paid", "method": "Razorpay link"},
        {"id": "p05", "member_id": "m11", "label": "IBP monthly", "amount": 999, "status": "pending", "method": "UPI"},
        {"id": "p06", "member_id": "m14", "label": "YHTTB monthly", "amount": 2499, "status": "paid", "method": "Netbanking"},
        {"id": "p07", "member_id": "m18", "label": "First Out trial", "amount": 499, "status": "pending", "method": "Razorpay link"},
        {"id": "p08", "member_id": "m23", "label": "Worth It monthly", "amount": 1499, "status": "paid", "method": "UPI"},
        {"id": "p09", "member_id": "m29", "label": "IBP monthly", "amount": 999, "status": "pending", "method": "Razorpay link"},
        {"id": "p10", "member_id": "m31", "label": "Worth It monthly", "amount": 1499, "status": "paid", "method": "Card"},
    ]

    return {
        "members": members,
        "admin": admin,
        "referrals": referrals,
        "private_entries": private_entries,
        "payments": payments,
    }


def tier_label(code: str) -> str:
    return {
        "fo": "First Out",
        "ibp": "In Between Plans",
        "wi": "Worth It",
        "yhttb": "YHTTB",
    }.get(code, code.upper())


def status_badge(status: str) -> str:
    styles = {
        "pending": (CITRIC, NOOK_BLACK, "rgba(216,92,26,0.22)"),
        "approved": (AQUAMARINE, NOOK_BLACK, "rgba(17,16,14,0.12)"),
        "declined": (TANGERINE, PAPER_ALT, "rgba(216,92,26,0.28)"),
        "waitlist": (FUCHSIA, PAPER_ALT, "rgba(17,16,14,0.10)"),
        "active": (AQUAMARINE, NOOK_BLACK, "rgba(17,16,14,0.12)"),
        "candidate": (CITRIC, NOOK_BLACK, "rgba(216,92,26,0.22)"),
        "offboarded": (NOOK_BLACK, PAPER_ALT, "rgba(17,16,14,0.16)"),
    }
    bg, fg, border = styles.get(status, (TANGERINE, PAPER_ALT, "rgba(216,92,26,0.28)"))
    return (
        f"<span style='padding:4px 10px;border-radius:999px;"
        f"background:{bg};color:{fg};border:1px solid {border};"
        f"font-size:12px;font-weight:700;letter-spacing:0.02em'>{status.title()}</span>"
    )


def pill_html(text: str, tone: str = "aqua") -> str:
    tone_map = {
        "klein": (NOOK_BLACK, PAPER_ALT, "rgba(17,16,14,0.18)"),
        "citric": (CITRIC, NOOK_BLACK, "rgba(216,92,26,0.18)"),
        "aqua": (AQUAMARINE, NOOK_BLACK, "rgba(17,16,14,0.12)"),
        "fuchsia": (FUCHSIA, PAPER_ALT, "rgba(17,16,14,0.10)"),
        "tangerine": (TANGERINE, PAPER_ALT, "rgba(216,92,26,0.22)"),
        "black": (NOOK_BLACK, PAPER_ALT, "rgba(17,16,14,0.18)"),
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


def render_stat_strip(items: List[Dict]) -> None:
    html = "<div class='stat-strip'>"
    for item in items:
        html += (
            "<div class='stat-cell'>"
            f"<div class='stat-line' style='background:{item.get('accent', FRAME_RED)}'></div>"
            f"<div class='stat-value'>{item['value']}</div>"
            f"<div class='stat-label'>{item['label']}</div>"
            f"<div class='stat-note'>{item.get('note', '')}</div>"
            "</div>"
        )
    html += "</div>"
    st.markdown(html, unsafe_allow_html=True)


def insight_card_html(title: str, detail: str, tone: str = "tangerine") -> str:
    return (
        "<div class='insight-card'>"
        f"{pill_html(title, tone=tone)}"
        f"<p>{detail}</p>"
        "</div>"
    )


def editorial_card(title: str, body: str, eyebrow: Optional[str] = None) -> str:
    eyebrow_html = f"<div class='eyebrow'>{eyebrow}</div>" if eyebrow else ""
    return (
        "<div class='card editorial-card'>"
        f"{eyebrow_html}"
        f"<h3>{title}</h3>"
        f"<p>{body}</p>"
        "</div>"
    )


def current_user() -> Optional[Dict]:
    return st.session_state.get("current_user")


def data_store() -> Dict:
    if "data" not in st.session_state:
        st.session_state.data = load_data()
    return st.session_state.data


def persist() -> None:
    st.session_state.data = hydrate_data(st.session_state.data)
    save_data(st.session_state.data)


def all_accounts(data: Optional[Dict] = None) -> List[Dict]:
    data = data or (st.session_state.get("data") if "data" in st.session_state else load_data())
    facilitator_accounts = []
    for fac in data["facs"]:
        if fac.get("uid") and fac.get("password") and fac.get("status") != "offboarded":
            facilitator_accounts.append(
                {
                    "id": fac["uid"],
                    "name": fac["name"],
                    "role": "facilitator",
                    "password": fac["password"],
                    "fac_id": fac["id"],
                }
            )
    return [FOUNDER_ACCOUNT, *facilitator_accounts]


def resolve_account(user_id: str) -> Optional[Dict]:
    return next((account for account in all_accounts() if account["id"] == user_id), None)


def resolve_user_name(user_id: str) -> str:
    account = resolve_account(user_id)
    return account["name"] if account else user_id


def parse_iso_day(raw: str) -> date:
    return datetime.strptime(raw, "%Y-%m-%d").date()


def upcoming_experiences(limit: Optional[int] = None) -> List[Dict]:
    items = sorted(data_store()["exps"], key=lambda exp: (exp.get("date", "9999-12-31"), exp.get("time", "23:59")))
    return items[:limit] if limit else items


def tier_rank(code: str) -> int:
    return {"fo": 1, "ibp": 2, "wi": 3, "yhttb": 4}.get(code, 0)


def format_money(amount: int) -> str:
    return f"Rs {amount:,}"


def facilitator_session_load(fid: str) -> int:
    return sum(1 for exp in data_store()["exps"] if exp.get("fac") == fid)


def smart_member_score(member: Dict) -> int:
    admin = get_admin(member["id"])
    text_blob = " ".join(
        [
            member.get("intent", "").lower(),
            member.get("activities", "").lower(),
            member.get("message", "").lower(),
            member.get("availability", "").lower(),
        ]
    )
    score = 32
    score += min(member.get("sessions", 0) * 9, 32)
    score += 10 if member.get("newsletter") == "yes" else 0
    score += 8 if any(word in text_blob for word in ["community", "thoughtful", "third place", "warm", "conversation"]) else 0
    score += 6 if any(word in text_blob for word in ["weekend", "friday", "saturday"]) else 0
    score += 8 if "1200" in member.get("budget", "") or "+" in member.get("budget", "") else 0
    score += 7 if admin["fac"] else 0
    score += 6 if admin["status"] == "approved" else 0
    return max(0, min(score, 100))


def smart_member_recommendation(member: Dict) -> Dict:
    admin = get_admin(member["id"])
    score = smart_member_score(member)
    if admin["fac"] and member.get("sessions", 0) >= 4:
        return {"label": "Onboard as facilitator candidate", "tone": "fuchsia"}
    if score >= 72 and admin["status"] in {"pending", "waitlist"}:
        return {"label": "Approve soon", "tone": "citric"}
    if score >= 55:
        return {"label": "Warm lead", "tone": "aqua"}
    return {"label": "Needs review", "tone": "tangerine"}


def recommended_facilitator(exp: Dict) -> Optional[Dict]:
    candidates = []
    for fac in data_store()["facs"]:
        if fac["status"] != "active":
            continue
        if on_leave(fac["id"]):
            continue
        access_gap = tier_rank(fac.get("access", "fo")) - tier_rank(exp.get("tier", "fo"))
        if access_gap < 0:
            continue
        load_penalty = facilitator_session_load(fac["id"]) * 4
        experience_bonus = min(fac.get("sessions", 0), 12)
        score = 70 + experience_bonus + (6 - access_gap * 2) - load_penalty
        candidates.append((score, fac))
    candidates.sort(key=lambda item: item[0], reverse=True)
    return candidates[0][1] if candidates else None


def smart_operational_alerts(user: Dict) -> List[Dict]:
    if user["role"] != "founder":
        fac = get_fac(user["fac_id"]) or {}
        alerts = []
        if on_leave(user["fac_id"]):
            alerts.append({"title": "You are currently marked on leave", "detail": "Update your availability if this changed.", "tone": "tangerine"})
        my_sessions = [exp for exp in upcoming_experiences() if exp.get("fac") == user["fac_id"]]
        if my_sessions:
            next_session = my_sessions[0]
            alerts.append(
                {
                    "title": f"Next session: {next_session['name']}",
                    "detail": f"{next_session['date']} at {next_session['time']} · {next_session['venue']}",
                    "tone": "aqua",
                }
            )
        unread = sum(1 for msg in data_store()["msgs"] if msg["to"] == user["id"] and not msg["read"])
        if unread:
            alerts.append({"title": f"{unread} unread message(s)", "detail": "Check Messages for founder notes and reminders.", "tone": "citric"})
        if fac.get("status") == "candidate":
            alerts.append({"title": "You are still in candidate mode", "detail": "Your access stays limited until founder review is complete.", "tone": "fuchsia"})
        return alerts[:3]

    alerts = []
    data = data_store()
    unread = sum(1 for msg in data["msgs"] if msg["to"] == "manju" and not msg["read"])
    if unread:
        alerts.append({"title": f"{unread} unread facilitator update(s)", "detail": "There are team messages waiting in the founder inbox.", "tone": "klein"})
    flagged_candidates = [member for member in data["members"] if get_admin(member["id"])["fac"]]
    if flagged_candidates:
        alerts.append({"title": f"{len(flagged_candidates)} facilitator candidate(s)", "detail": "Promising members are ready for onboarding review.", "tone": "fuchsia"})
    for exp in upcoming_experiences(limit=5):
        if not exp.get("fac"):
            alerts.append({"title": f"{exp['name']} has no facilitator", "detail": "Assign an active facilitator before the session goes live.", "tone": "tangerine"})
        elif on_leave(exp["fac"]):
            fac = get_fac(exp["fac"])
            fac_name = fac["name"] if fac else "Assigned facilitator"
            alerts.append({"title": f"{fac_name} is on leave", "detail": f"Reassign {exp['name']} or update leave dates.", "tone": "tangerine"})
    stale_pending = [
        member
        for member in data["members"]
        if get_admin(member["id"])["status"] == "pending"
        and datetime.now() - datetime.strptime(member["ts"], "%Y-%m-%d %H:%M") > timedelta(days=5)
    ]
    if stale_pending:
        alerts.append({"title": f"{len(stale_pending)} pending lead(s) are aging", "detail": "Those members have waited more than five days for a decision.", "tone": "citric"})
    return alerts[:4]


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
    for user in all_accounts():
        if user["id"] == username and user["password"] == password:
            return user
    return None


def inject_css() -> None:
    st.markdown(
        f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;700&family=Syne:wght@700;800&display=swap');
        :root {{
            --frame-red: {FRAME_RED};
            --paper: {PAPER};
            --paper-alt: {PAPER_ALT};
            --ink: {INK};
            --soft-ink: {SOFT_INK};
            --line: {LINE};
            --klein-blue: {KLEIN_BLUE};
            --citric: {CITRIC};
            --aquamarine: {AQUAMARINE};
            --fuchsia: {FUCHSIA};
            --tangerine: {TANGERINE};
            --cream: #fff7ef;
            --glow: rgba(216,92,26,0.24);
            --glow-strong: rgba(216,92,26,0.42);
            --shadow-soft: 0 22px 55px rgba(17,16,14,0.12);
            --shadow-float: 0 36px 90px rgba(17,16,14,0.22);
            --radius-lg: 24px;
            --radius-xl: 34px;
        }}
        html, body, [class*="css"] {{
            font-family: "Space Grotesk", sans-serif;
        }}
        html {{
            scroll-behavior: smooth;
        }}
        body {{
            background:
                radial-gradient(circle at 18% 4%, rgba(255,173,113,0.35), transparent 16%),
                radial-gradient(circle at 86% 10%, rgba(216,92,26,0.22), transparent 18%),
                linear-gradient(180deg, #1c1712 0%, #2a2119 13%, #ead4bb 30%, #f2e7d8 100%);
        }}
        .stApp {{
            background:
                radial-gradient(circle at 18% 0%, rgba(255,165,92,0.28), transparent 18%),
                radial-gradient(circle at 88% 14%, rgba(216,92,26,0.18), transparent 22%),
                linear-gradient(180deg, #1c1712 0%, #2a2119 13%, #ead4bb 30%, #f2e7d8 100%);
            color: var(--ink);
        }}
        [data-testid="stAppViewContainer"] {{
            background: transparent;
        }}
        [data-testid="stAppViewContainer"]::before {{
            content: "";
            position: fixed;
            inset: 0;
            pointer-events: none;
            background:
                linear-gradient(rgba(255,255,255,0.05) 1px, transparent 1px),
                linear-gradient(90deg, rgba(255,255,255,0.05) 1px, transparent 1px);
            background-size: 34px 34px;
            mask-image: linear-gradient(180deg, rgba(0,0,0,0.55), transparent 36%, rgba(0,0,0,0.18));
            opacity: 0.18;
            z-index: 0;
        }}
        .block-container {{
            max-width: 1220px;
            margin: 24px auto 54px auto;
            padding: 30px 36px 54px 36px;
            background:
                linear-gradient(180deg, rgba(255,250,244,0.90), rgba(242,231,216,0.98)),
                linear-gradient(135deg, rgba(255,255,255,0.75), rgba(255,255,255,0.30));
            border: 1px solid rgba(17,16,14,0.08);
            border-radius: var(--radius-xl);
            box-shadow: var(--shadow-float);
            position: relative;
            overflow: hidden;
        }}
        .block-container::before {{
            content: "";
            position: absolute;
            inset: 0;
            pointer-events: none;
            background:
                radial-gradient(circle at 84% 8%, rgba(255,189,133,0.35), transparent 22%),
                radial-gradient(circle at 8% 0%, rgba(216,92,26,0.16), transparent 22%),
                linear-gradient(180deg, rgba(255,255,255,0.32), transparent 26%);
        }}
        .block-container > * {{
            position: relative;
            z-index: 1;
        }}
        [data-testid="stSidebar"] {{
            background:
                radial-gradient(circle at 18% 0%, rgba(216,92,26,0.24), transparent 20%),
                linear-gradient(180deg, #0f0d0b 0%, #17120f 56%, #211912 100%);
            border-right: 1px solid rgba(255,255,255,0.05);
            box-shadow: 18px 0 48px rgba(0,0,0,0.18);
        }}
        [data-testid="stSidebar"]::before {{
            content: "";
            position: absolute;
            inset: 0;
            pointer-events: none;
            background:
                linear-gradient(rgba(255,255,255,0.04) 1px, transparent 1px),
                linear-gradient(90deg, rgba(255,255,255,0.03) 1px, transparent 1px);
            background-size: 28px 28px;
            opacity: 0.45;
        }}
        [data-testid="stSidebar"] * {{
            color: #f8eadc !important;
        }}
        [data-testid="stSidebar"] .block-container {{
            margin: 0;
            padding: 22px 18px 24px 18px;
            background: transparent;
            border: none;
            box-shadow: none;
        }}
        [data-testid="stMetric"] {{
            background:
                linear-gradient(180deg, rgba(255,250,245,0.98), rgba(247,238,227,0.96));
            border: 1px solid rgba(17,16,14,0.08);
            padding: 16px;
            border-radius: 26px;
            box-shadow: var(--shadow-soft);
            overflow: hidden;
            position: relative;
        }}
        [data-testid="stMetric"]::after {{
            content: "";
            position: absolute;
            inset: auto -24px -24px auto;
            width: 96px;
            height: 96px;
            background: radial-gradient(circle, rgba(216,92,26,0.22), transparent 70%);
            filter: blur(8px);
        }}
        [data-testid="stMetricLabel"],
        [data-testid="stMetricValue"],
        [data-testid="stMetricDelta"] {{
            color: var(--ink) !important;
        }}
        h1, h2, h3, h4 {{
            font-family: "Syne", "Space Grotesk", sans-serif;
            color: var(--ink);
            letter-spacing: -0.05em;
        }}
        h1, h2, h3, p, li, label, .stMarkdown, .stCaption, .stAlert {{
            color: var(--ink);
        }}
        .stMarkdown a {{
            color: var(--frame-red);
            text-decoration: none;
        }}
        div[data-baseweb="input"] > div,
        div[data-baseweb="select"] > div,
        div[data-baseweb="textarea"] > div,
        .stTextInput input,
        .stTextArea textarea,
        .stDateInput input,
        .stNumberInput input {{
            background: rgba(255,248,241,0.94);
            color: var(--ink);
            border: 1px solid rgba(17,16,14,0.10);
            border-radius: 18px;
            box-shadow: inset 0 1px 0 rgba(255,255,255,0.72);
        }}
        div[data-baseweb="input"] input,
        div[data-baseweb="select"] * ,
        div[data-baseweb="textarea"] textarea,
        .stDateInput * ,
        .stNumberInput input {{
            color: var(--ink) !important;
        }}
        div[data-baseweb="select"] > div,
        div[data-baseweb="input"] > div,
        div[data-baseweb="textarea"] > div {{
            background: rgba(255,248,241,0.94);
            border-radius: 18px;
        }}
        .stTextInput label,
        .stTextArea label,
        .stDateInput label,
        .stSelectbox label,
        .stNumberInput label {{
            color: var(--ink) !important;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            font-size: 11px;
        }}
        .stButton > button,
        .stForm [data-testid="stFormSubmitButton"] > button {{
            border-radius: 999px;
            border: 1px solid rgba(17,16,14,0.10);
            min-height: 2.9rem;
            font-weight: 700;
            letter-spacing: 0.08em;
            text-transform: uppercase;
            transition: transform 0.18s ease, box-shadow 0.18s ease, border-color 0.18s ease, background 0.18s ease;
        }}
        .stButton > button[kind="primary"],
        .stForm [data-testid="stFormSubmitButton"] > button[kind="primary"] {{
            background: linear-gradient(135deg, #ffb77d 0%, #f08a44 34%, #d85c1a 100%);
            color: #150f0c;
            border-color: rgba(216,92,26,0.42);
            box-shadow: 0 14px 30px rgba(216,92,26,0.24);
        }}
        .stButton > button[kind="secondary"],
        .stForm [data-testid="stFormSubmitButton"] > button[kind="secondary"] {{
            background: rgba(255,248,241,0.74);
            color: var(--ink);
            border-color: rgba(17,16,14,0.08);
            box-shadow: 0 8px 24px rgba(17,16,14,0.06);
        }}
        .stButton > button:hover,
        .stForm [data-testid="stFormSubmitButton"] > button:hover {{
            border-color: var(--frame-red);
            color: var(--ink);
            transform: translateY(-1px);
            box-shadow: 0 16px 32px rgba(17,16,14,0.10);
        }}
        [data-testid="stSidebar"] .stButton > button {{
            background: rgba(255,255,255,0.05);
            border-color: rgba(255,255,255,0.10);
            color: #f8eadc;
            box-shadow: none;
        }}
        [data-testid="stSidebar"] .stButton > button[kind="primary"] {{
            background: linear-gradient(135deg, #ffc891 0%, #f08a44 40%, #d85c1a 100%);
            color: #110f0d !important;
            border-color: rgba(255,173,113,0.34);
            box-shadow: 0 14px 32px rgba(216,92,26,0.24);
        }}
        [data-testid="stSidebar"] .stButton > button[kind="secondary"]:hover {{
            background: rgba(255,166,92,0.12);
            border-color: rgba(255,193,141,0.28);
            color: #fff2e7 !important;
        }}
        .stExpander {{
            background: linear-gradient(180deg, rgba(255,250,245,0.97), rgba(247,238,227,0.95));
            border: 1px solid rgba(17,16,14,0.08);
            border-radius: 24px;
            overflow: hidden;
            box-shadow: var(--shadow-soft);
        }}
        .stExpander details summary p {{
            color: var(--ink) !important;
            font-weight: 600;
        }}
        .card {{
            background: linear-gradient(180deg, rgba(255,250,245,0.98), rgba(247,238,227,0.95));
            border: 1px solid rgba(17,16,14,0.08);
            padding: 22px;
            margin-bottom: 18px;
            box-shadow: var(--shadow-soft);
            border-radius: 28px;
            position: relative;
            overflow: hidden;
            transition: transform 0.18s ease, box-shadow 0.18s ease;
        }}
        .card::after,
        .queue-card::after,
        .session-card::after,
        .insight-card::after {{
            content: "";
            position: absolute;
            top: -26px;
            right: -18px;
            width: 110px;
            height: 110px;
            background: radial-gradient(circle, rgba(255,186,126,0.34), transparent 70%);
            pointer-events: none;
        }}
        .card:hover,
        .queue-card:hover,
        .session-card:hover,
        .insight-card:hover,
        .stat-cell:hover {{
            transform: translateY(-2px);
            box-shadow: 0 28px 60px rgba(17,16,14,0.14);
        }}
        .eyebrow {{
            color: var(--frame-red);
            font-size: 11px;
            letter-spacing: 0.18em;
            text-transform: uppercase;
            margin-bottom: 8px;
            font-weight: 700;
        }}
        .hero {{
            display: grid;
            grid-template-columns: 1.35fr .8fr;
            gap: 24px;
            padding: 8px 0 24px 0;
            margin-bottom: 26px;
            align-items: stretch;
        }}
        .hero h1 {{
            margin: 0;
            font-size: clamp(56px, 8vw, 98px);
            line-height: 0.86;
            max-width: 8ch;
            text-wrap: balance;
        }}
        .hero-copy {{
            font-size: 15px;
            line-height: 1.7;
            max-width: 420px;
            color: var(--soft-ink);
        }}
        .muted {{
            color: var(--soft-ink);
        }}
        .session-card {{
            background: linear-gradient(180deg, rgba(255,250,245,0.98), rgba(247,238,227,0.95));
            border: 1px solid rgba(17,16,14,0.08);
            padding: 18px;
            margin-bottom: 14px;
            border-radius: 24px;
            box-shadow: var(--shadow-soft);
        }}
        .subtle {{
            color: var(--soft-ink);
            font-size: 13px;
        }}
        .pill {{
            display: inline-block;
            padding: 6px 11px;
            border-radius: 999px;
            margin-right: 8px;
            font-weight: 700;
            margin-bottom: 8px;
            font-size: 12px;
            backdrop-filter: blur(6px);
        }}
        .sidebar-brand {{
            background:
                linear-gradient(180deg, rgba(255,255,255,0.08), rgba(255,255,255,0.04));
            border: 1px solid rgba(255,255,255,0.10);
            padding: 18px;
            margin-bottom: 16px;
            border-radius: 28px;
            box-shadow: inset 0 1px 0 rgba(255,255,255,0.08);
        }}
        .sidebar-brand h3 {{
            margin: 0 0 4px 0;
            color: #fff4ea;
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
            border: 1px solid rgba(255,255,255,0.20);
            box-shadow: 0 0 18px rgba(255,255,255,0.10);
        }}
        .editorial-rail {{
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            padding-left: 0;
            gap: 18px;
        }}
        .editorial-visual {{
            min-height: 340px;
            background:
                radial-gradient(circle at 24% 26%, rgba(255,192,131,0.86), transparent 18%),
                radial-gradient(circle at 70% 36%, rgba(216,92,26,0.66), transparent 18%),
                radial-gradient(circle at 82% 78%, rgba(17,16,14,0.20), transparent 16%),
                linear-gradient(135deg, #20170f 0%, #e9d6c2 52%, #fff7ef 100%);
            border: 1px solid rgba(17,16,14,0.08);
            position: relative;
            overflow: hidden;
            border-radius: 32px;
            box-shadow: var(--shadow-soft);
        }}
        .editorial-visual::before {{
            content: "";
            position: absolute;
            left: 6%;
            bottom: 8%;
            width: 44%;
            height: 24%;
            background: rgba(255,255,255,0.34);
            border: 1px solid rgba(255,255,255,0.40);
            border-radius: 999px;
            backdrop-filter: blur(18px);
        }}
        .editorial-visual::after {{
            content: "";
            position: absolute;
            right: 11%;
            top: 10%;
            width: 128px;
            height: 128px;
            border-radius: 50%;
            background: radial-gradient(circle, rgba(255,244,234,0.92), rgba(255,244,234,0.10) 70%);
            filter: blur(6px);
        }}
        .stat-strip {{
            display: grid;
            grid-template-columns: repeat(4, minmax(0, 1fr));
            gap: 16px;
            margin: 12px 0 30px 0;
        }}
        .stat-cell {{
            padding: 18px;
            border-radius: 24px;
            border: 1px solid rgba(17,16,14,0.08);
            background: linear-gradient(180deg, rgba(255,250,245,0.94), rgba(247,238,227,0.92));
            box-shadow: var(--shadow-soft);
            position: relative;
            overflow: hidden;
            transition: transform 0.18s ease, box-shadow 0.18s ease;
        }}
        .stat-line {{
            width: 54px;
            height: 6px;
            margin-bottom: 18px;
            border-radius: 999px;
        }}
        .stat-value {{
            font-family: "Syne", "Space Grotesk", sans-serif;
            font-size: clamp(30px, 3vw, 50px);
            line-height: 1;
            letter-spacing: -0.05em;
            color: var(--ink);
        }}
        .stat-label {{
            font-size: 11px;
            text-transform: uppercase;
            letter-spacing: 0.12em;
            color: var(--soft-ink);
            margin-top: 6px;
        }}
        .stat-note {{
            font-size: 12px;
            color: var(--soft-ink);
            margin-top: 6px;
        }}
        .insight-card {{
            padding: 18px;
            background: linear-gradient(180deg, rgba(255,250,245,0.98), rgba(247,238,227,0.95));
            border: 1px solid rgba(17,16,14,0.08);
            margin-bottom: 14px;
            border-radius: 26px;
            box-shadow: var(--shadow-soft);
            position: relative;
            overflow: hidden;
        }}
        .insight-card p {{
            margin: 10px 0 0 0;
            line-height: 1.6;
            color: var(--soft-ink);
            font-size: 14px;
        }}
        .editorial-card h3 {{
            margin: 0 0 8px 0;
            font-size: 30px;
        }}
        .editorial-card p {{
            margin: 0;
            line-height: 1.7;
            color: var(--soft-ink);
        }}
        .section-title {{
            font-family: "Syne", "Space Grotesk", sans-serif;
            font-size: clamp(32px, 4vw, 60px);
            line-height: 0.92;
            letter-spacing: -0.06em;
            margin: 16px 0 8px 0;
            text-transform: uppercase;
            max-width: 11ch;
            text-wrap: balance;
        }}
        .section-note {{
            max-width: 520px;
            font-size: 14px;
            line-height: 1.7;
            color: var(--soft-ink);
            margin-bottom: 20px;
        }}
        .queue-card {{
            padding: 18px;
            border: 1px solid rgba(17,16,14,0.08);
            background: linear-gradient(180deg, rgba(255,250,245,0.98), rgba(247,238,227,0.95));
            margin-bottom: 14px;
            border-radius: 26px;
            box-shadow: var(--shadow-soft);
            position: relative;
            overflow: hidden;
        }}
        .queue-card h4 {{
            margin: 6px 0 2px 0;
            font-size: 24px;
        }}
        .queue-card p {{
            margin: 10px 0 0 0;
            color: var(--soft-ink);
            line-height: 1.6;
            font-size: 14px;
        }}
        [data-testid="stAlert"] {{
            border-radius: 22px;
            border: 1px solid rgba(17,16,14,0.08);
            background: linear-gradient(180deg, rgba(255,250,245,0.98), rgba(247,238,227,0.95));
            box-shadow: var(--shadow-soft);
        }}
        [data-testid="stMarkdownContainer"] code,
        code {{
            background: rgba(17,16,14,0.08);
            border-radius: 8px;
            padding: 0.15rem 0.35rem;
            color: var(--ink);
        }}
        hr {{
            border: none;
            height: 1px;
            background: linear-gradient(90deg, rgba(216,92,26,0.32), rgba(17,16,14,0.06));
        }}
        @media (max-width: 980px) {{
            .hero {{
                grid-template-columns: 1fr;
            }}
            .editorial-rail {{
                padding-left: 0;
                padding-top: 18px;
            }}
            .stat-strip {{
                grid-template-columns: repeat(2, minmax(0, 1fr));
            }}
            .block-container {{
                margin: 10px 10px 36px 10px;
                padding: 22px 18px 36px 18px;
                border-radius: 26px;
            }}
        }}
        @media (max-width: 640px) {{
            .stat-strip {{
                grid-template-columns: 1fr;
            }}
            .hero h1 {{
                font-size: clamp(46px, 16vw, 72px);
            }}
            .editorial-visual {{
                min-height: 260px;
            }}
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )


def login_screen() -> None:
    inject_css()
    left, right = st.columns([1.45, 0.9], gap="large")
    with left:
        st.markdown(
            f"""
            <div class="hero">
              <div>
                <div class="eyebrow">Nook Control Room</div>
                <h1>FOUNDER<br>& FACILITATOR<br><span style="color:{FRAME_RED}">SYSTEM</span></h1>
                <p class="hero-copy">
                  A role-based operating layer for Nook: founder decisions, facilitator logistics,
                  member review, experience design, internal messaging, and smarter daily action cues.
                </p>
              </div>
              <div class="editorial-rail">
                <div class="editorial-visual"></div>
                <div>
                  <div class="eyebrow">Access Design</div>
                  <p class="hero-copy">
                    Founder view sees the entire operating picture. Facilitator view stays focused on
                    assigned sessions, messages, availability, and profile context.
                  </p>
                </div>
              </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        render_stat_strip(
            [
                {"value": "2", "label": "Core routes", "note": "Founder and facilitator", "accent": FRAME_RED},
                {"value": "6", "label": "Seeded accounts", "note": "Ready for demo and testing", "accent": KLEIN_BLUE},
                {"value": "4", "label": "Smart layers", "note": "Priorities, alerts, fits, staffing", "accent": AQUAMARINE},
                {"value": "1", "label": "Single workspace", "note": "One control room, different access", "accent": FUCHSIA},
            ]
        )
        st.markdown(
            editorial_card(
                "Access stays private",
                "Passwords are no longer shown on this screen. Founder can still create or reset facilitator access inside the app, and demo entry points stay available without exposing credentials.",
                eyebrow="Security",
            ),
            unsafe_allow_html=True,
        )
    with right:
        st.markdown(
            editorial_card(
                "Enter your assigned credentials",
                "Founder and facilitator passwords stay private. Use the demo entry below if you only want to preview the routes.",
                eyebrow="Login",
            ),
            unsafe_allow_html=True,
        )
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
        st.caption("Usernames are visible to the founder. Passwords stay hidden from this page.")
        st.markdown(
            editorial_card(
                "Demo entry",
                "Open the founder workspace or the facilitator route without revealing passwords on the login screen.",
                eyebrow="Preview",
            ),
            unsafe_allow_html=True,
        )
        demo_left, demo_right = st.columns(2)
        if demo_left.button("Demo founder", use_container_width=True, type="secondary"):
            st.session_state.current_user = deepcopy(FOUNDER_ACCOUNT)
            st.rerun()
        facilitator_demo = next((account for account in all_accounts() if account["role"] == "facilitator"), None)
        if demo_right.button("Demo facilitator", use_container_width=True, type="secondary") and facilitator_demo:
            st.session_state.current_user = facilitator_demo
            st.rerun()
        st.markdown(
            editorial_card(
                "Visible usernames",
                "Founder username: manju. Facilitator usernames are assigned by founder, for example riya.fac and sneha.fac.",
                eyebrow="Hint",
            ),
            unsafe_allow_html=True,
        )


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
              <div class="eyebrow">Nook</div>
              <h3>{user['name']}</h3>
              <div class="subtle">{user['role'].title()} route</div>
              <div class="swatch-row">
                <div class="swatch" style="background:{FRAME_RED}"></div>
                <div class="swatch" style="background:{KLEIN_BLUE}"></div>
                <div class="swatch" style="background:{CITRIC}"></div>
                <div class="swatch" style="background:{AQUAMARINE}"></div>
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
        <div class="eyebrow">Nook / {title}</div>
        <div class="section-title">{title}</div>
        <div class="section-note">{subtitle}</div>
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


def build_experience_blueprint(theme: str, tier: str, mood: str, venue_type: str) -> Dict[str, str]:
    theme_clean = theme.strip() or "Curated Evening"
    mood_key = mood.lower().strip()
    venue_key = venue_type.lower().strip()
    opener_map = {
        "calm": "Soft arrival ritual with a welcome drink and one low-pressure prompt card per person.",
        "playful": "Fast warm-up with pair swaps, playful prompt cards, and an immediate shared challenge.",
        "intimate": "Quiet seating cluster, no-name introductions, and a short story exchange.",
        "bold": "High-energy arrival with a tactile icebreaker and immediate room movement.",
    }
    unwind_map = {
        "fo": "Founder-style closeout with one memorable question and an easy next-step invitation.",
        "ibp": "A slower circle close where members reflect on one surprising connection from the room.",
        "wi": "A premium-feeling closing ritual with names revealed at the warmest emotional beat.",
        "yhttb": "A richer hosted close with founder-grade details, memory anchors, and a discreet follow-up cue.",
    }
    activity = "Shared experience designed around the venue so conversation grows naturally instead of feeling forced."
    if any(word in theme_clean.lower() for word in ["paint", "canvas", "art", "sketch"]):
        activity = "Paired visual creation with hidden prompts, then a mid-point swap so people build on each other's work."
    elif any(word in theme_clean.lower() for word in ["dinner", "supper", "food", "tasting"]):
        activity = "A guided tasting arc where each course unlocks a conversation direction and one shared choice."
    elif any(word in theme_clean.lower() for word in ["walk", "route", "city", "trail"]):
        activity = "A structured movement-based experience with check-in stops and one reflective prompt at each pivot."
    elif any(word in theme_clean.lower() for word in ["pottery", "clay", "craft", "studio"]):
        activity = "Hands-on making session where pairs trade interpretation rather than working in isolation."

    transport = "Founder-arranged cab clusters."
    if "walk" in venue_key or "old city" in venue_key:
        transport = "Walkable route with one fixed regroup point."
    elif "cafe" in venue_key or "studio" in venue_key:
        transport = "Auto and cab mix with clear arrival timing."

    notes = (
        f"Keep the room feeling {mood.lower()} and intentional. "
        f"Prioritize {tier_label(tier)} expectations and make sure the venue supports easy conversation flow."
    )
    return {
        "name": theme_clean,
        "act1": opener_map.get(mood_key, opener_map["calm"]),
        "act2": activity,
        "act3": unwind_map.get(tier, unwind_map["fo"]),
        "transport": transport,
        "notes": notes,
    }


def render_dashboard(user: Dict) -> None:
    data = data_store()
    show_header("Dashboard", "An editorial view of what needs attention now, what is healthy, and what should happen next.")
    if user["role"] == "founder":
        pending = sum(1 for m in data["members"] if get_admin(m["id"])["status"] == "pending")
        revenue = sum(p["amount"] for p in data["payments"] if p["status"] == "paid")
        active_facs = sum(1 for f in data["facs"] if f["status"] == "active")
        render_stat_strip(
            [
                {"value": len(data["members"]), "label": "Total submissions", "note": "Community pipeline", "accent": FRAME_RED},
                {"value": pending, "label": "Pending review", "note": "Needs founder decision", "accent": CITRIC},
                {"value": format_money(revenue), "label": "Revenue collected", "note": "Paid memberships", "accent": KLEIN_BLUE},
                {"value": active_facs, "label": "Active facilitators", "note": "Available team", "accent": AQUAMARINE},
            ]
        )
        st.markdown(
            "<div class='section-title'>Priority Queue</div>"
            "<div class='section-note'>Smart-ranked leads and live operational alerts so the founder can move quickly without scanning every page.</div>",
            unsafe_allow_html=True,
        )
        left, right = st.columns([1.2, 0.8], gap="large")
        priority_members = sorted(
            data["members"],
            key=lambda member: (
                get_admin(member["id"])["status"] not in {"pending", "waitlist"},
                -smart_member_score(member),
                member["ts"],
            ),
        )[:4]
        with left:
            for member in priority_members:
                admin = get_admin(member["id"])
                recommendation = smart_member_recommendation(member)
                st.markdown(
                    f"""
                    <div class="queue-card">
                      {pill_html(recommendation["label"], recommendation["tone"])}
                      {status_badge(admin["status"])}
                      {tier_badge(admin["tier"])}
                      <h4>{member["name"]}</h4>
                      <div class="subtle">Lead score {smart_member_score(member)} · {member["email"]} · {member["availability"]}</div>
                      <p>{member["intent"]}</p>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
        with right:
            for alert in smart_operational_alerts(user):
                st.markdown(insight_card_html(alert["title"], alert["detail"], alert["tone"]), unsafe_allow_html=True)

        st.markdown(
            "<div class='section-title'>Upcoming Experiences</div>"
            "<div class='section-note'>Current sessions, staffing confidence, and quick founder visibility into facilitator coverage.</div>",
            unsafe_allow_html=True,
        )
        exp_left, exp_right = st.columns([1.05, 0.95], gap="large")
        with exp_left:
            for exp in upcoming_experiences(limit=3):
                fac = get_fac(exp["fac"]) if exp.get("fac") else None
                recommendation = recommended_facilitator(exp) if (not fac or on_leave(fac["id"])) else None
                suggestion = f"Suggested facilitator: {recommendation['name']}" if recommendation else "Current staffing looks good."
                st.markdown(
                    f"""
                    <div class="session-card">
                      {tier_badge(exp["tier"])}
                      <strong>{exp["name"]}</strong><br>
                      <span class="subtle">{exp["date"]} · {exp["time"]} · {exp["venue"]} · {format_money(int(exp["price"]))}/person</span><br>
                      <span class="subtle">Assigned: {fac["name"] if fac else "Unassigned"}{' · on leave' if fac and on_leave(fac['id']) else ''}</span>
                      <p style="margin:10px 0 0 0;color:{SOFT_INK};font-size:14px;line-height:1.6">{suggestion}</p>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
        with exp_right:
            facilitator_rows = sorted(
                [fac_item for fac_item in data["facs"] if fac_item["status"] != "offboarded"],
                key=lambda fac_item: (on_leave(fac_item["id"]), facilitator_session_load(fac_item["id"])),
            )
            for fac_item in facilitator_rows[:4]:
                availability = "On leave" if on_leave(fac_item["id"]) else "Available"
                st.markdown(
                    f"""
                    <div class="queue-card">
                      {status_badge(fac_item["status"])}
                      {pill_html(availability, "tangerine" if availability == "On leave" else "aqua")}
                      <h4>{fac_item["name"]}</h4>
                      <div class="subtle">{tier_label(fac_item["access"])} access · {facilitator_session_load(fac_item["id"])} assigned session(s)</div>
                      <p>{fac_item["notes"]}</p>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
    else:
        fac = get_fac(user["fac_id"]) or {}
        my_sessions = [exp for exp in data["exps"] if exp["fac"] == user["fac_id"]]
        unread = sum(1 for msg in data["msgs"] if msg["to"] == user["id"] and not msg["read"])
        render_stat_strip(
            [
                {"value": len(my_sessions), "label": "My sessions", "note": "Assigned by founder", "accent": FRAME_RED},
                {"value": fac.get("status", "-").title(), "label": "My status", "note": "Current facilitator state", "accent": AQUAMARINE},
                {"value": fac.get("refs", 0), "label": "Referral slots", "note": "Available invites", "accent": CITRIC},
                {"value": unread, "label": "Unread messages", "note": "Founder updates waiting", "accent": KLEIN_BLUE},
            ]
        )
        st.markdown(
            "<div class='section-title'>Facilitator Focus</div>"
            "<div class='section-note'>Your next session, your live alerts, and the room details you need before showing up.</div>",
            unsafe_allow_html=True,
        )
        left, right = st.columns([1.08, 0.92], gap="large")
        with left:
            if not my_sessions:
                st.info("No sessions assigned yet.")
            for exp in my_sessions:
                st.markdown(
                    f"""
                    <div class="session-card">
                      {tier_badge(exp["tier"])}
                      <strong>{exp["name"]}</strong><br>
                      <span class="subtle">{exp["date"]} · {exp["time"]} · {exp["venue"]} · Max {exp["max"]}</span>
                      <hr style="border-color:{LINE}">
                      <div class="subtle"><strong>Act 1:</strong> {exp["act1"]}</div>
                      <div class="subtle"><strong>Act 2:</strong> {exp["act2"]}</div>
                      <div class="subtle"><strong>Act 3:</strong> {exp["act3"]}</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
        with right:
            for alert in smart_operational_alerts(user):
                st.markdown(insight_card_html(alert["title"], alert["detail"], alert["tone"]), unsafe_allow_html=True)


def render_members() -> None:
    data = data_store()
    show_header("Members", "Review incoming Nook submissions, sort by smart fit, and move quickly on people who deserve attention.")
    counts = {
        "all": len(data["members"]),
        "pending": sum(1 for m in data["members"] if get_admin(m["id"])["status"] == "pending"),
        "approved": sum(1 for m in data["members"] if get_admin(m["id"])["status"] == "approved"),
        "waitlist": sum(1 for m in data["members"] if get_admin(m["id"])["status"] == "waitlist"),
    }
    render_stat_strip(
        [
            {"value": counts["all"], "label": "All members", "note": "Current records", "accent": FRAME_RED},
            {"value": counts["pending"], "label": "Pending", "note": "Awaiting founder action", "accent": CITRIC},
            {"value": counts["approved"], "label": "Approved", "note": "Ready for programming", "accent": AQUAMARINE},
            {"value": counts["waitlist"], "label": "Waitlist", "note": "Hold for later follow-up", "accent": FUCHSIA},
        ]
    )
    filters_left, filters_mid, filters_right = st.columns([1.1, 0.8, 0.8])
    query = filters_left.text_input("Search members", placeholder="Name, email, availability, activities")
    status_filter = filters_mid.selectbox("Status", ["all", "pending", "approved", "waitlist", "declined"])
    sort_mode = filters_right.selectbox("Sort by", ["Smart priority", "Newest", "Most sessions"])

    members = data["members"]
    if query.strip():
        needle = query.lower().strip()
        members = [
            member for member in members
            if needle in " ".join(
                [
                    member.get("name", ""),
                    member.get("email", ""),
                    member.get("availability", ""),
                    member.get("activities", ""),
                    member.get("intent", ""),
                ]
            ).lower()
        ]
    if status_filter != "all":
        members = [member for member in members if get_admin(member["id"])["status"] == status_filter]
    if sort_mode == "Smart priority":
        members = sorted(
            members,
            key=lambda member: (
                get_admin(member["id"])["status"] not in {"pending", "waitlist"},
                -smart_member_score(member),
                -member.get("sessions", 0),
            ),
        )
    elif sort_mode == "Newest":
        members = sorted(members, key=lambda member: member["ts"], reverse=True)
    else:
        members = sorted(members, key=lambda member: member.get("sessions", 0), reverse=True)

    for member in members:
        admin = get_admin(member["id"])
        recommendation = smart_member_recommendation(member)
        expander_label = f"{member['name']} · {member['email']} · score {smart_member_score(member)}"
        with st.expander(expander_label):
            left, right = st.columns([1.2, 0.9], gap="large")
            with left:
                st.markdown(
                    f"""
                    <div class="queue-card">
                      {pill_html(recommendation["label"], recommendation["tone"])}
                      {status_badge(admin["status"])}
                      {tier_badge(admin["tier"])}
                      <h4>{member["name"]}</h4>
                      <div class="subtle">Submitted {member["ts"]} · {member["availability"]} · {member.get("sessions", 0)} past session(s)</div>
                      <p>{member["intent"]}</p>
                      <p style="margin-top:12px"><strong>Activities:</strong> {member["activities"]}<br><strong>Budget:</strong> {member["budget"]}<br><strong>Newsletter:</strong> {'Yes' if member["newsletter"] == 'yes' else 'No'}<br><strong>Cafe ideas:</strong> {member["cafe"]}</p>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
            with right:
                with st.form(f"member_admin_v2_{member['id']}"):
                    new_status = st.selectbox(
                        "Status",
                        ["pending", "approved", "waitlist", "declined"],
                        index=["pending", "approved", "waitlist", "declined"].index(admin["status"]),
                        key=f"member_status_v2_{member['id']}",
                    )
                    new_tier = st.selectbox(
                        "Tier",
                        ["fo", "ibp", "wi", "yhttb"],
                        index=["fo", "ibp", "wi", "yhttb"].index(admin["tier"]),
                        format_func=tier_label,
                        key=f"member_tier_v2_{member['id']}",
                    )
                    fac_flag = st.checkbox("Facilitator candidate", value=admin["fac"], key=f"member_fac_v2_{member['id']}")
                    notes = st.text_area("Founder notes", value=admin["notes"], key=f"member_notes_v2_{member['id']}")
                    if st.form_submit_button("Save member review", use_container_width=True, type="primary"):
                        data["admin"][member["id"]] = {
                            "status": new_status,
                            "tier": new_tier,
                            "notes": notes,
                            "fac": fac_flag,
                        }
                        persist()
                        st.success("Member updated.")
                        st.rerun()


def render_planner() -> None:
    data = data_store()
    show_header("Planner", "Design sessions with smarter structure, staffing suggestions, and cleaner founder control.")
    if "planner_name" not in st.session_state:
        st.session_state.planner_name = ""
        st.session_state.planner_act1 = ""
        st.session_state.planner_act2 = ""
        st.session_state.planner_act3 = ""
        st.session_state.planner_transport = ""
        st.session_state.planner_notes = ""

    top_left, top_right = st.columns([1.05, 0.95], gap="large")
    with top_left:
        st.markdown(
            editorial_card(
                "Smart blueprint builder",
                "Use a theme, mood, and venue type to generate a session structure you can edit before saving.",
                eyebrow="Planning help",
            ),
            unsafe_allow_html=True,
        )
        with st.form("blueprint_form"):
            bp_theme = st.text_input("Experience theme", placeholder="Canvas night, secret supper, slow brunch, city walk")
            bp_cols = st.columns(3)
            bp_tier = bp_cols[0].selectbox("Tier", ["fo", "ibp", "wi", "yhttb"], format_func=tier_label)
            bp_mood = bp_cols[1].selectbox("Mood", ["calm", "playful", "intimate", "bold"])
            bp_venue = bp_cols[2].text_input("Venue type", placeholder="Cafe, studio, old city, rooftop")
            if st.form_submit_button("Generate blueprint", use_container_width=True, type="secondary"):
                blueprint = build_experience_blueprint(bp_theme, bp_tier, bp_mood, bp_venue)
                st.session_state.planner_name = blueprint["name"]
                st.session_state.planner_tier = bp_tier
                st.session_state.planner_venue = bp_venue
                st.session_state.planner_act1 = blueprint["act1"]
                st.session_state.planner_act2 = blueprint["act2"]
                st.session_state.planner_act3 = blueprint["act3"]
                st.session_state.planner_transport = blueprint["transport"]
                st.session_state.planner_notes = blueprint["notes"]
                st.rerun()
    with top_right:
        alerts = smart_operational_alerts(FOUNDER_ACCOUNT)
        for alert in alerts[:3]:
            st.markdown(insight_card_html(alert["title"], alert["detail"], alert["tone"]), unsafe_allow_html=True)

    with st.expander("Create new experience", expanded=True):
        with st.form("new_experience_v2"):
            c1, c2, c3 = st.columns(3)
            name = c1.text_input("Experience name", key="planner_name")
            tier = c2.selectbox("Tier", ["fo", "ibp", "wi", "yhttb"], format_func=tier_label, key="planner_tier")
            active_facs = [fac for fac in data["facs"] if fac["status"] != "offboarded"]
            fac_map = {"Unassigned": ""}
            for fac in active_facs:
                fac_map[fac["name"]] = fac["id"]
            fac_name = c3.selectbox("Facilitator", list(fac_map.keys()), key="planner_fac")
            d1, d2, d3, d4 = st.columns(4)
            exp_date = d1.date_input("Date", value=date.today(), key="planner_date")
            exp_time = d2.text_input("Time", value="18:00", key="planner_time")
            capacity = d3.number_input("Max attendees", min_value=1, value=8, key="planner_capacity")
            price = d4.number_input("Price per person", min_value=0, value=500, key="planner_price")
            venue = st.text_input("Venue", key="planner_venue")
            act1 = st.text_area("Act 1 - Opener", key="planner_act1")
            act2 = st.text_area("Act 2 - Activity", key="planner_act2")
            act3 = st.text_area("Act 3 - Unwind", key="planner_act3")
            transport = st.text_input("Transport", key="planner_transport")
            notes = st.text_area("Notes / vibe", key="planner_notes")
            if st.form_submit_button("Save experience", use_container_width=True, type="primary"):
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

    st.markdown(
        "<div class='section-title'>Experience Deck</div>"
        "<div class='section-note'>Every session stays editable through the data file, and staffing recommendations surface when coverage looks weak.</div>",
        unsafe_allow_html=True,
    )
    for exp in upcoming_experiences():
        fac = get_fac(exp["fac"]) if exp.get("fac") else None
        suggestion = recommended_facilitator(exp) if (not fac or on_leave(fac["id"])) else None
        with st.expander(f"{exp['name']} · {exp['date']}"):
            st.markdown(
                f"""
                <div class="session-card">
                  {tier_badge(exp["tier"])}
                  <strong>{exp["name"]}</strong><br>
                  <span class="subtle">{exp["time"]} · {exp["venue"]} · Max {exp["max"]} · {format_money(int(exp["price"]))}</span><br>
                  <span class="subtle">Assigned facilitator: {fac["name"] if fac else "Unassigned"}{' · on leave' if fac and on_leave(fac['id']) else ''}</span>
                </div>
                """,
                unsafe_allow_html=True,
            )
            st.write(f"Act 1: {exp['act1']}")
            st.write(f"Act 2: {exp['act2']}")
            st.write(f"Act 3: {exp['act3']}")
            if exp["notes"]:
                st.caption(exp["notes"])
            actions_left, actions_right = st.columns([1, 1])
            if suggestion and actions_left.button(f"Assign {suggestion['name']}", key=f"assign_{exp['id']}"):
                exp["fac"] = suggestion["id"]
                persist()
                st.success("Suggested facilitator assigned.")
                st.rerun()
            if actions_right.button("Delete experience", key=f"delete_planner_{exp['id']}"):
                data["exps"] = [item for item in data["exps"] if item["id"] != exp["id"]]
                persist()
                st.rerun()


def render_facilitator_team(user: Dict) -> None:
    data = data_store()
    if user["role"] != "founder":
        fac = get_fac(user["fac_id"])
        show_header("My Profile", "Your facilitator route stays focused on your access, your status, and your role context.")
        if fac:
            st.markdown(
                f"""
                <div class="queue-card">
                  {status_badge(fac['status'])}
                  {pill_html(f"{tier_label(fac['access'])} access", 'klein')}
                  {pill_html(f"{fac['refs']} referral slots", 'citric')}
                  <h4>{fac['name']}</h4>
                  <div class="subtle">{fac['email']} · {fac['phone']}</div>
                  <p>{fac['notes']}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )
        return

    show_header("Facilitator Team", "Manage active facilitators, onboard flagged members, and update access without exposing passwords on-screen.")
    render_stat_strip(
        [
            {"value": sum(1 for fac in data["facs"] if fac["status"] == "active"), "label": "Active", "note": "Running sessions", "accent": AQUAMARINE},
            {"value": sum(1 for fac in data["facs"] if fac["status"] == "candidate"), "label": "Candidate", "note": "In observation", "accent": CITRIC},
            {"value": sum(1 for fac in data["facs"] if on_leave(fac["id"]) and fac["status"] != "offboarded"), "label": "On leave", "note": "Needs coverage", "accent": TANGERINE},
            {"value": len([m for m in data["members"] if get_admin(m["id"])["fac"]]), "label": "Flagged members", "note": "Potential facilitators", "accent": FUCHSIA},
        ]
    )

    candidates = [
        member for member in data["members"]
        if get_admin(member["id"])["fac"] and not any(fac.get("member_id") == member["id"] for fac in data["facs"])
    ]
    if candidates:
        st.markdown(
            "<div class='section-title'>Onboarding Queue</div><div class='section-note'>Members already flagged by the founder can be converted into facilitator accounts here.</div>",
            unsafe_allow_html=True,
        )
        for member in candidates:
            with st.expander(f"{member['name']} · flagged candidate"):
                default_uid = member["name"].split(" ")[0].lower() + ".fac"
                with st.form(f"onboard_{member['id']}"):
                    cols = st.columns(3)
                    uid = cols[0].text_input("Login ID", value=default_uid, key=f"candidate_uid_{member['id']}")
                    password = cols[1].text_input("Temporary password", type="password", value="", placeholder="Set a private temp password", key=f"candidate_pw_{member['id']}")
                    access = cols[2].selectbox("Tier access", ["fo", "ibp", "wi", "yhttb"], format_func=tier_label, key=f"candidate_access_{member['id']}")
                    notes = st.text_area("Notes", value="Onboarded from flagged member pipeline.", key=f"candidate_notes_{member['id']}")
                    if st.form_submit_button("Create facilitator account", use_container_width=True, type="primary"):
                        data["facs"].append(
                            {
                                "id": f"f{uuid4().hex[:5]}",
                                "member_id": member["id"],
                                "name": member["name"],
                                "uid": uid.strip(),
                                "password": password or f"nook-{uuid4().hex[:6]}",
                                "email": member["email"],
                                "phone": member.get("phone", ""),
                                "status": "candidate",
                                "access": access,
                                "refs": 2,
                                "sessions": max(member.get("sessions", 0), 2),
                                "notes": notes,
                            }
                        )
                        persist()
                        st.success("Facilitator account created.")
                        st.rerun()

    with st.expander("Add facilitator manually", expanded=False):
        with st.form("add_facilitator_v2"):
            c1, c2 = st.columns(2)
            name = c1.text_input("Full name")
            uid = c2.text_input("Login ID", placeholder="name.fac")
            c3, c4 = st.columns(2)
            email = c3.text_input("Email")
            phone = c4.text_input("Phone")
            c5, c6, c7 = st.columns(3)
            password = c5.text_input("Temporary password", type="password", value="", placeholder="Set a private temp password")
            status = c6.selectbox("Status", ["candidate", "active", "offboarded"])
            access = c7.selectbox("Tier access", ["fo", "ibp", "wi", "yhttb"], format_func=tier_label)
            refs = st.number_input("Referral slots", min_value=0, value=2)
            notes = st.text_area("Notes")
            if st.form_submit_button("Save facilitator", use_container_width=True, type="primary"):
                data["facs"].append(
                    {
                        "id": f"f{uuid4().hex[:5]}",
                        "name": name,
                        "uid": uid.strip(),
                        "password": password or f"nook-{uuid4().hex[:6]}",
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

    st.markdown(
        "<div class='section-title'>Team Profiles</div><div class='section-note'>Login IDs remain visible to the founder, but passwords are only editable through private reset fields.</div>",
        unsafe_allow_html=True,
    )
    for fac in data["facs"]:
        with st.expander(f"{fac['name']} · {fac['status'].title()}"):
            with st.form(f"fac_edit_{fac['id']}"):
                cols = st.columns([1, 1, 1])
                status = cols[0].selectbox("Status", ["candidate", "active", "offboarded"], index=["candidate", "active", "offboarded"].index(fac["status"]), key=f"fac_status_edit_{fac['id']}")
                access = cols[1].selectbox("Tier access", ["fo", "ibp", "wi", "yhttb"], index=["fo", "ibp", "wi", "yhttb"].index(fac["access"]), format_func=tier_label, key=f"fac_access_edit_{fac['id']}")
                refs = cols[2].number_input("Referral slots", min_value=0, value=int(fac["refs"]), key=f"fac_refs_edit_{fac['id']}")
                st.write(f"Login ID: `{fac['uid']}`")
                st.write(f"Email: {fac['email']}")
                st.write(f"Phone: {fac['phone']}")
                reset_password = st.text_input("Reset password", type="password", value="", key=f"reset_pw_{fac['id']}")
                notes = st.text_area("Notes", value=fac["notes"], key=f"fac_notes_v2_{fac['id']}")
                save_col, off_col = st.columns(2)
                if save_col.form_submit_button("Save facilitator", use_container_width=True, type="primary"):
                    fac["status"] = status
                    fac["access"] = access
                    fac["refs"] = int(refs)
                    fac["notes"] = notes
                    if reset_password.strip():
                        fac["password"] = reset_password
                    persist()
                    st.success("Facilitator updated.")
                    st.rerun()
                if off_col.form_submit_button("Offboard", use_container_width=True, type="secondary"):
                    fac["status"] = "offboarded"
                    persist()
                    st.warning("Facilitator offboarded.")
                    st.rerun()


def render_messages(user: Dict) -> None:
    data = data_store()
    show_header("Messages", "Founder and facilitator conversations stay inside the system, with dynamic account routing instead of hard-coded users.")
    for msg in data["msgs"]:
        if msg["to"] == user["id"]:
            msg["read"] = True
    persist()

    accounts = [{"id": account["id"], "name": account["name"]} for account in all_accounts()]
    recipient_options = {account["name"]: account["id"] for account in accounts if account["id"] != user["id"]}
    with st.expander("Send a new message", expanded=False):
        with st.form("new_message_v2"):
            recipient = st.selectbox("To", list(recipient_options.keys()))
            subject = st.selectbox("Message type", ["General update", "Session reminder", "Request information from member", "Post-session update"])
            body = st.text_area("Message")
            if st.form_submit_button("Send message", use_container_width=True, type="primary"):
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

    thread = [msg for msg in data["msgs"] if msg["to"] == user["id"] or msg["from"] == user["id"]]
    thread.sort(key=lambda msg: msg["ts"], reverse=True)
    for msg in thread:
        st.markdown(
            f"""
            <div class="queue-card">
              {pill_html(msg["subject"], "klein" if msg["from"] == user["id"] else "aqua")}
              <h4>{resolve_user_name(msg["from"])}</h4>
              <div class="subtle">To {resolve_user_name(msg["to"])} · {msg["ts"]}</div>
              <p>{msg["body"]}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )


def render_docs() -> None:
    show_header("Docs", "What this app now does, how access is handled, and where the functional pieces live.")
    st.markdown(
        editorial_card(
            "System overview",
            "This Streamlit version now behaves like a real internal operating layer: dynamic facilitator accounts, founder and facilitator routes, local persistence, smart dashboard signals, experience planning support, internal messaging, and private credential handling on the login screen.",
            eyebrow="Architecture",
        ),
        unsafe_allow_html=True,
    )
    render_stat_strip(
        [
            {"value": "Founder", "label": "Primary route", "note": "Sees the full operating layer", "accent": FRAME_RED},
            {"value": "Facilitator", "label": "Secondary route", "note": "Sees only assigned operational context", "accent": AQUAMARINE},
            {"value": "JSON", "label": "Persistence", "note": "Local workspace data store", "accent": KLEIN_BLUE},
            {"value": "Private", "label": "Passwords", "note": "No passwords shown on login", "accent": FUCHSIA},
        ]
    )
    st.write("- Data is stored locally in `nook_data.json`.")
    st.write("- Founder login still uses private credentials, but no password is shown anywhere on the login page.")
    st.write("- Facilitator accounts are now generated from the live facilitator records, so new facilitators can actually log in.")
    st.write("- Password resets happen through private fields inside the founder workspace instead of visible account lists.")


def current_month_key() -> str:
    return datetime.now().strftime("%Y-%m")


def visible_private_entries(user: Dict) -> List[Dict]:
    entries = data_store().get("private_entries", [])
    if user["role"] == "founder":
        return sorted(entries, key=lambda entry: entry["created_at"], reverse=True)
    return sorted([entry for entry in entries if entry["owner_id"] == user["id"]], key=lambda entry: entry["created_at"], reverse=True)


def monthly_referral_usage(fac_user_id: str, month_key: Optional[str] = None) -> int:
    month_key = month_key or current_month_key()
    return sum(1 for referral in data_store().get("referrals", []) if referral["fac_id"] == fac_user_id and referral["month"] == month_key)


def sync_referral_status(member_id: str, new_status: str) -> None:
    referral_map = {"approved": "approved", "waitlist": "waitlist", "declined": "rejected"}
    for referral in data_store().get("referrals", []):
        if referral.get("member_id") == member_id:
            referral["status"] = referral_map.get(new_status, referral["status"])


def render_home(user: Dict) -> None:
    data = data_store()
    show_header("Home", "A private workspace for personal notes and operating updates. Entries stay visible to the owner and the founder only.")
    left, right = st.columns([1.08, 0.92], gap="large")
    with left:
        st.markdown(
            editorial_card(
                "Private desk",
                "Write notes, session reads, reminders, and operational thoughts. Facilitators only see their own entries. Founder can view everyone's private desk for oversight.",
                eyebrow="Workspace",
            ),
            unsafe_allow_html=True,
        )
        with st.form(f"private_entry_{user['id']}"):
            kind = st.selectbox("Entry type", ["note", "update", "reminder"])
            title = st.text_input("Title", placeholder="What do you want to remember?")
            body = st.text_area("Body", placeholder="Write a founder-only or personal operating note.")
            if st.form_submit_button("Save private entry", use_container_width=True, type="primary"):
                if body.strip():
                    data.setdefault("private_entries", []).append(
                        {
                            "id": uuid4().hex[:8],
                            "owner_id": user["id"],
                            "title": title.strip() or kind.title(),
                            "body": body.strip(),
                            "kind": kind,
                            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
                        }
                    )
                    persist()
                    st.success("Private entry saved.")
                    st.rerun()
                st.error("Write something first.")

        st.markdown("<div class='section-title'>My Private Entries</div>", unsafe_allow_html=True)
        mine = [entry for entry in visible_private_entries(user) if entry["owner_id"] == "manju"] if user["role"] == "founder" else visible_private_entries(user)
        for entry in mine[:8]:
            st.markdown(
                f"""
                <div class="queue-card">
                  {pill_html(entry["kind"].title(), "black" if entry["kind"] == "note" else "tangerine")}
                  <h4>{entry["title"]}</h4>
                  <div class="subtle">{entry["created_at"]}</div>
                  <p>{entry["body"]}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )
        if not mine:
            st.info("No private entries yet.")
    with right:
        render_stat_strip(
            [
                {"value": len(visible_private_entries(user)), "label": "Visible entries", "note": "Private workspace items", "accent": FRAME_RED},
                {"value": monthly_referral_usage(user["id"]) if user["role"] == "facilitator" else len(data.get("referrals", [])), "label": "Referral load", "note": "This month or total queue", "accent": TANGERINE},
                {"value": len(smart_operational_alerts(user)), "label": "Smart alerts", "note": "Actionable cues", "accent": NOOK_BLACK},
                {"value": len([msg for msg in data["msgs"] if msg["to"] == user["id"] and not msg["read"]]) if user["role"] != "founder" else len([msg for msg in data["msgs"] if msg["to"] == "manju" and not msg["read"]]), "label": "Unread", "note": "Internal messages", "accent": CITRIC},
            ]
        )
        st.markdown("<div class='section-title'>Smart Suggestions</div><div class='section-note'>Operational prompts generated from live app data.</div>", unsafe_allow_html=True)
        for alert in smart_operational_alerts(user):
            st.markdown(insight_card_html(alert["title"], alert["detail"], alert["tone"]), unsafe_allow_html=True)
        if user["role"] == "founder":
            owners = ["All facilitators", *[fac["uid"] for fac in data["facs"] if fac["status"] != "offboarded"]]
            selected_owner = st.selectbox("Team private feed", owners)
            team_entries = [
                entry for entry in data.get("private_entries", [])
                if entry["owner_id"] != "manju" and (selected_owner == "All facilitators" or entry["owner_id"] == selected_owner)
            ]
            for entry in sorted(team_entries, key=lambda item: item["created_at"], reverse=True)[:8]:
                st.markdown(
                    f"""
                    <div class="queue-card">
                      {pill_html(resolve_user_name(entry["owner_id"]), "citric")}
                      <h4>{entry["title"]}</h4>
                      <div class="subtle">{entry["created_at"]}</div>
                      <p>{entry["body"]}</p>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
        else:
            st.markdown(
                editorial_card(
                    "Privacy rule",
                    "Your notes and updates are visible only to you and the founder. Other facilitators cannot read them.",
                    eyebrow="Access",
                ),
                unsafe_allow_html=True,
            )


def render_members() -> None:
    data = data_store()
    show_header("Applications", "Founder-only application review with direct accept, reject, and waitlist controls.")
    counts = {
        "all": len(data["members"]),
        "pending": sum(1 for member in data["members"] if get_admin(member["id"])["status"] == "pending"),
        "approved": sum(1 for member in data["members"] if get_admin(member["id"])["status"] == "approved"),
        "waitlist": sum(1 for member in data["members"] if get_admin(member["id"])["status"] == "waitlist"),
    }
    render_stat_strip(
        [
            {"value": counts["all"], "label": "Applications", "note": "Demo-ready volume", "accent": FRAME_RED},
            {"value": counts["pending"], "label": "Pending", "note": "Needs founder action", "accent": TANGERINE},
            {"value": counts["approved"], "label": "Approved", "note": "Accepted members", "accent": NOOK_BLACK},
            {"value": counts["waitlist"], "label": "Waitlist", "note": "Held for follow-up", "accent": CITRIC},
        ]
    )
    filter_left, filter_mid, filter_right = st.columns([1.1, 0.8, 0.9])
    query = filter_left.text_input("Search applications", placeholder="Name, email, source, activities")
    status_filter = filter_mid.selectbox("Status", ["all", "pending", "approved", "waitlist", "declined"])
    source_filter = filter_right.selectbox("Source", ["all", "organic", "referral"])
    members = data["members"]
    if query.strip():
        needle = query.lower().strip()
        members = [
            member for member in members
            if needle in " ".join(
                [
                    member.get("name", ""),
                    member.get("email", ""),
                    member.get("source", ""),
                    member.get("activities", ""),
                    member.get("intent", ""),
                ]
            ).lower()
        ]
    if status_filter != "all":
        members = [member for member in members if get_admin(member["id"])["status"] == status_filter]
    if source_filter != "all":
        members = [member for member in members if member.get("source", "organic") == source_filter]
    members = sorted(
        members,
        key=lambda member: (
            get_admin(member["id"])["status"] not in {"pending", "waitlist"},
            -smart_member_score(member),
            member["ts"],
        ),
    )
    for member in members:
        admin = get_admin(member["id"])
        recommendation = smart_member_recommendation(member)
        with st.expander(f"{member['name']} · {member['email']} · {admin['status'].title()}"):
            top_left, top_right = st.columns([1.15, 0.85], gap="large")
            with top_left:
                st.markdown(
                    f"""
                    <div class="queue-card">
                      {pill_html(recommendation["label"], recommendation["tone"])}
                      {status_badge(admin["status"])}
                      {tier_badge(admin["tier"])}
                      <h4>{member["name"]}</h4>
                      <div class="subtle">Lead score {smart_member_score(member)} · Source {member.get("source", "organic")} · Submitted {member["ts"]}</div>
                      <p>{member["intent"]}</p>
                      <p style="margin-top:12px"><strong>Activities:</strong> {member["activities"]}<br><strong>Budget:</strong> {member["budget"]}<br><strong>Availability:</strong> {member["availability"]}<br><strong>Newsletter:</strong> {'Yes' if member['newsletter'] == 'yes' else 'No'}<br><strong>Referred by:</strong> {member.get("referred_by") or '—'}</p>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
                quick_a, quick_b, quick_c = st.columns(3)
                if quick_a.button("Accept", key=f"accept_{member['id']}", use_container_width=True, type="primary"):
                    admin["status"] = "approved"
                    sync_referral_status(member["id"], "approved")
                    persist()
                    st.rerun()
                if quick_b.button("Waitlist", key=f"waitlist_{member['id']}", use_container_width=True, type="secondary"):
                    admin["status"] = "waitlist"
                    sync_referral_status(member["id"], "waitlist")
                    persist()
                    st.rerun()
                if quick_c.button("Reject", key=f"reject_{member['id']}", use_container_width=True, type="secondary"):
                    admin["status"] = "declined"
                    sync_referral_status(member["id"], "declined")
                    persist()
                    st.rerun()
            with top_right:
                with st.form(f"member_admin_actions_{member['id']}"):
                    new_tier = st.selectbox("Tier", ["fo", "ibp", "wi", "yhttb"], index=["fo", "ibp", "wi", "yhttb"].index(admin["tier"]), format_func=tier_label)
                    fac_flag = st.checkbox("Facilitator candidate", value=admin["fac"])
                    notes = st.text_area("Founder notes", value=admin["notes"])
                    if st.form_submit_button("Save founder notes", use_container_width=True, type="primary"):
                        admin["tier"] = new_tier
                        admin["fac"] = fac_flag
                        admin["notes"] = notes
                        persist()
                        st.success("Application updated.")
                        st.rerun()


def render_referrals(user: Dict) -> None:
    data = data_store()
    show_header("Referrals", "Facilitators can refer up to three people a month. Founder retains final control over every application.")
    if user["role"] == "founder":
        render_stat_strip(
            [
                {"value": len(data.get("referrals", [])), "label": "All referrals", "note": "Tracked in system", "accent": FRAME_RED},
                {"value": sum(1 for referral in data.get("referrals", []) if referral["status"] == "pending"), "label": "Pending", "note": "Awaiting founder action", "accent": TANGERINE},
                {"value": sum(1 for referral in data.get("referrals", []) if referral["status"] == "approved"), "label": "Approved", "note": "Converted referrals", "accent": NOOK_BLACK},
                {"value": sum(1 for referral in data.get("referrals", []) if referral["status"] == "rejected"), "label": "Rejected", "note": "Closed referrals", "accent": CITRIC},
            ]
        )
        for referral in sorted(data.get("referrals", []), key=lambda item: item["created_at"], reverse=True):
            member = next((candidate for candidate in data["members"] if candidate["id"] == referral["member_id"]), None)
            admin = get_admin(member["id"]) if member else {"status": "pending", "tier": "fo", "notes": "", "fac": False}
            with st.expander(f"{referral['candidate_name']} · referred by {resolve_user_name(referral['fac_id'])}"):
                st.markdown(
                    f"""
                    <div class="queue-card">
                      {pill_html(referral["experience_name"], "citric")}
                      {status_badge(referral["status"] if referral["status"] != "rejected" else "declined")}
                      <h4>{referral["candidate_name"]}</h4>
                      <div class="subtle">{referral["created_at"]} · linked application {admin["status"].title()}</div>
                      <p>{referral["reason"]}</p>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
                actions = st.columns(3)
                if actions[0].button("Approve referral", key=f"approve_referral_{referral['id']}", use_container_width=True, type="primary") and member:
                    referral["status"] = "approved"
                    admin["status"] = "approved"
                    persist()
                    st.rerun()
                if actions[1].button("Waitlist referral", key=f"wait_referral_{referral['id']}", use_container_width=True, type="secondary") and member:
                    referral["status"] = "waitlist"
                    admin["status"] = "waitlist"
                    persist()
                    st.rerun()
                if actions[2].button("Reject referral", key=f"reject_referral_{referral['id']}", use_container_width=True, type="secondary") and member:
                    referral["status"] = "rejected"
                    admin["status"] = "declined"
                    persist()
                    st.rerun()
    else:
        used = monthly_referral_usage(user["id"])
        remaining = max(0, 3 - used)
        render_stat_strip(
            [
                {"value": used, "label": "Used this month", "note": "Referral submissions", "accent": FRAME_RED},
                {"value": remaining, "label": "Remaining", "note": "Out of 3 monthly referrals", "accent": CITRIC},
                {"value": sum(1 for referral in data.get("referrals", []) if referral["fac_id"] == user["id"] and referral["status"] == "approved"), "label": "Approved", "note": "Accepted by founder", "accent": NOOK_BLACK},
                {"value": sum(1 for referral in data.get("referrals", []) if referral["fac_id"] == user["id"] and referral["status"] == "pending"), "label": "Pending", "note": "Still under review", "accent": TANGERINE},
            ]
        )
        with st.expander("Submit referral", expanded=True):
            if used >= 3:
                st.warning("You have used all 3 referrals for this month.")
            else:
                with st.form("new_referral_form"):
                    candidate_name = st.text_input("Candidate name")
                    email = st.text_input("Email")
                    phone = st.text_input("Phone")
                    experience_name = st.selectbox("Best-fit experience", [exp["name"] for exp in upcoming_experiences(limit=6)])
                    reason = st.text_area("Why are you referring this person?")
                    if st.form_submit_button("Submit referral", use_container_width=True, type="primary"):
                        if candidate_name.strip() and email.strip():
                            member_id = f"mref{uuid4().hex[:6]}"
                            data["members"].append(
                                {
                                    "id": member_id,
                                    "name": candidate_name.strip(),
                                    "email": email.strip(),
                                    "phone": phone.strip(),
                                    "budget": "Rs 800-1200",
                                    "availability": "To be confirmed",
                                    "activities": "Referral intake",
                                    "intent": reason.strip() or "Referred by facilitator.",
                                    "cafe": "To be discussed",
                                    "message": "Facilitator referral",
                                    "newsletter": "no",
                                    "sessions": 0,
                                    "ts": datetime.now().strftime("%Y-%m-%d %H:%M"),
                                    "source": "referral",
                                    "referred_by": user["id"],
                                }
                            )
                            data["admin"][member_id] = {"status": "pending", "tier": "fo", "notes": "Referral intake.", "fac": False}
                            data.setdefault("referrals", []).append(
                                {
                                    "id": f"r{uuid4().hex[:6]}",
                                    "fac_id": user["id"],
                                    "member_id": member_id,
                                    "candidate_name": candidate_name.strip(),
                                    "email": email.strip(),
                                    "phone": phone.strip(),
                                    "experience_name": experience_name,
                                    "reason": reason.strip() or "Facilitator referral.",
                                    "created_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
                                    "month": current_month_key(),
                                    "status": "pending",
                                    "founder_note": "",
                                }
                            )
                            persist()
                            st.success("Referral submitted for founder review.")
                            st.rerun()
                        st.error("Candidate name and email are required.")
        st.markdown("<div class='section-title'>My referrals</div>", unsafe_allow_html=True)
        my_referrals = [referral for referral in data.get("referrals", []) if referral["fac_id"] == user["id"]]
        for referral in sorted(my_referrals, key=lambda item: item["created_at"], reverse=True):
            st.markdown(
                f"""
                <div class="queue-card">
                  {pill_html(referral["experience_name"], "citric")}
                  {status_badge(referral["status"] if referral["status"] != "rejected" else "declined")}
                  <h4>{referral["candidate_name"]}</h4>
                  <div class="subtle">{referral["created_at"]}</div>
                  <p>{referral["reason"]}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )


def render_payments() -> None:
    data = data_store()
    show_header("Payments", "Founder-only payments and integrations layer for a smarter backend control room.")
    paid_total = sum(payment["amount"] for payment in data["payments"] if payment["status"] == "paid")
    pending_total = sum(payment["amount"] for payment in data["payments"] if payment["status"] == "pending")
    approved_without_payment = [
        member for member in data["members"]
        if get_admin(member["id"])["status"] == "approved" and not any(payment["member_id"] == member["id"] for payment in data["payments"])
    ]
    render_stat_strip(
        [
            {"value": format_money(paid_total), "label": "Collected", "note": "Marked paid", "accent": FRAME_RED},
            {"value": format_money(pending_total), "label": "Pending", "note": "Outstanding requests", "accent": TANGERINE},
            {"value": len(approved_without_payment), "label": "No payment record", "note": "Needs payment setup", "accent": CITRIC},
            {"value": "Razorpay", "label": "Gateway", "note": "Founder-only configuration", "accent": NOOK_BLACK},
        ]
    )
    left, right = st.columns([1.05, 0.95], gap="large")
    with left:
        st.markdown("<div class='section-title'>Payment Queue</div>", unsafe_allow_html=True)
        for payment in sorted(data["payments"], key=lambda item: (item["status"] != "pending", item["id"])):
            member_name = next((member["name"] for member in data["members"] if member["id"] == payment["member_id"]), payment["member_id"])
            st.markdown(
                f"""
                <div class="queue-card">
                  {pill_html(payment.get("method", "Manual"), "black" if payment["status"] == "paid" else "tangerine")}
                  {status_badge(payment["status"])}
                  <h4>{member_name}</h4>
                  <div class="subtle">{payment["label"]} · {format_money(int(payment["amount"]))}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
            action_left, action_right = st.columns([1, 1])
            if payment["status"] != "paid" and action_left.button("Mark paid", key=f"mark_paid_{payment['id']}", use_container_width=True, type="primary"):
                payment["status"] = "paid"
                persist()
                st.rerun()
            if action_right.button("Remove", key=f"remove_payment_{payment['id']}", use_container_width=True, type="secondary"):
                data["payments"] = [item for item in data["payments"] if item["id"] != payment["id"]]
                persist()
                st.rerun()
    with right:
        st.markdown(
            editorial_card(
                "Razorpay-ready configuration",
                "The app can hold founder-only payment settings here. Real checkout and webhook wiring can be connected once live keys are available.",
                eyebrow="Gateway",
            ),
            unsafe_allow_html=True,
        )
        with st.form("payment_settings_form"):
            settings = data.setdefault("settings", default_data()["settings"])
            razorpay_key_id = st.text_input("Razorpay Key ID", value=settings.get("razorpay_key_id", ""))
            razorpay_key_secret = st.text_input("Razorpay Key Secret", value=settings.get("razorpay_key_secret", ""), type="password")
            payment_link_base = st.text_input("Payment link base", value=settings.get("payment_link_base", ""), placeholder="https://rzp.io/...")
            preferred_ai_api = st.text_input("Preferred AI API", value=settings.get("preferred_ai_api", "OpenAI or Groq"))
            ops_note = st.text_area("Founder integration note", value=settings.get("ops_note", ""))
            if st.form_submit_button("Save payment settings", use_container_width=True, type="primary"):
                settings["razorpay_key_id"] = razorpay_key_id
                settings["razorpay_key_secret"] = razorpay_key_secret
                settings["payment_link_base"] = payment_link_base
                settings["preferred_ai_api"] = preferred_ai_api
                settings["ops_note"] = ops_note
                persist()
                st.success("Settings saved.")
                st.rerun()
        st.markdown("<div class='section-title'>Smart revenue prompts</div>", unsafe_allow_html=True)
        for member in approved_without_payment[:6]:
            if st.button(f"Create payment due for {member['name']}", key=f"create_due_{member['id']}", use_container_width=True, type="secondary"):
                data["payments"].append(
                    {
                        "id": f"p{uuid4().hex[:6]}",
                        "member_id": member["id"],
                        "label": f"{tier_label(get_admin(member['id'])['tier'])} membership",
                        "amount": 499 if get_admin(member["id"])["tier"] == "fo" else 999 if get_admin(member["id"])["tier"] == "ibp" else 1499 if get_admin(member["id"])["tier"] == "wi" else 2499,
                        "status": "pending",
                        "method": "Razorpay link" if settings.get("payment_link_base") else "Manual follow-up",
                    }
                )
                persist()
                st.rerun()
        st.markdown(
            editorial_card(
                "Useful API options",
                "OpenAI or Groq for richer founder summaries and membership-fit suggestions, Razorpay for payment links and checkout, and Google Sheets or Airtable if you want external ops sync later.",
                eyebrow="Integrations",
            ),
            unsafe_allow_html=True,
        )


def render_docs() -> None:
    show_header("Docs", "Founder-facing notes about access, demo data, and optional integrations.")
    st.markdown(
        editorial_card(
            "Control room design",
            "This app is intentionally internal. It now has a private home workspace, founder-only application decisions, facilitator referrals, seeded demo data, payment operations, and dynamic facilitator access.",
            eyebrow="Overview",
        ),
        unsafe_allow_html=True,
    )
    render_stat_strip(
        [
            {"value": len(data_store()["members"]), "label": "Demo applications", "note": "Seeded for presentation", "accent": FRAME_RED},
            {"value": len(data_store().get("referrals", [])), "label": "Referral records", "note": "Tracked monthly", "accent": TANGERINE},
            {"value": "Private", "label": "Home notes", "note": "Visible to owner + founder", "accent": NOOK_BLACK},
            {"value": "Ready", "label": "Payment layer", "note": "Razorpay-ready admin surface", "accent": CITRIC},
        ]
    )
    st.write("- Login page no longer shows any passwords.")
    st.write("- Founder can still reset facilitator passwords privately inside the team management area.")
    st.write("- Facilitators can submit up to 3 referrals per month, but founder still approves or rejects the application.")
    st.write("- The app includes seeded demo records so it feels usable in presentations and walkthroughs.")


def sidebar_navigation(user: Dict) -> str:
    founder_pages = [
        "Home",
        "Dashboard",
        "Applications",
        "Referrals",
        "Planner",
        "Payments",
        "Facilitator Team",
        "Leave",
        "Messages",
        "Docs",
    ]
    facilitator_pages = [
        "Home",
        "Dashboard",
        "My Sessions",
        "Referrals",
        "My Profile",
        "Leave",
        "Messages",
    ]
    options = founder_pages if user["role"] == "founder" else facilitator_pages
    if st.session_state.get("page") not in options:
        st.session_state.page = "Home"
    with st.sidebar:
        st.markdown(
            f"""
            <div class="sidebar-brand">
              <div class="eyebrow">Nook</div>
              <h3>{user['name']}</h3>
              <div class="subtle">{user['role'].title()} route</div>
              <div class="swatch-row">
                <div class="swatch" style="background:{FRAME_RED}"></div>
                <div class="swatch" style="background:{PAPER}"></div>
                <div class="swatch" style="background:{NOOK_BLACK}"></div>
              </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.caption("Navigation")
        for page in options:
            is_active = st.session_state.page == page
            if st.button(page, key=f"nav_new_{page}", use_container_width=True, type="primary" if is_active else "secondary"):
                st.session_state.page = page
        st.markdown("---")
        if st.button("Log out", use_container_width=True, type="secondary"):
            st.session_state.pop("current_user", None)
            st.rerun()
    return st.session_state.page


def main() -> None:
    st.set_page_config(page_title="Nook Control Room", page_icon="N", layout="wide", initial_sidebar_state="expanded")
    if current_user() is None:
        login_screen()
        return

    inject_css()
    user = current_user()
    if user["role"] == "facilitator" and not any(account["id"] == user["id"] for account in all_accounts()):
        st.session_state.pop("current_user", None)
        st.rerun()
    page = sidebar_navigation(user)

    if page == "Home":
        render_home(user)
    elif page == "Dashboard":
        render_dashboard(user)
    elif page == "Applications":
        render_members()
    elif page == "Referrals":
        render_referrals(user)
    elif page == "Planner":
        render_planner()
    elif page == "Payments":
        render_payments()
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
