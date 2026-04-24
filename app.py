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
BORDER = "rgba(17,16,14,0.10)"

FOUNDER_ACCOUNT = {"id": "manju", "name": "Manju Singh", "role": "founder", "password": "founder2026"}

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
        "transport": "Auto cluster, approx Rs 40/person",
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
        elif isinstance(data[key], dict) and isinstance(value, dict):
            data[key].update(value)
        else:
            data[key] = value
    return data


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
    data = data or data_store()
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


def authenticate(username: str, password: str) -> Optional[Dict]:
    for user in all_accounts():
        if user["id"] == username and user["password"] == password:
            return user
    return None


def get_admin(member_id: str) -> Dict:
    data = data_store()
    member = next((m for m in data["members"] if m["id"] == member_id), None)
    fallback_tier = auto_tier(member.get("sessions", 0) if member else 0)
    return data["admin"].setdefault(member_id, {"status": "pending", "tier": fallback_tier, "notes": "", "fac": False})


def get_fac(fid: str) -> Optional[Dict]:
    return next((fac for fac in data_store()["facs"] if fac["id"] == fid), None)


def on_leave(fid: str) -> bool:
    today = date.today().isoformat()
    return any(item["fid"] == fid and item["from"] <= today <= item["to"] for item in data_store()["leaves"])


def upcoming_experiences(limit: Optional[int] = None) -> List[Dict]:
    items = sorted(data_store()["exps"], key=lambda exp: (exp.get("date", "9999-12-31"), exp.get("time", "23:59")))
    return items[:limit] if limit else items


def tier_label(code: str) -> str:
    return {"fo": "First Out", "ibp": "In Between Plans", "wi": "Worth It", "yhttb": "YHTTB"}.get(code, code.upper())


def tier_rank(code: str) -> int:
    return {"fo": 1, "ibp": 2, "wi": 3, "yhttb": 4}.get(code, 0)


def format_money(amount: int) -> str:
    return f"Rs {amount:,}"


def current_month_key() -> str:
    return datetime.now().strftime("%Y-%m")


def monthly_referral_usage(fac_user_id: str, month_key: Optional[str] = None) -> int:
    month_key = month_key or current_month_key()
    return sum(1 for referral in data_store().get("referrals", []) if referral["fac_id"] == fac_user_id and referral["month"] == month_key)


def visible_private_entries(user: Dict) -> List[Dict]:
    entries = data_store().get("private_entries", [])
    if user["role"] == "founder":
        return sorted(entries, key=lambda item: item["created_at"], reverse=True)
    return sorted([item for item in entries if item["owner_id"] == user["id"]], key=lambda item: item["created_at"], reverse=True)


def sync_referral_status(member_id: str, new_status: str) -> None:
    referral_map = {"approved": "approved", "waitlist": "waitlist", "declined": "rejected"}
    for referral in data_store().get("referrals", []):
        if referral.get("member_id") == member_id:
            referral["status"] = referral_map.get(new_status, referral["status"])


def facilitator_session_load(fid: str) -> int:
    return sum(1 for exp in data_store()["exps"] if exp.get("fac") == fid)


def smart_member_score(member: Dict) -> int:
    admin = get_admin(member["id"])
    text_blob = " ".join(
        [member.get("intent", "").lower(), member.get("activities", "").lower(), member.get("message", "").lower(), member.get("availability", "").lower()]
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
        if fac["status"] != "active" or on_leave(fac["id"]):
            continue
        access_gap = tier_rank(fac.get("access", "fo")) - tier_rank(exp.get("tier", "fo"))
        if access_gap < 0:
            continue
        score = 70 + min(fac.get("sessions", 0), 12) + (6 - access_gap * 2) - facilitator_session_load(fac["id"]) * 4
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
            alerts.append({"title": f"Next session: {next_session['name']}", "detail": f"{next_session['date']} at {next_session['time']} · {next_session['venue']}", "tone": "aqua"})
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
    flagged = [member for member in data["members"] if get_admin(member["id"])["fac"]]
    if flagged:
        alerts.append({"title": f"{len(flagged)} facilitator candidate(s)", "detail": "Promising members are ready for onboarding review.", "tone": "fuchsia"})
    for exp in upcoming_experiences(limit=5):
        if not exp.get("fac"):
            alerts.append({"title": f"{exp['name']} has no facilitator", "detail": "Assign an active facilitator before the session goes live.", "tone": "tangerine"})
        elif on_leave(exp["fac"]):
            fac = get_fac(exp["fac"])
            alerts.append({"title": f"{fac['name'] if fac else 'Assigned facilitator'} is on leave", "detail": f"Reassign {exp['name']} or update leave dates.", "tone": "tangerine"})
    stale_pending = [
        member for member in data["members"]
        if get_admin(member["id"])["status"] == "pending"
        and datetime.now() - datetime.strptime(member["ts"], "%Y-%m-%d %H:%M") > timedelta(days=5)
    ]
    if stale_pending:
        alerts.append({"title": f"{len(stale_pending)} pending lead(s) are aging", "detail": "Those members have waited more than five days for a decision.", "tone": "citric"})
    return alerts[:4]


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
    lower_theme = theme_clean.lower()
    if any(word in lower_theme for word in ["paint", "canvas", "art", "sketch"]):
        activity = "Paired visual creation with hidden prompts, then a mid-point swap so people build on each other's work."
    elif any(word in lower_theme for word in ["dinner", "supper", "food", "tasting"]):
        activity = "A guided tasting arc where each course unlocks a conversation direction and one shared choice."
    elif any(word in lower_theme for word in ["walk", "route", "city", "trail"]):
        activity = "A structured movement-based experience with check-in stops and one reflective prompt at each pivot."
    elif any(word in lower_theme for word in ["pottery", "clay", "craft", "studio"]):
        activity = "Hands-on making session where pairs trade interpretation rather than working in isolation."

    transport = "Founder-arranged cab clusters."
    if "walk" in venue_key or "old city" in venue_key:
        transport = "Walkable route with one fixed regroup point."
    elif "cafe" in venue_key or "studio" in venue_key:
        transport = "Auto and cab mix with clear arrival timing."

    return {
        "name": theme_clean,
        "act1": opener_map.get(mood_key, opener_map["calm"]),
        "act2": activity,
        "act3": unwind_map.get(tier, unwind_map["fo"]),
        "transport": transport,
        "notes": f"Keep the room feeling {mood.lower()} and intentional. Prioritize {tier_label(tier)} expectations and make sure the venue supports easy conversation flow.",
    }


def status_badge(status: str) -> str:
    styles = {
        "pending": (CITRIC, NOOK_BLACK, "rgba(216,92,26,0.22)"),
        "approved": (AQUAMARINE, NOOK_BLACK, "rgba(17,16,14,0.12)"),
        "declined": (TANGERINE, PAPER_ALT, "rgba(216,92,26,0.28)"),
        "waitlist": (FUCHSIA, PAPER_ALT, "rgba(17,16,14,0.10)"),
        "active": (AQUAMARINE, NOOK_BLACK, "rgba(17,16,14,0.12)"),
        "candidate": (CITRIC, NOOK_BLACK, "rgba(216,92,26,0.22)"),
        "offboarded": (NOOK_BLACK, PAPER_ALT, "rgba(17,16,14,0.16)"),
        "paid": (AQUAMARINE, NOOK_BLACK, "rgba(17,16,14,0.12)"),
    }
    bg, fg, border = styles.get(status, (TANGERINE, PAPER_ALT, "rgba(216,92,26,0.28)"))
    return f"<span style='padding:4px 10px;border-radius:999px;background:{bg};color:{fg};border:1px solid {border};font-size:12px;font-weight:700;letter-spacing:0.02em'>{status.title()}</span>"


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
    return f"<span class='pill' style='background:{bg};color:{fg};border:1px solid {border};'>{text}</span>"


def tier_badge(code: str) -> str:
    tone = {"fo": "klein", "ibp": "aqua", "wi": "citric", "yhttb": "fuchsia"}.get(code, "tangerine")
    return pill_html(tier_label(code), tone)


def insight_card_html(title: str, detail: str, tone: str = "tangerine") -> str:
    return f"<div class='insight-card'>{pill_html(title, tone=tone)}<p>{detail}</p></div>"


def editorial_card(title: str, body: str, eyebrow: Optional[str] = None) -> str:
    eyebrow_html = f"<div class='eyebrow'>{eyebrow}</div>" if eyebrow else ""
    return f"<div class='content-panel'>{eyebrow_html}<h3>{title}</h3><p>{body}</p></div>"


def render_stat_strip(items: List[Dict]) -> None:
    html = "<div class='stats-grid'>"
    for index, item in enumerate(items):
        tone = "accent" if index == 0 else "dark" if index == len(items) - 1 else "light"
        html += (
            f"<div class='stat-card stat-card--{tone}'>"
            f"<div class='stat-rule' style='background:{item.get('accent', FRAME_RED)}'></div>"
            f"<div class='stat-value'>{item['value']}</div>"
            f"<div class='stat-label'>{item['label']}</div>"
            f"<div class='stat-copy'>{item.get('note', '')}</div>"
            "</div>"
        )
    html += "</div>"
    st.markdown(html, unsafe_allow_html=True)


def show_header(title: str, subtitle: str) -> None:
    st.markdown(
        f"""
        <div class='page-header page-header-grid'>
          <div>
            <div class='eyebrow'>Nook / {title}</div>
            <div class='page-title'>{title}</div>
            <div class='page-subtitle'>{subtitle}</div>
          </div>
          <div class='page-chip-stack'>
            <span class='page-chip page-chip--dark'>Private system</span>
            <span class='page-chip'>Founder led</span>
            <span class='page-chip'>Orange accent</span>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def inject_css() -> None:
    st.markdown(
        f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Archivo:wght@700;800;900&family=Space+Grotesk:wght@400;500;700&display=swap');
        html, body, [class*="css"] {{ font-family: "Space Grotesk", sans-serif; color: {INK}; }}
        body, .stApp {{
            background:
                radial-gradient(circle at top left, rgba(255,90,43,0.06), transparent 22%),
                radial-gradient(circle at 88% 12%, rgba(216,92,26,0.08), transparent 18%),
                linear-gradient(180deg, #ece9e4 0%, #f5f3ef 38%, #f2efea 100%);
        }}
        .block-container {{ max-width: 1280px; padding: 18px 28px 64px 28px; }}
        h1, h2, h3, h4, .page-title, .hero-title, .section-title {{ font-family: "Archivo", sans-serif; letter-spacing: -0.04em; color: {INK}; }}
        [data-testid="stSidebar"] {{
            background: rgba(255,255,255,0.72);
            border-right: 1px solid rgba(18,17,16,0.08);
            backdrop-filter: blur(18px);
        }}
        [data-testid="stSidebar"] .block-container {{ padding: 18px 14px 24px 14px; }}
        .sidebar-card, .brand-panel, .route-panel, .content-panel, .queue-card, .session-card, .insight-card, .stExpander, div[data-testid="stForm"], [data-testid="stAlert"] {{
            background: rgba(255,255,255,0.92);
            border: 1px solid rgba(18,17,16,0.08);
            border-radius: 28px;
            box-shadow: 0 22px 44px rgba(18,17,16,0.08);
        }}
        .sidebar-card, .content-panel, .queue-card, .session-card, .insight-card {{ padding: 22px; }}
        .sidebar-card h3 {{ margin: 0 0 4px 0; color: #fff6ef !important; font-size: 22px; font-family: "Space Grotesk", sans-serif; font-weight: 700; }}
        .sidebar-card {{
            background:
                radial-gradient(circle at 84% 16%, rgba(255,160,115,0.22), transparent 18%),
                linear-gradient(180deg, #0f0f10 0%, #191514 100%);
        }}
        .sidebar-accent {{
            width: 100%;
            height: 10px;
            margin-top: 14px;
            border-radius: 999px;
            background: linear-gradient(90deg, #ffd8c2 0%, #ff8f59 45%, #ff5b2b 100%);
        }}
        .shell-topbar {{
            display: grid;
            grid-template-columns: 1.35fr 0.85fr;
            gap: 20px;
            margin-bottom: 18px;
        }}
        .brand-panel, .route-panel {{ padding: 24px; }}
        .brand-panel {{
            min-height: 190px;
            background:
                radial-gradient(circle at 85% 18%, rgba(255,98,45,0.15), transparent 18%),
                linear-gradient(180deg, rgba(255,255,255,0.96), rgba(250,249,246,0.96));
        }}
        .route-panel {{
            background:
                radial-gradient(circle at top right, rgba(255,94,52,0.22), transparent 18%),
                linear-gradient(180deg, #ffffff 0%, #fbfaf7 100%);
        }}
        .brand-title {{
            font-family: "Archivo", sans-serif;
            font-size: clamp(34px, 4.4vw, 64px);
            line-height: 0.9;
            text-transform: uppercase;
            max-width: 9ch;
        }}
        .page-header {{
            margin: 0 0 22px 0;
            padding: 10px 0 18px 0;
            border-bottom: 1px solid rgba(18,17,16,0.08);
        }}
        .page-header-grid {{
            display: grid;
            grid-template-columns: 1.15fr 0.85fr;
            gap: 20px;
            align-items: end;
        }}
        .page-title {{ font-size: clamp(38px, 5.5vw, 72px); line-height: 0.9; margin-bottom: 8px; text-transform: uppercase; max-width: 8ch; }}
        .page-subtitle, .subtle, .content-panel p, .queue-card p, .insight-card p, .session-card p, .brand-copy, .route-copy {{ color: {SOFT_INK}; line-height: 1.7; }}
        .hero-shell {{ display: grid; grid-template-columns: 1.18fr 0.82fr; gap: 22px; margin-bottom: 24px; }}
        .hero-panel {{
            background: linear-gradient(180deg, rgba(255,255,255,0.98), rgba(249,248,245,0.96));
            border: 1px solid rgba(18,17,16,0.08);
            border-radius: 36px;
            box-shadow: 0 24px 54px rgba(18,17,16,0.08);
            padding: 30px;
        }}
        .hero-panel--dark {{
            background:
                radial-gradient(circle at 82% 18%, rgba(255,120,78,0.30), transparent 16%),
                linear-gradient(180deg, #111111 0%, #171514 100%);
            color: #fff9f4;
            border-color: rgba(255,255,255,0.06);
        }}
        .hero-panel--accent {{
            background:
                linear-gradient(135deg, #ff5a2c 0%, #ff6b37 32%, #ffb38b 100%);
            color: #130f0d;
        }}
        .hero-title {{ font-size: clamp(56px, 8vw, 96px); line-height: 0.84; text-transform: uppercase; margin-bottom: 16px; max-width: 7ch; }}
        .hero-kicker {{ display: inline-block; padding: 8px 14px; border-radius: 999px; border: 1px solid rgba(18,17,16,0.10); font-size: 11px; font-weight: 700; letter-spacing: 0.18em; text-transform: uppercase; margin-bottom: 18px; }}
        .hero-item {{ display: grid; grid-template-columns: auto 1fr; gap: 12px; align-items: start; padding-top: 12px; border-top: 1px solid rgba(18,17,16,0.10); }}
        .hero-item strong, .stat-label, .route-title, .eyebrow {{ font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.18em; color: {FRAME_RED}; }}
        .hero-panel--dark .eyebrow, .hero-panel--dark .hero-copy, .hero-panel--dark .section-title {{ color: #fff7f1 !important; }}
        .hero-panel--accent .eyebrow, .hero-panel--accent .hero-copy, .hero-panel--accent .section-title {{ color: #130f0d !important; }}
        .hero-thumb-grid {{
            display: grid;
            grid-template-columns: repeat(2, minmax(0, 1fr));
            gap: 14px;
            margin-top: 18px;
        }}
        .hero-thumb {{
            min-height: 118px;
            border-radius: 24px;
            border: 1px solid rgba(18,17,16,0.08);
            background: linear-gradient(135deg, #f5f2ee 0%, #ffffff 100%);
            overflow: hidden;
            position: relative;
        }}
        .hero-thumb--accent {{
            background: linear-gradient(135deg, #ff5d31 0%, #ff8a5a 60%, #ffd3bf 100%);
        }}
        .hero-thumb--dark {{
            background: linear-gradient(135deg, #121212 0%, #22201e 100%);
        }}
        .hero-thumb::after {{
            content: "";
            position: absolute;
            inset: auto -8% -28% auto;
            width: 120px;
            height: 120px;
            border-radius: 28px;
            background: rgba(255,255,255,0.24);
            transform: rotate(24deg);
        }}
        .stats-grid {{ display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 18px; margin: 0 0 26px 0; }}
        .stat-card {{ border-radius: 20px; border: 1px solid rgba(18,17,16,0.10); padding: 18px; box-shadow: 0 18px 38px rgba(18,17,16,0.08); min-height: 150px; }}
        .stat-card--light {{ background: #fffdfa; color: {INK}; }}
        .stat-card--accent {{ background: linear-gradient(135deg, #fff0e7 0%, #ffd4bd 100%); color: {INK}; }}
        .stat-card--dark {{ background: linear-gradient(180deg, #171310 0%, #201915 100%); color: #fff6ef; border-color: rgba(255,255,255,0.06); }}
        .stat-rule {{ width: 56px; height: 6px; border-radius: 999px; margin-bottom: 18px; }}
        .stat-value {{ font-family: "Archivo", sans-serif; font-size: clamp(28px, 3vw, 48px); line-height: 1; margin-bottom: 10px; }}
        .stat-copy {{ font-size: 13px; line-height: 1.6; opacity: 0.82; }}
        .content-panel h3, .queue-card h4, .session-card strong {{ margin: 0 0 10px 0; }}
        .content-panel h3, .queue-card h4, .session-card strong, .section-title {{ text-transform: uppercase; }}
        .content-panel, .queue-card, .session-card, .insight-card {{
            position: relative;
            overflow: hidden;
        }}
        .content-panel::after, .queue-card::after, .session-card::after, .insight-card::after {{
            content: "";
            position: absolute;
            top: -18px;
            right: -12px;
            width: 88px;
            height: 88px;
            border-radius: 28px;
            background: linear-gradient(135deg, rgba(255,95,46,0.12), rgba(255,95,46,0.02));
            transform: rotate(24deg);
        }}
        .pill {{ display: inline-block; margin: 0 8px 10px 0; padding: 6px 12px; border-radius: 999px; font-size: 11px; font-weight: 700; letter-spacing: 0.10em; text-transform: uppercase; }}
        .queue-card, .session-card, .insight-card {{ margin-bottom: 14px; }}
        .page-chip-stack {{
            display: flex;
            flex-wrap: wrap;
            justify-content: flex-end;
            gap: 10px;
            align-self: start;
        }}
        .page-chip {{
            display: inline-flex;
            align-items: center;
            padding: 10px 16px;
            border-radius: 999px;
            border: 1px solid rgba(18,17,16,0.08);
            background: rgba(255,255,255,0.84);
            font-size: 11px;
            font-weight: 700;
            letter-spacing: 0.14em;
            text-transform: uppercase;
        }}
        .page-chip--dark {{
            background: #111111;
            color: #fff8f2;
            border-color: rgba(255,255,255,0.06);
        }}
        .stExpander {{ border-radius: 20px; overflow: hidden; }}
        .stExpander details summary p {{ font-weight: 700; color: {INK} !important; }}
        div[data-testid="stForm"] {{ padding: 12px 14px 18px 14px; margin-bottom: 14px; }}
        div[data-baseweb="input"] > div, div[data-baseweb="select"] > div, div[data-baseweb="textarea"] > div, .stTextInput input, .stTextArea textarea, .stDateInput input, .stNumberInput input {{ background: #ffffff; color: {INK}; border: 1px solid rgba(18,17,16,0.10); border-radius: 14px; }}
        div[data-baseweb="input"] input, div[data-baseweb="select"] *, div[data-baseweb="textarea"] textarea, .stDateInput *, .stNumberInput input {{ color: {INK} !important; }}
        .stTextInput label, .stTextArea label, .stDateInput label, .stSelectbox label, .stNumberInput label {{ font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.14em; color: {SOFT_INK} !important; }}
        .stButton > button, .stForm [data-testid="stFormSubmitButton"] > button {{ min-height: 2.9rem; border-radius: 14px; border: 1px solid rgba(18,17,16,0.10); background: #fffdfa; color: {INK}; font-weight: 700; letter-spacing: 0.07em; text-transform: uppercase; }}
        .stButton > button[kind="primary"], .stForm [data-testid="stFormSubmitButton"] > button[kind="primary"] {{ background: linear-gradient(135deg, #ffd9c1 0%, #ffb07d 42%, #ff8d59 100%); border-color: rgba(216,92,26,0.18); color: {INK}; }}
        @media (max-width: 1080px) {{
            .shell-topbar, .hero-shell, .page-header-grid {{ grid-template-columns: 1fr; }}
            .stats-grid {{ grid-template-columns: repeat(2, minmax(0, 1fr)); }}
            .page-chip-stack {{ justify-content: flex-start; }}
        }}
        @media (max-width: 700px) {{ .block-container {{ padding: 16px 14px 44px 14px; }} .hero-title {{ font-size: clamp(42px, 16vw, 62px); }} .stats-grid {{ grid-template-columns: 1fr; }} }}
        </style>
        """,
        unsafe_allow_html=True,
    )


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
        left, right = st.columns([1.2, 0.8], gap="large")
        priority_members = sorted(
            data["members"],
            key=lambda member: (get_admin(member["id"])["status"] not in {"pending", "waitlist"}, -smart_member_score(member), member["ts"]),
        )[:4]
        with left:
            st.markdown("<div class='section-title'>Priority queue</div>", unsafe_allow_html=True)
            for member in priority_members:
                admin = get_admin(member["id"])
                recommendation = smart_member_recommendation(member)
                st.markdown(
                    f"<div class='queue-card'>{pill_html(recommendation['label'], recommendation['tone'])}{status_badge(admin['status'])}{tier_badge(admin['tier'])}<h4>{member['name']}</h4><div class='subtle'>Lead score {smart_member_score(member)} · {member['email']} · {member['availability']}</div><p>{member['intent']}</p></div>",
                    unsafe_allow_html=True,
                )
        with right:
            st.markdown("<div class='section-title'>Live alerts</div>", unsafe_allow_html=True)
            for alert in smart_operational_alerts(user):
                st.markdown(insight_card_html(alert["title"], alert["detail"], alert["tone"]), unsafe_allow_html=True)
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
        left, right = st.columns([1.08, 0.92], gap="large")
        with left:
            st.markdown("<div class='section-title'>Facilitator focus</div>", unsafe_allow_html=True)
            if not my_sessions:
                st.info("No sessions assigned yet.")
            for exp in my_sessions:
                st.markdown(
                    f"<div class='session-card'>{tier_badge(exp['tier'])}<strong>{exp['name']}</strong><br><span class='subtle'>{exp['date']} · {exp['time']} · {exp['venue']} · Max {exp['max']}</span><hr style='border-color:{LINE}'><div class='subtle'><strong>Act 1:</strong> {exp['act1']}</div><div class='subtle'><strong>Act 2:</strong> {exp['act2']}</div><div class='subtle'><strong>Act 3:</strong> {exp['act3']}</div></div>",
                    unsafe_allow_html=True,
                )
        with right:
            st.markdown("<div class='section-title'>Live alerts</div>", unsafe_allow_html=True)
            for alert in smart_operational_alerts(user):
                st.markdown(insight_card_html(alert["title"], alert["detail"], alert["tone"]), unsafe_allow_html=True)


def render_home(user: Dict) -> None:
    data = data_store()
    show_header("Home", "A private workspace for personal notes and operating updates. Entries stay visible to the owner and the founder only.")
    render_stat_strip(
        [
            {"value": len(visible_private_entries(user)), "label": "Visible entries", "note": "Private workspace items", "accent": FRAME_RED},
            {"value": monthly_referral_usage(user["id"]) if user["role"] == "facilitator" else len(data.get("referrals", [])), "label": "Referral load", "note": "This month or total queue", "accent": TANGERINE},
            {"value": len(smart_operational_alerts(user)), "label": "Smart alerts", "note": "Actionable cues", "accent": NOOK_BLACK},
            {"value": len([msg for msg in data["msgs"] if msg["to"] == user["id"] and not msg["read"]]) if user["role"] != "founder" else len([msg for msg in data["msgs"] if msg["to"] == "manju" and not msg["read"]]), "label": "Unread", "note": "Internal messages", "accent": CITRIC},
        ]
    )
    left, right = st.columns([1.08, 0.92], gap="large")
    with left:
        st.markdown(editorial_card("Private desk", "Write notes, reminders, and operating reads in one place. It is visible only to you and the founder.", "Workspace"), unsafe_allow_html=True)
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
        st.markdown("<div class='section-title'>My private entries</div>", unsafe_allow_html=True)
        mine = [entry for entry in visible_private_entries(user) if entry["owner_id"] == "manju"] if user["role"] == "founder" else visible_private_entries(user)
        if not mine:
            st.info("No private entries yet.")
        for entry in mine[:8]:
            st.markdown(
                f"<div class='queue-card'>{pill_html(entry['kind'].title(), 'black' if entry['kind'] == 'note' else 'tangerine')}<h4>{entry['title']}</h4><div class='subtle'>{entry['created_at']}</div><p>{entry['body']}</p></div>",
                unsafe_allow_html=True,
            )
    with right:
        st.markdown("<div class='section-title'>Smart suggestions</div>", unsafe_allow_html=True)
        for alert in smart_operational_alerts(user):
            st.markdown(insight_card_html(alert["title"], alert["detail"], alert["tone"]), unsafe_allow_html=True)
        if user["role"] == "founder":
            st.markdown("<div class='section-title'>Team private feed</div>", unsafe_allow_html=True)
            owners = ["All facilitators", *[fac["uid"] for fac in data["facs"] if fac["status"] != "offboarded"]]
            selected_owner = st.selectbox("Filter by facilitator", owners)
            team_entries = [
                entry for entry in data.get("private_entries", [])
                if entry["owner_id"] != "manju" and (selected_owner == "All facilitators" or entry["owner_id"] == selected_owner)
            ]
            for entry in sorted(team_entries, key=lambda item: item["created_at"], reverse=True)[:8]:
                st.markdown(
                    f"<div class='queue-card'>{pill_html(resolve_user_name(entry['owner_id']), 'citric')}<h4>{entry['title']}</h4><div class='subtle'>{entry['created_at']}</div><p>{entry['body']}</p></div>",
                    unsafe_allow_html=True,
                )
        else:
            st.markdown(editorial_card("Access rule", "Your notes and updates are visible only to you and the founder. Other facilitators cannot read them.", "Reminder"), unsafe_allow_html=True)


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
    query_col, status_col, source_col = st.columns([1.1, 0.8, 0.9])
    query = query_col.text_input("Search applications", placeholder="Name, email, source, activities")
    status_filter = status_col.selectbox("Status", ["all", "pending", "approved", "waitlist", "declined"])
    source_filter = source_col.selectbox("Source", ["all", "organic", "referral"])
    members = data["members"]
    if query.strip():
        needle = query.lower().strip()
        members = [member for member in members if needle in " ".join([member.get("name", ""), member.get("email", ""), member.get("source", ""), member.get("activities", ""), member.get("intent", "")]).lower()]
    if status_filter != "all":
        members = [member for member in members if get_admin(member["id"])["status"] == status_filter]
    if source_filter != "all":
        members = [member for member in members if member.get("source", "organic") == source_filter]
    members = sorted(members, key=lambda member: (get_admin(member["id"])["status"] not in {"pending", "waitlist"}, -smart_member_score(member), member["ts"]))
    for member in members:
        admin = get_admin(member["id"])
        recommendation = smart_member_recommendation(member)
        with st.expander(f"{member['name']} · {member['email']} · {admin['status'].title()}"):
            top_left, top_right = st.columns([1.15, 0.85], gap="large")
            with top_left:
                st.markdown(
                    f"<div class='queue-card'>{pill_html(recommendation['label'], recommendation['tone'])}{status_badge(admin['status'])}{tier_badge(admin['tier'])}<h4>{member['name']}</h4><div class='subtle'>Lead score {smart_member_score(member)} · Source {member.get('source', 'organic')} · Submitted {member['ts']}</div><p>{member['intent']}</p><p><strong>Activities:</strong> {member['activities']}<br><strong>Budget:</strong> {member['budget']}<br><strong>Availability:</strong> {member['availability']}<br><strong>Newsletter:</strong> {'Yes' if member['newsletter'] == 'yes' else 'No'}<br><strong>Referred by:</strong> {member.get('referred_by') or '—'}</p></div>",
                    unsafe_allow_html=True,
                )
                a, b, c = st.columns(3)
                if a.button("Accept", key=f"accept_{member['id']}", use_container_width=True, type="primary"):
                    admin["status"] = "approved"
                    sync_referral_status(member["id"], "approved")
                    persist()
                    st.rerun()
                if b.button("Waitlist", key=f"waitlist_{member['id']}", use_container_width=True, type="secondary"):
                    admin["status"] = "waitlist"
                    sync_referral_status(member["id"], "waitlist")
                    persist()
                    st.rerun()
                if c.button("Reject", key=f"reject_{member['id']}", use_container_width=True, type="secondary"):
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
            admin = get_admin(member["id"]) if member else {"status": "pending"}
            with st.expander(f"{referral['candidate_name']} · referred by {resolve_user_name(referral['fac_id'])}"):
                st.markdown(
                    f"<div class='queue-card'>{pill_html(referral['experience_name'], 'citric')}{status_badge(referral['status'] if referral['status'] != 'rejected' else 'declined')}<h4>{referral['candidate_name']}</h4><div class='subtle'>{referral['created_at']} · linked application {admin['status'].title()}</div><p>{referral['reason']}</p></div>",
                    unsafe_allow_html=True,
                )
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
        for referral in sorted([item for item in data.get("referrals", []) if item["fac_id"] == user["id"]], key=lambda item: item["created_at"], reverse=True):
            st.markdown(
                f"<div class='queue-card'>{pill_html(referral['experience_name'], 'citric')}{status_badge(referral['status'] if referral['status'] != 'rejected' else 'declined')}<h4>{referral['candidate_name']}</h4><div class='subtle'>{referral['created_at']}</div><p>{referral['reason']}</p></div>",
                unsafe_allow_html=True,
            )


def render_planner() -> None:
    data = data_store()
    show_header("Planner", "Design sessions with smarter structure, staffing suggestions, and cleaner founder control.")
    if "planner_name" not in st.session_state:
        st.session_state.planner_name = ""
        st.session_state.planner_tier = "fo"
        st.session_state.planner_venue = ""
        st.session_state.planner_act1 = ""
        st.session_state.planner_act2 = ""
        st.session_state.planner_act3 = ""
        st.session_state.planner_transport = ""
        st.session_state.planner_notes = ""
    with st.expander("Smart blueprint builder", expanded=False):
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
    with st.expander("Create new experience", expanded=True):
        with st.form("new_experience"):
            c1, c2, c3 = st.columns(3)
            name = c1.text_input("Experience name", key="planner_name")
            tier = c2.selectbox("Tier", ["fo", "ibp", "wi", "yhttb"], format_func=tier_label, key="planner_tier")
            fac_map = {"Unassigned": ""}
            for fac in [item for item in data["facs"] if item["status"] != "offboarded"]:
                fac_map[fac["name"]] = fac["id"]
            fac_name = c3.selectbox("Facilitator", list(fac_map.keys()))
            d1, d2, d3, d4 = st.columns(4)
            exp_date = d1.date_input("Date", value=date.today())
            exp_time = d2.text_input("Time", value="18:00")
            capacity = d3.number_input("Max attendees", min_value=1, value=8)
            price = d4.number_input("Price per person", min_value=0, value=500)
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
    st.markdown("<div class='section-title'>Experience deck</div>", unsafe_allow_html=True)
    for exp in upcoming_experiences():
        fac = get_fac(exp["fac"]) if exp.get("fac") else None
        suggestion = recommended_facilitator(exp) if (not fac or on_leave(fac["id"])) else None
        with st.expander(f"{exp['name']} · {exp['date']}"):
            st.markdown(
                f"<div class='session-card'>{tier_badge(exp['tier'])}<strong>{exp['name']}</strong><br><span class='subtle'>{exp['time']} · {exp['venue']} · Max {exp['max']} · {format_money(int(exp['price']))}</span><br><span class='subtle'>Assigned facilitator: {fac['name'] if fac else 'Unassigned'}{' · on leave' if fac and on_leave(fac['id']) else ''}</span></div>",
                unsafe_allow_html=True,
            )
            st.write(f"Act 1: {exp['act1']}")
            st.write(f"Act 2: {exp['act2']}")
            st.write(f"Act 3: {exp['act3']}")
            if suggestion and st.button(f"Assign {suggestion['name']}", key=f"assign_{exp['id']}", use_container_width=True, type="secondary"):
                exp["fac"] = suggestion["id"]
                persist()
                st.rerun()
            if st.button("Delete experience", key=f"delete_{exp['id']}", use_container_width=True, type="secondary"):
                data["exps"] = [item for item in data["exps"] if item["id"] != exp["id"]]
                persist()
                st.rerun()


def render_payments() -> None:
    data = data_store()
    show_header("Payments", "Founder-only payments and integrations layer for a smarter backend control room.")
    paid_total = sum(payment["amount"] for payment in data["payments"] if payment["status"] == "paid")
    pending_total = sum(payment["amount"] for payment in data["payments"] if payment["status"] == "pending")
    approved_without_payment = [member for member in data["members"] if get_admin(member["id"])["status"] == "approved" and not any(payment["member_id"] == member["id"] for payment in data["payments"])]
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
        st.markdown("<div class='section-title'>Payment queue</div>", unsafe_allow_html=True)
        for payment in sorted(data["payments"], key=lambda item: (item["status"] != "pending", item["id"])):
            member_name = next((member["name"] for member in data["members"] if member["id"] == payment["member_id"]), payment["member_id"])
            st.markdown(
                f"<div class='queue-card'>{pill_html(payment.get('method', 'Manual'), 'black' if payment['status'] == 'paid' else 'tangerine')}{status_badge(payment['status'])}<h4>{member_name}</h4><div class='subtle'>{payment['label']} · {format_money(int(payment['amount']))}</div></div>",
                unsafe_allow_html=True,
            )
    with right:
        settings = data.setdefault("settings", default_data()["settings"])
        with st.form("payment_settings_form"):
            settings["razorpay_key_id"] = st.text_input("Razorpay Key ID", value=settings.get("razorpay_key_id", ""))
            settings["razorpay_key_secret"] = st.text_input("Razorpay Key Secret", value=settings.get("razorpay_key_secret", ""), type="password")
            settings["payment_link_base"] = st.text_input("Payment link base", value=settings.get("payment_link_base", ""))
            settings["preferred_ai_api"] = st.text_input("Preferred AI API", value=settings.get("preferred_ai_api", "OpenAI or Groq"))
            settings["ops_note"] = st.text_area("Founder integration note", value=settings.get("ops_note", ""))
            if st.form_submit_button("Save payment settings", use_container_width=True, type="primary"):
                persist()
                st.success("Settings saved.")
                st.rerun()


def render_facilitator_team(user: Dict) -> None:
    data = data_store()
    if user["role"] != "founder":
        fac = get_fac(user["fac_id"])
        show_header("My Profile", "Your facilitator route stays focused on your access, your status, and your role context.")
        if fac:
            st.markdown("<div class='queue-card'><h4>Profile</h4></div>", unsafe_allow_html=True)
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
    with st.expander("Add facilitator manually", expanded=False):
        with st.form("add_facilitator"):
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
                data["facs"].append({"id": f"f{uuid4().hex[:5]}", "name": name, "uid": uid.strip(), "password": password or f"nook-{uuid4().hex[:6]}", "email": email, "phone": phone, "status": status, "access": access, "refs": int(refs), "sessions": 2, "notes": notes})
                persist()
                st.rerun()
    st.markdown("<div class='section-title'>Team profiles</div>", unsafe_allow_html=True)
    for fac in data["facs"]:
        with st.expander(f"{fac['name']} · {fac['status'].title()}"):
            with st.form(f"fac_edit_{fac['id']}"):
                cols = st.columns(3)
                status = cols[0].selectbox("Status", ["candidate", "active", "offboarded"], index=["candidate", "active", "offboarded"].index(fac["status"]))
                access = cols[1].selectbox("Tier access", ["fo", "ibp", "wi", "yhttb"], index=["fo", "ibp", "wi", "yhttb"].index(fac["access"]), format_func=tier_label)
                refs = cols[2].number_input("Referral slots", min_value=0, value=int(fac["refs"]))
                st.write(f"Login ID: `{fac['uid']}`")
                st.write(f"Email: {fac['email']}")
                st.write(f"Phone: {fac['phone']}")
                reset_password = st.text_input("Reset password", type="password", value="")
                notes = st.text_area("Notes", value=fac["notes"])
                if st.form_submit_button("Save facilitator", use_container_width=True, type="primary"):
                    fac["status"] = status
                    fac["access"] = access
                    fac["refs"] = int(refs)
                    fac["notes"] = notes
                    if reset_password.strip():
                        fac["password"] = reset_password
                    persist()
                    st.rerun()


def render_leave() -> None:
    data = data_store()
    show_header("Leave", "See who is available for sessions right now and capture leave history in one place.")
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
                data["leaves"].append({"id": uuid4().hex[:8], "fid": fac_names[fac_name], "from": from_dt.isoformat(), "to": to_dt.isoformat(), "reason": reason, "notes": notes})
                persist()
                st.rerun()
    for leave in data["leaves"]:
        fac = get_fac(leave["fid"])
        st.markdown(
            f"<div class='queue-card'><h4>{fac['name'] if fac else 'Unknown'}</h4><div class='subtle'>{leave['from']} to {leave['to']} · {leave['reason']}</div><p>{leave['notes']}</p></div>",
            unsafe_allow_html=True,
        )


def render_my_sessions(user: Dict) -> None:
    show_header("My Sessions", "Assigned session details for the facilitator route, including the three-act flow and notes.")
    my_sessions = [e for e in data_store()["exps"] if e["fac"] == user["fac_id"]]
    if not my_sessions:
        st.info("No sessions assigned to you yet.")
        return
    for exp in my_sessions:
        st.markdown(
            f"<div class='session-card'>{tier_badge(exp['tier'])}<strong>{exp['name']}</strong><br><span class='subtle'>{exp['date']} · {exp['time']} · {exp['venue']} · Rs {exp['price']}/person</span><br><div class='subtle'><strong>Act 1:</strong> {exp['act1']}</div><div class='subtle'><strong>Act 2:</strong> {exp['act2']}</div><div class='subtle'><strong>Act 3:</strong> {exp['act3']}</div><div class='subtle'><strong>Transport:</strong> {exp['transport'] or 'Not specified'}</div></div>",
            unsafe_allow_html=True,
        )


def render_messages(user: Dict) -> None:
    data = data_store()
    show_header("Messages", "Founder and facilitator conversations stay inside the system.")
    for msg in data["msgs"]:
        if msg["to"] == user["id"]:
            msg["read"] = True
    persist()
    accounts = [{"id": account["id"], "name": account["name"]} for account in all_accounts()]
    recipient_options = {account["name"]: account["id"] for account in accounts if account["id"] != user["id"]}
    with st.expander("Send a new message", expanded=False):
        with st.form("new_message"):
            recipient = st.selectbox("To", list(recipient_options.keys()))
            subject = st.selectbox("Message type", ["General update", "Session reminder", "Request information from member", "Post-session update"])
            body = st.text_area("Message")
            if st.form_submit_button("Send message", use_container_width=True, type="primary"):
                if body.strip():
                    data["msgs"].append({"id": uuid4().hex[:8], "from": user["id"], "to": recipient_options[recipient], "subject": subject, "body": body.strip(), "ts": datetime.now().strftime("%Y-%m-%d %H:%M"), "read": False})
                    persist()
                    st.rerun()
                st.error("Write a message first.")
    for msg in sorted([m for m in data["msgs"] if m["to"] == user["id"] or m["from"] == user["id"]], key=lambda item: item["ts"], reverse=True):
        st.markdown(
            f"<div class='queue-card'>{pill_html(msg['subject'], 'klein' if msg['from'] == user['id'] else 'aqua')}<h4>{resolve_user_name(msg['from'])}</h4><div class='subtle'>To {resolve_user_name(msg['to'])} · {msg['ts']}</div><p>{msg['body']}</p></div>",
            unsafe_allow_html=True,
        )


def render_docs() -> None:
    show_header("Docs", "Founder-facing notes about access, demo data, and optional integrations.")
    st.markdown(editorial_card("Control room design", "This app is intentionally internal. It has a private home workspace, founder-only application decisions, facilitator referrals, seeded demo data, payment operations, and dynamic facilitator access.", "Overview"), unsafe_allow_html=True)
    st.write("- Data is stored locally in `nook_data.json`.")
    st.write("- Login page does not show passwords.")
    st.write("- Founder can reset facilitator passwords privately inside the team management area.")
    st.write("- Facilitators can submit up to 3 referrals per month, but founder still approves or rejects the application.")


def login_screen() -> None:
    inject_css()
    left, right = st.columns([1.08, 0.92], gap="large")
    with left:
        st.markdown(
            """
            <div class="hero-shell">
              <div class="hero-panel">
                <div class="hero-kicker">Nook control room</div>
                <div class="hero-title">Clean<br>bold<br>control</div>
                <p class="hero-copy">
                  Founder approvals, facilitator workflows, private notes, referrals,
                  planner tools, and payments in one internal app with a sharper editorial layout.
                </p>
                <div class="hero-list">
                  <div class="hero-item"><strong>01</strong><span>Founder route for approvals, referrals, payments, and team oversight.</span></div>
                  <div class="hero-item"><strong>02</strong><span>Facilitator route for sessions, referrals, messages, and private notes.</span></div>
                  <div class="hero-item"><strong>03</strong><span>Smarter backend cues without turning the whole screen into a dashboard wall.</span></div>
                </div>
              </div>
              <div class="hero-panel hero-panel--dark">
                <div class="eyebrow">Why it works</div>
                <div class="section-title">Private access, product energy.</div>
                <p class="hero-copy">
                  Passwords stay hidden on the login screen. Founder and facilitator routes stay separate,
                  while the app keeps the same core logic underneath.
                </p>
                <div class="hero-thumb-grid">
                  <div class="hero-thumb hero-thumb--accent"></div>
                  <div class="hero-thumb"></div>
                  <div class="hero-thumb"></div>
                  <div class="hero-thumb hero-thumb--dark"></div>
                </div>
              </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        render_stat_strip(
            [
                {"value": "2", "label": "Routes", "note": "Founder and facilitator", "accent": FRAME_RED},
                {"value": "40+", "label": "Demo leads", "note": "Seeded for walkthroughs", "accent": TANGERINE},
                {"value": "3", "label": "Monthly referrals", "note": "Per facilitator", "accent": CITRIC},
            ]
        )
    with right:
        st.markdown(editorial_card("Sign in", "Use your assigned credentials or jump into demo mode to preview the founder or facilitator route.", "Private access"), unsafe_allow_html=True)
        with st.form("login_form"):
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            submitted = st.form_submit_button("Enter control room", use_container_width=True, type="primary")
        if submitted:
            user = authenticate(username.strip(), password)
            if user:
                st.session_state.current_user = user
                st.rerun()
            st.error("Wrong credentials. Contact Manju.")
        st.caption("Usernames are visible to the founder. Passwords stay hidden from this page.")
        demo_left, demo_right = st.columns(2)
        if demo_left.button("Demo founder", use_container_width=True, type="secondary"):
            st.session_state.current_user = deepcopy(FOUNDER_ACCOUNT)
            st.rerun()
        facilitator_demo = next((account for account in all_accounts() if account["role"] == "facilitator"), None)
        if demo_right.button("Demo facilitator", use_container_width=True, type="secondary") and facilitator_demo:
            st.session_state.current_user = facilitator_demo
            st.rerun()
        st.markdown(editorial_card("Visible usernames", "Founder username: manju. Facilitator usernames are assigned by founder, for example riya.fac and sneha.fac.", "Hint"), unsafe_allow_html=True)


def navigation_options(user: Dict) -> List[str]:
    if user["role"] == "founder":
        return ["Home", "Dashboard", "Applications", "Referrals", "Planner", "Payments", "Facilitator Team", "Messages", "Leave", "Docs"]
    return ["Home", "Dashboard", "My Sessions", "Referrals", "My Profile", "Messages", "Leave"]


def navigation_rows(options: List[str], row_size: int) -> List[List[str]]:
    return [options[index:index + row_size] for index in range(0, len(options), row_size)]


def sidebar_navigation(user: Dict) -> str:
    options = navigation_options(user)
    if st.session_state.get("page") not in options:
        st.session_state.page = "Home"
    with st.sidebar:
        st.markdown(
            f"<div class='sidebar-card'><div class='eyebrow'>Nook</div><h3>{user['name']}</h3><div class='subtle'>{user['role'].title()} route</div><div class='sidebar-accent'></div></div>",
            unsafe_allow_html=True,
        )
        if st.button("Log out", use_container_width=True, type="secondary"):
            st.session_state.pop("current_user", None)
            st.rerun()
    route_copy = "Founder can move across approvals, referrals, planning, payments, and team operations." if user["role"] == "founder" else "Facilitator tools stay focused on sessions, referrals, profile, and internal updates."
    st.markdown(
        f"<div class='shell-topbar'><div class='brand-panel'><div><div class='eyebrow'>Nook control room</div><div class='brand-title'>{user['name']}</div><div class='brand-copy'>{route_copy}</div></div></div><div class='route-panel'><div><div class='route-title'>Current page</div><div class='brand-title' style='font-size:30px;max-width:none'>{st.session_state.page}</div></div><div class='route-copy'>Header links switch pages. The sidebar stays minimal so the canvas feels cleaner and more like a product showcase.</div></div></div>",
        unsafe_allow_html=True,
    )
    row_size = 5 if user["role"] == "founder" else 4
    for row_index, row in enumerate(navigation_rows(options, row_size)):
        cols = st.columns(len(row))
        for col, page in zip(cols, row):
            is_active = st.session_state.page == page
            if col.button(page, key=f"top_nav_{row_index}_{page}", use_container_width=True, type="primary" if is_active else "secondary"):
                st.session_state.page = page
                st.rerun()
    return st.session_state.page


def render_facilitator_team(user: Dict) -> None:
    data = data_store()
    if user["role"] != "founder":
        fac = get_fac(user["fac_id"])
        show_header("My Profile", "Your facilitator route stays focused on your access, your status, and your role context.")
        if fac:
            access_pill = pill_html(f"{tier_label(fac['access'])} access", "klein")
            refs_pill = pill_html(f"{fac['refs']} referral slots", "citric")
            profile_html = (
                "<div class='queue-card'>"
                f"{status_badge(fac['status'])}"
                f"{access_pill}"
                f"{refs_pill}"
                f"<h4>{fac['name']}</h4>"
                f"<div class='subtle'>{fac['email']} · {fac['phone']}</div>"
                f"<p>{fac['notes']}</p>"
                "</div>"
            )
            st.markdown(profile_html, unsafe_allow_html=True)
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
    with st.expander("Add facilitator manually", expanded=False):
        with st.form("add_facilitator_override"):
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
                st.rerun()

    st.markdown("<div class='section-title'>Team profiles</div>", unsafe_allow_html=True)
    for fac in data["facs"]:
        with st.expander(f"{fac['name']} · {fac['status'].title()}"):
            with st.form(f"fac_edit_override_{fac['id']}"):
                cols = st.columns(3)
                status = cols[0].selectbox("Status", ["candidate", "active", "offboarded"], index=["candidate", "active", "offboarded"].index(fac["status"]))
                access = cols[1].selectbox("Tier access", ["fo", "ibp", "wi", "yhttb"], index=["fo", "ibp", "wi", "yhttb"].index(fac["access"]), format_func=tier_label)
                refs = cols[2].number_input("Referral slots", min_value=0, value=int(fac["refs"]))
                st.write(f"Login ID: `{fac['uid']}`")
                st.write(f"Email: {fac['email']}")
                st.write(f"Phone: {fac['phone']}")
                reset_password = st.text_input("Reset password", type="password", value="")
                notes = st.text_area("Notes", value=fac["notes"])
                if st.form_submit_button("Save facilitator", use_container_width=True, type="primary"):
                    fac["status"] = status
                    fac["access"] = access
                    fac["refs"] = int(refs)
                    fac["notes"] = notes
                    if reset_password.strip():
                        fac["password"] = reset_password
                    persist()
                    st.rerun()


def main() -> None:
    st.set_page_config(page_title="Nook Control Room", page_icon="N", layout="wide", initial_sidebar_state="collapsed")
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

