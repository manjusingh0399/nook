import streamlit as st
import pandas as pd
from datetime import date

st.set_page_config(page_title='Nook Web App V1', layout='wide')

# ---------- STYLE ----------
st.markdown('''
<style>
.stApp {background:#f5f5f5;}
.hero{background:#ff5a00;padding:28px;border-radius:18px;color:white;margin-bottom:18px;}
.card{background:white;padding:18px;border-radius:16px;box-shadow:0 8px 24px rgba(0,0,0,.08);margin-bottom:14px;}
.metric{font-size:34px;font-weight:800;color:#111;}
.small{color:#666;font-size:13px;}
.tag{display:inline-block;padding:4px 10px;border-radius:20px;background:#111;color:#fff;font-size:12px;margin-right:6px;}
button[kind='primary']{background:#ff5a00 !important;border:none !important;}
</style>
''', unsafe_allow_html=True)

# ---------- DATA ----------
if 'users' not in st.session_state:
    st.session_state.users = {
        'founder@nook.com': {'name':'Manju Singh','role':'founder','tier':'YHTBT','password':'admin123','referrals':3},
        'user@nook.com': {'name':'Kabir','role':'member','tier':'First Out','password':'user123','referrals':3},
    }
if 'events' not in st.session_state:
    st.session_state.events = [
        {'name':'Canvas Night','tier':'First Out','date':'2026-05-10','price':499},
        {'name':'Dinner Stories','tier':'In Between Plans','date':'2026-05-14','price':899},
        {'name':'Farmhouse Social','tier':'Worth It','date':'2026-05-22','price':2499},
    ]
if 'applications' not in st.session_state:
    st.session_state.applications = []
if 'bookings' not in st.session_state:
    st.session_state.bookings = []
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# ---------- HELPERS ----------
def logout():
    st.session_state.logged_in=False
    st.rerun()

def login(email,pw):
    u=st.session_state.users.get(email)
    if u and u['password']==pw:
        st.session_state.logged_in=True
        st.session_state.email=email
        st.rerun()

# ---------- LOGIN ----------
if not st.session_state.logged_in:
    st.markdown("<div class='hero'><h1>NOOK</h1><h3>Your Third Place</h3><p>More than just going out.</p></div>", unsafe_allow_html=True)
    c1,c2=st.columns(2)
    with c1:
        st.subheader('Login')
        email=st.text_input('Email', value='founder@nook.com')
        pw=st.text_input('Password', type='password', value='admin123')
        if st.button('Enter Nook'):
            login(email,pw)
    with c2:
        st.subheader('Join Waitlist')
        n=st.text_input('Name')
        e=st.text_input('Your Email')
        vibe=st.selectbox('What are you seeking?', ['New people','Meaningful evenings','Fun plans','Something different'])
        if st.button('Apply to Nook'):
            st.session_state.applications.append({'name':n,'email':e,'vibe':vibe,'status':'Pending'})
            st.success('Applied successfully.')
    st.stop()

# ---------- APP ----------
user=st.session_state.users[st.session_state.email]
st.sidebar.image('https://dummyimage.com/220x60/ff5a00/ffffff&text=NOOK')
st.sidebar.write(user['name'])
st.sidebar.caption(user['role'])
page = st.sidebar.radio('Navigate', ['Dashboard','Experiences','Referrals','Founder Panel'] if user['role']=='founder' else ['Dashboard','Experiences','Referrals'])
if st.sidebar.button('Logout'): logout()

# ---------- DASHBOARD ----------
if page=='Dashboard':
    st.markdown("<div class='hero'><h1>Welcome to Nook</h1><p>Your social life, upgraded.</p></div>", unsafe_allow_html=True)
    c1,c2,c3=st.columns(3)
    with c1:
        st.markdown("<div class='card'><div class='small'>Your Tier</div><div class='metric'>%s</div></div>"%user['tier'], unsafe_allow_html=True)
    with c2:
        st.markdown("<div class='card'><div class='small'>Referrals Left</div><div class='metric'>%s</div></div>"%user['referrals'], unsafe_allow_html=True)
    with c3:
        st.markdown("<div class='card'><div class='small'>Upcoming Events</div><div class='metric'>%s</div></div>"%len(st.session_state.events), unsafe_allow_html=True)

# ---------- EXPERIENCES ----------
if page=='Experiences':
    st.title('Upcoming Experiences')
    for i,e in enumerate(st.session_state.events):
        st.markdown(f"<div class='card'><h3>{e['name']}</h3><span class='tag'>{e['tier']}</span><p>{e['date']} · ₹{e['price']}</p></div>", unsafe_allow_html=True)
        if st.button(f"Book {e['name']}", key=i):
            st.session_state.bookings.append({'user':user['name'],'event':e['name']})
            st.success('Booked!')

# ---------- REFERRALS ----------
if page=='Referrals':
    st.title('Invite Friends')
    st.markdown(f"<div class='card'><h3>Your Code: NOOK{user['name'][:3].upper()}</h3><p>{user['referrals']} invites left</p></div>", unsafe_allow_html=True)
    friend=st.text_input('Friend email')
    if st.button('Send Invite'):
        st.success('Invite sent.')

# ---------- FOUNDER PANEL ----------
if page=='Founder Panel' and user['role']=='founder':
    st.title('Founder Control Room')
    c1,c2,c3=st.columns(3)
    c1.metric('Members', len(st.session_state.users))
    c2.metric('Applications', len(st.session_state.applications))
    c3.metric('Bookings', len(st.session_state.bookings))

    st.subheader('Applications')
    if st.session_state.applications:
        df=pd.DataFrame(st.session_state.applications)
        st.dataframe(df, use_container_width=True)
    else:
        st.info('No applications yet.')

    st.subheader('Create Event')
    n=st.text_input('Event Name')
    tier=st.selectbox('Tier',['First Out','In Between Plans','Worth It','YHTBT'])
    d=st.date_input('Date', value=date.today())
    p=st.number_input('Price', value=499)
    if st.button('Create Experience'):
        st.session_state.events.append({'name':n,'tier':tier,'date':str(d),'price':p})
        st.success('Experience created.')
