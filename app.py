# app.py
import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Design Class Landing",
    page_icon="🎨",
    layout="wide",
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;900&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: #6e6e6e;
}

.main-box {
    background: #2f2f2f;
    border-radius: 28px;
    padding: 28px 45px;
    margin-top: 20px;
    color: white;
}

.topnav {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid rgba(255,255,255,0.2);
    padding-bottom: 18px;
    margin-bottom: 35px;
}

.nav-left, .nav-right {
    display: flex;
    gap: 28px;
    align-items: center;
}

.logo {
    font-size: 28px;
    font-weight: 900;
}

.nav-item {
    color: #ddd;
    font-size: 14px;
}

.btn-outline {
    border: 1px solid white;
    padding: 8px 18px;
    border-radius: 50px;
    font-size: 13px;
}

.hero {
    text-align: center;
    margin-top: 25px;
}

.hero h1 {
    font-size: 74px;
    line-height: 0.92;
    font-weight: 900;
    margin-bottom: 20px;
}

.orange {
    color: #ff5a00;
}

.sub-small {
    text-align: left;
    font-size: 14px;
    color: #ddd;
    line-height: 1.5;
    margin-top: 20px;
}

.join-btn {
    display: inline-block;
    border: 1px solid white;
    border-radius: 50px;
    padding: 10px 22px;
    margin-top: 20px;
}

.image-card {
    background: #f2f2f2;
    border-radius: 28px;
    padding: 10px;
    text-align: center;
    height: 250px;
}

.image-card img {
    width: 100%;
    border-radius: 20px;
    object-fit: cover;
    height: 230px;
}

.class-box {
    border: 1px solid rgba(255,255,255,0.35);
    border-radius: 28px;
    padding: 35px;
    margin-top: 60px;
}

.section-title {
    font-size: 34px;
    font-weight: 700;
}

.class-card {
    border-radius: 24px;
    padding: 22px;
    height: 290px;
}

.white-card {
    background: #ececec;
    color: black;
}

.orange-card {
    background: #ff5a00;
    color: white;
}

.class-card h3 {
    font-size: 28px;
    margin-bottom: 10px;
}

.quote {
    text-align: center;
    font-size: 44px;
    font-weight: 900;
    margin-top: 30px;
    line-height: 1.0;
}

.footer {
    display: flex;
    justify-content: space-between;
    margin-top: 30px;
    color: #aaa;
    font-size: 12px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- MAIN CONTAINER ----------------
st.markdown('<div class="main-box">', unsafe_allow_html=True)

# NAVBAR
st.markdown("""
<div class="topnav">
    <div class="nav-left">
        <div class="logo">◈</div>
        <div class="nav-item">Home</div>
        <div class="nav-item">Store</div>
        <div class="nav-item">About Us</div>
    </div>

    <div class="nav-right">
        <div class="nav-item">Class</div>
        <div class="btn-outline">Contact Us ↗</div>
    </div>
</div>
""", unsafe_allow_html=True)

# HERO
st.markdown("""
<div class="hero">
    <h1><span class="orange">#</span>LEVEL UP YOUR<br>DESIGN WITH OUR<br>DESIGN CLASS</h1>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns([1,1])

with col1:
    st.markdown("""
    <div class="sub-small">
    With more than<br>
    2K+ Members<br>
    500+ Tutorials
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style='text-align:right'>
    <div class="join-btn">Join Us ↗</div>
    </div>
    """, unsafe_allow_html=True)

# IMAGE SECTION
st.markdown("<br>", unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="image-card">
    <img src="https://images.unsplash.com/photo-1516321318423-f06f85e504b3">
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="image-card">
    <img src="https://images.unsplash.com/photo-1497366754035-f200968a6e72">
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="image-card">
    <img src="https://images.unsplash.com/photo-1517245386807-bb43f82c33c4">
    </div>
    """, unsafe_allow_html=True)

# CLASS SECTION
st.markdown("""
<div class="class-box">
<div style="display:flex;justify-content:space-between;align-items:center;">
<div class="section-title">Our Classes</div>
<div style="max-width:420px;color:#ccc;font-size:16px;">
Here is our types of design classes that will accompany you in learning graphic design
</div>
</div>
</div>
""", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="class-card white-card">
        <h3>Beginner<br>Class</h3>
        <p>For those of you who are just learning design.</p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="class-card orange-card">
        <h3>Expert<br>Class</h3>
        <p>For those of you who want to upgrade your skills.</p>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="class-card white-card">
        <h3>Employee<br>Class</h3>
        <p>For those of you who are busy but still want to learn.</p>
    </div>
    """, unsafe_allow_html=True)

# QUOTE
st.markdown("""
<div class="quote">
KEEP <span class="orange">CREATING</span> UNTIL YOU<br>
FIND YOUR OWN <span class="orange">AUDIENCE</span>
</div>
""", unsafe_allow_html=True)

# FOOTER
st.markdown("""
<div class="footer">
<div>Copyright RE Production</div>
<div>Ruang Edit 2024</div>
</div>
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
