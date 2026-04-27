import streamlit as st
import plotly.express as px
import pandas as pd
import time

st.set_page_config(page_title='Nook Control Room V2', layout='wide', initial_sidebar_state='expanded')

st.markdown('''
<style>
section[data-testid="stSidebar"]{background:#050505;border-right:1px solid rgba(255,255,255,.06);} 
section[data-testid="stSidebar"] *{color:#fff;} 
button[kind="primary"]{background:#F04E23!important;border:none!important;border-radius:999px!important;} 
@import url("https://fonts.googleapis.com/css2?family=Anton&family=Inter:wght@400;700;900&display=swap");
html, body, [class*="css"] {background:#0A0A0A;color:#F5F5F5;font-family:Inter,sans-serif;}
.block-container{padding-top:1rem;padding-bottom:1rem;max-width:1400px;}
.metric{border-top:6px solid #F04E23;padding:1rem;background:#111;margin-bottom:1rem;}
.big{font-family:Anton,sans-serif;font-size:5rem;line-height:0.9;letter-spacing:1px;}
.hero{font-family:Anton,sans-serif;font-size:8rem;line-height:0.85;margin:0;}
.micro{font-size:.75rem;letter-spacing:.25em;color:#aaa;text-transform:uppercase;}
.panel{background:#f3f3f3;color:#000;padding:1.2rem;min-height:280px;}
.panel-dark{background:#111;color:#fff;padding:1.2rem;min-height:280px;border-left:6px solid #F04E23;}
.smallhead{font-family:Anton,sans-serif;font-size:2.5rem;line-height:1;}
.nav{position:fixed;top:0;left:0;width:100%;height:8px;background:#F04E23;z-index:999;}
</style>
<div class='nav'></div>
''', unsafe_allow_html=True)

page = st.sidebar.radio('navigation',['dashboard','people','incoming','events','insights','payments','settings'])
st.sidebar.markdown('### nook')
st.sidebar.caption('founder mode')

st.markdown("<p class='micro'>bhopal / live / membership engine / social architecture</p>", unsafe_allow_html=True)
if page=='dashboard':
st.markdown("<h1 class='hero'>CONTROL ROOM</h1>", unsafe_allow_html=True)

c1,c2,c3=st.columns(3)
for col,val,label in [(c1,'128','members inside'),(c2,'₹42K','this month'),(c3,'03','nights this week')]:
    with col:
        st.markdown(f"<div class='metric'><div class='big'>{val}</div><div class='micro'>{label}</div></div>", unsafe_allow_html=True)

l,r=st.columns([1.2,1])
with l:
    st.markdown("<div class='panel'><div class='smallhead'>INCOMING ENERGY</div><br><b>17 pending applications</b><br><br>Most common intent: looking for real people, not random plans.<br><br><span class='micro'>approve / waitlist / observe</span></div>", unsafe_allow_html=True)
with r:
    st.markdown("<div class='panel-dark'><div class='smallhead'>NEXT EVENT</div><br><b>CANVAS NIGHT</b><br>Saturday · 8 seats · 87% matched<br><br>Hidden facilitator assigned.<br><br><span class='micro'>mp nagar / chai after</span></div>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

c1,c2=st.columns(2)
with c1:
    st.markdown("<div class='panel-dark'><div class='smallhead'>SPACE HOLDERS</div><br>Riya · Holding<br>Tanya · Available<br>Dev · Session prep</div>", unsafe_allow_html=True)
with c2:
    st.markdown("<div class='panel'><div class='smallhead'>ROOM SIGNAL</div><br>creative leaning<br>low social fatigue<br>ready to gather</div>", unsafe_allow_html=True)


if page=='people':
    st.markdown("<h1 class='hero'>PEOPLE</h1>", unsafe_allow_html=True)
    c1,c2=st.columns(2)
    with c1: st.markdown("<div class='panel'><div class='smallhead'>KABIR</div>quiet energy<br>first out<br>2 sessions</div>", unsafe_allow_html=True)
    with c2: st.markdown("<div class='panel-dark'><div class='smallhead'>ISHITA</div>expressive<br>ibp<br>5 sessions</div>", unsafe_allow_html=True)

if page=='incoming':
    st.markdown("<h1 class='hero'>INCOMING</h1>", unsafe_allow_html=True)
    st.markdown("<div class='panel-dark'><div class='smallhead'>17 PENDING</div>Most applicants seek meaningful social plans.</div>", unsafe_allow_html=True)

if page=='events':
    st.markdown("<h1 class='hero'>EVENTS</h1>", unsafe_allow_html=True)
    st.markdown("<div class='panel'><div class='smallhead'>CANVAS NIGHT</div>sat · 8 seats · sold 6</div>", unsafe_allow_html=True)
    st.markdown("<div class='panel-dark'><div class='smallhead'>ROOFTOP CHAI</div>thu · 10 seats · live</div>", unsafe_allow_html=True)

if page=='insights':
    st.markdown("<h1 class='hero'>INSIGHTS</h1>", unsafe_allow_html=True)
    df=pd.DataFrame({'month':['jan','feb','mar','apr'],'revenue':[12000,18000,26000,42000]})
    fig=px.line(df,x='month',y='revenue',markers=True)
    fig.update_layout(paper_bgcolor='#0A0A0A',plot_bgcolor='#0A0A0A',font_color='white')
    st.plotly_chart(fig,use_container_width=True)

if page=='payments':
    st.markdown("<h1 class='hero'>PAYMENTS</h1>", unsafe_allow_html=True)
    st.markdown("<div class='panel'><div class='smallhead'>₹42K COLLECTED</div>12 successful payments this month.</div>", unsafe_allow_html=True)

if page=='settings':
    st.markdown("<h1 class='hero'>SETTINGS</h1>", unsafe_allow_html=True)
    st.text_input('sheet url')
    st.button('sync now')

st.markdown("---")
st.markdown("<p class='micro' style='text-align:center'>built quietly · bhopal</p>", unsafe_allow_html=True)
