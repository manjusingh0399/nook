import streamlit as st
import pandas as pd
from datetime import date

st.set_page_config(page_title='NOOK Ecosystem V1', layout='wide', initial_sidebar_state='expanded')

st.markdown('''<style>
.stApp{background:#0b0b0b;color:white}.block-container{padding-top:1rem}
.hero{background:linear-gradient(135deg,#ff5a00,#ff7a1a);padding:28px;border-radius:20px;color:white;margin-bottom:16px}
.card{background:#151515;border:1px solid #2a2a2a;padding:18px;border-radius:18px;margin-bottom:14px}
.small{color:#999;font-size:12px}.big{font-size:34px;font-weight:800}.pill{padding:4px 10px;border-radius:999px;background:#ff5a00;color:white;font-size:11px}
</style>''', unsafe_allow_html=True)

if 'users' not in st.session_state:
    st.session_state.users={
        'founder@nook.com':{'pw':'admin123','name':'Manju','role':'founder','tier':'YHTBT'},
        'member@nook.com':{'pw':'user123','name':'Kabir','role':'member','tier':'First Out'}
    }
if 'events' not in st.session_state:
    st.session_state.events=[{'name':'Canvas Night','tier':'First Out','date':'2026-05-10','price':499,'spots':8},{'name':'Dinner Stories','tier':'IBP','date':'2026-05-14','price':899,'spots':10}]
if 'apps' not in st.session_state: st.session_state.apps=[]
if 'bookings' not in st.session_state: st.session_state.bookings=[]
if 'logged' not in st.session_state: st.session_state.logged=False

# Public website mode
mode=st.sidebar.selectbox('Mode',['Website','Login Portal'] if not st.session_state.logged else ['App'])

if not st.session_state.logged and mode=='Website':
    st.markdown("<div class='hero'><h1>NOOK</h1><h2>Your Third Place</h2><p>More than plans. Better than staying in.</p></div>",unsafe_allow_html=True)
    tabs=st.tabs(['Home','Experiences','Apply'])
    with tabs[0]:
        st.markdown("<div class='card'><h3>Curated real-world social experiences in Bhopal.</h3></div>",unsafe_allow_html=True)
    with tabs[1]:
        for e in st.session_state.events:
            st.markdown(f"<div class='card'><b>{e['name']}</b><br><span class='small'>{e['tier']} · {e['date']} · ₹{e['price']}</span></div>",unsafe_allow_html=True)
    with tabs[2]:
        n=st.text_input('Name')
        em=st.text_input('Email')
        why=st.text_area('Why Nook?')
        if st.button('Join Waitlist'):
            st.session_state.apps.append({'name':n,'email':em,'why':why,'status':'Pending'})
            st.success('Applied to Nook.')
    st.stop()

if not st.session_state.logged:
    st.markdown("<div class='hero'><h1>Member / Founder Login</h1></div>",unsafe_allow_html=True)
    em=st.text_input('Email')
    pw=st.text_input('Password',type='password')
    if st.button('Enter'):
        u=st.session_state.users.get(em)
        if u and u['pw']==pw:
            st.session_state.logged=True; st.session_state.email=em; st.rerun()
        else: st.error('Invalid login')
    st.stop()

user=st.session_state.users[st.session_state.email]
st.sidebar.write(user['name'])
st.sidebar.caption(user['role'])
if st.sidebar.button('Logout'):
    st.session_state.logged=False; st.rerun()

if user['role']=='member':
    page=st.sidebar.radio('Navigate',['Dashboard','Events','Community','Referrals','Profile'])
    if page=='Dashboard':
        st.markdown("<div class='hero'><h1>Welcome Back</h1></div>",unsafe_allow_html=True)
        c1,c2=st.columns(2)
        c1.markdown(f"<div class='card'><div class='small'>Tier</div><div class='big'>{user['tier']}</div></div>",unsafe_allow_html=True)
        c2.markdown(f"<div class='card'><div class='small'>Bookings</div><div class='big'>{len(st.session_state.bookings)}</div></div>",unsafe_allow_html=True)
    elif page=='Events':
        for i,e in enumerate(st.session_state.events):
            st.markdown(f"<div class='card'><b>{e['name']}</b><br>{e['date']} · ₹{e['price']}</div>",unsafe_allow_html=True)
            if st.button(f"Book {e['name']}",key=i):
                st.session_state.bookings.append({'user':user['name'],'event':e['name']})
                st.success('Booked')
    elif page=='Community':
        st.markdown("<div class='card'>Members-only vibe feed coming soon.</div>",unsafe_allow_html=True)
    elif page=='Referrals':
        st.markdown("<div class='card'><h3>Your Code: NOOKKAB</h3><p>3 invites left</p></div>",unsafe_allow_html=True)
    elif page=='Profile':
        st.json(user)
else:
    page=st.sidebar.radio('Control Room',['Dashboard','Applicants','Events','Members','Revenue'])
    if page=='Dashboard':
        st.markdown("<div class='hero'><h1>NOOK CONTROL ROOM</h1></div>",unsafe_allow_html=True)
        c1,c2,c3=st.columns(3)
        c1.metric('Applicants',len(st.session_state.apps))
        c2.metric('Events',len(st.session_state.events))
        c3.metric('Bookings',len(st.session_state.bookings))
    elif page=='Applicants':
        st.dataframe(pd.DataFrame(st.session_state.apps),use_container_width=True)
    elif page=='Events':
        n=st.text_input('Event Name')
        t=st.selectbox('Tier',['First Out','IBP','Worth It','YHTBT'])
        d=st.date_input('Date',date.today())
        p=st.number_input('Price',value=499)
        if st.button('Create Event'):
            st.session_state.events.append({'name':n,'tier':t,'date':str(d),'price':p,'spots':8})
            st.success('Created')
        st.write(st.session_state.events)
    elif page=='Members':
        st.dataframe(pd.DataFrame([{'email':k,**v} for k,v in st.session_state.users.items()]),use_container_width=True)
    elif page=='Revenue':
        rev=sum([e['price'] for e in st.session_state.events])
        st.metric('Potential Revenue',f'₹{rev}')
