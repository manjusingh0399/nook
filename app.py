import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title='Nook Control Room V2', layout='wide', initial_sidebar_state='expanded')

# ---------- DATA ----------
if 'members' not in st.session_state:
    st.session_state.members = pd.DataFrame([
        ['Kabir','Pending','First Out',2],['Ishita','Approved','IBP',5],['Dev','Waitlist','First Out',0],['Naina','Approved','Worth It',6]
    ], columns=['Name','Status','Tier','Sessions'])

# ---------- UI ----------
st.markdown('''
<style>
@import url("https://fonts.googleapis.com/css2?family=Anton&family=Inter:wght@400;700;900&display=swap");
html,body,[class*='css']{background:#050505;color:#fff;font-family:Inter,sans-serif}
section[data-testid='stSidebar']{background:#0b0b0b;border-right:1px solid rgba(255,255,255,.08)}
.block-container{padding-top:1rem;max-width:1450px}
.hero{font-family:Anton,sans-serif;font-size:5rem;line-height:.9;margin:0}
.micro{font-size:.72rem;letter-spacing:.22em;color:#9a9a9a;text-transform:uppercase}
.card{background:linear-gradient(135deg,#111,#0a0a0a);border:1px solid rgba(255,255,255,.08);border-radius:22px;padding:1.2rem;margin-bottom:1rem}
.metric{font-family:Anton,sans-serif;font-size:3rem;color:#F04E23;line-height:1}
.orange{color:#F04E23}
button[kind='primary']{background:#F04E23!important;border:none!important;border-radius:999px!important}
</style>
''', unsafe_allow_html=True)

# ---------- SIDEBAR ----------
page = st.sidebar.radio('Navigation', ['Dashboard','People','Incoming','Events','Insights','Payments','Settings'])
st.sidebar.caption('Founder Mode')

# ---------- DASHBOARD ----------
if page == 'Dashboard':
    st.markdown("<div class='micro'>bhopal / live / control room</div>", unsafe_allow_html=True)
    st.markdown("<h1 class='hero'>CONTROL ROOM</h1>", unsafe_allow_html=True)
    c1,c2,c3=st.columns(3)
    for c,v,l in [(c1,'128','members inside'),(c2,'₹42K','monthly revenue'),(c3,'03','events this week')]:
        with c:
            st.markdown(f"<div class='card'><div class='metric'>{v}</div><div class='micro'>{l}</div></div>", unsafe_allow_html=True)
    st.markdown("<div class='card'><b class='orange'>Room Signal</b><br>creative leaning · ready to gather · low fatigue</div>", unsafe_allow_html=True)

elif page == 'People':
    st.markdown("<h1 class='hero'>PEOPLE</h1>", unsafe_allow_html=True)
    st.dataframe(st.session_state.members, use_container_width=True)

elif page == 'Incoming':
    st.markdown("<h1 class='hero'>INCOMING</h1>", unsafe_allow_html=True)
    df = st.session_state.members[st.session_state.members['Status'].isin(['Pending','Waitlist'])]
    st.dataframe(df, use_container_width=True)

elif page == 'Events':
    st.markdown("<h1 class='hero'>EVENTS</h1>", unsafe_allow_html=True)
    st.markdown("<div class='card'><div class='metric'>CANVAS NIGHT</div>Sat · 8 Seats · Hidden facilitator assigned</div>", unsafe_allow_html=True)
    st.markdown("<div class='card'><div class='metric'>ROOFTOP CHAI</div>Thu · 10 Seats · Live now</div>", unsafe_allow_html=True)

elif page == 'Insights':
    st.markdown("<h1 class='hero'>INSIGHTS</h1>", unsafe_allow_html=True)
    df=pd.DataFrame({'Month':['Jan','Feb','Mar','Apr'],'Revenue':[12000,18000,26000,42000]})
    fig=px.area(df,x='Month',y='Revenue')
    fig.update_layout(paper_bgcolor='#050505',plot_bgcolor='#050505',font_color='white')
    st.plotly_chart(fig,use_container_width=True)

elif page == 'Payments':
    st.markdown("<h1 class='hero'>PAYMENTS</h1>", unsafe_allow_html=True)
    st.markdown("<div class='card'><div class='metric'>₹42,000</div>Collected this month</div>", unsafe_allow_html=True)

elif page == 'Settings':
    st.markdown("<h1 class='hero'>SETTINGS</h1>", unsafe_allow_html=True)
    st.text_input('Google Sheet URL')
    st.button('Sync Now', type='primary')

st.markdown("<div class='micro' style='text-align:center;padding:2rem 0'>built quietly · bhopal</div>", unsafe_allow_html=True)
