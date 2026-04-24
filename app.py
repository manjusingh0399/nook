import streamlit as st

st.set_page_config(layout="wide")

# -------------------- STYLES --------------------
st.markdown("""
<style>

/* BASE */
html, body, [data-testid="stApp"] {
    background: #050505;
    color: #EDEDED;
    font-family: Inter, sans-serif;
}

/* REMOVE DEFAULT */
#MainMenu, header, footer {visibility: hidden;}
.block-container {
    padding: 0;
    max-width: 1200px;
    margin: auto;
}

/* HERO */
.hero {
    padding: 80px 40px 60px;
    background: radial-gradient(circle at 70% 20%, #ff5a00 0%, #050505 60%);
    border-radius: 20px;
    margin: 20px 0;
}

.hero-title {
    font-size: 48px;
    font-weight: 800;
    line-height: 1.1;
}

.hero-sub {
    margin-top: 10px;
    color: #aaa;
}

/* BUTTON */
.cta {
    margin-top: 20px;
    display: inline-block;
    padding: 10px 18px;
    background: #FF5A00;
    border-radius: 20px;
    font-size: 12px;
}

/* METRIC */
.metric-card {
    background: #0E0E0E;
    padding: 20px;
    border-radius: 16px;
    border: 1px solid rgba(255,255,255,0.05);
}

.metric-value {
    font-size: 28px;
    font-weight: 700;
}

.metric-label {
    font-size: 10px;
    color: #777;
}

/* SECTION */
.section-title {
    font-size: 22px;
    font-weight: 700;
    margin-top: 40px;
    margin-bottom: 10px;
}

/* CARD GRID */
.card {
    background: #0E0E0E;
    border-radius: 16px;
    padding: 16px;
    margin-bottom: 12px;
    border: 1px solid rgba(255,255,255,0.05);
}

.card-title {
    font-size: 14px;
    font-weight: 600;
}

.card-sub {
    font-size: 11px;
    color: #777;
}

/* GRADIENT FOOTER */
.footer {
    margin-top: 60px;
    padding: 60px;
    background: linear-gradient(180deg, #050505, #ff5a00);
    border-radius: 20px;
    text-align: center;
}

</style>
""", unsafe_allow_html=True)

# -------------------- HERO --------------------
st.markdown("""
<div class="hero">
    <div class="hero-title">
        your control system<br>
        for meaningful experiences
    </div>
    <div class="hero-sub">
        design, track and evolve social energy — not just events
    </div>
    <div class="cta">start now</div>
</div>
""", unsafe_allow_html=True)

# -------------------- METRICS --------------------
cols = st.columns(4)

metrics = [
    ("40", "people"),
    ("5", "active evenings"),
    ("₹998", "revenue"),
    ("4", "facilitators")
]

for i, (val, label) in enumerate(metrics):
    with cols[i]:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-value">{val}</div>
            <div class="metric-label">{label}</div>
        </div>
        """, unsafe_allow_html=True)

# -------------------- SUBMISSIONS --------------------
st.markdown("<div class='section-title'>recent submissions</div>", unsafe_allow_html=True)

col1, col2 = st.columns([2,1])

with col1:
    st.markdown("""
    <div class="card">
        Vikram Tiwari — ₹600–₹1000<br>
        <span class="card-sub">pending</span>
    </div>

    <div class="card">
        Naina Gupta — Under ₹400<br>
        <span class="card-sub">pending</span>
    </div>

    <div class="card">
        Dev Sharma — ₹400–₹600<br>
        <span class="card-sub">pending</span>
    </div>
    """, unsafe_allow_html=True)

# -------------------- SESSIONS --------------------
with col2:
    st.markdown("<div class='section-title'>upcoming sessions</div>", unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        Canvas Night — MP Nagar<br>
        <span class="card-sub">₹499 · Riya Kapoor</span>
    </div>

    <div class="card">
        After Dark Walk — Upper Lake<br>
        <span class="card-sub">₹299 · Aryan Mehta</span>
    </div>
    """, unsafe_allow_html=True)

# -------------------- INSIGHTS --------------------
st.markdown("<div class='section-title'>insights</div>", unsafe_allow_html=True)

st.markdown("""
<div class="card">
    smaller groups → better emotional depth<br>
    quiet users return more consistently
</div>
""", unsafe_allow_html=True)

# -------------------- FOOTER --------------------
st.markdown("""
<div class="footer">
    built for meaningful connection, not noise
</div>
""", unsafe_allow_html=True)
