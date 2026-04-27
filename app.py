import streamlit as st
import pandas as pd
from datetime import date

st.set_page_config(page_title='NOOK Control Room', layout='wide', initial_sidebar_state='expanded')

# ---------- STATE ----------
if 'members' not in st.session_state:
    st.session_state.members = pd.DataFrame([
        ['Kabir Anand','Pending','First Out',2,'Weekend evenings'],
        ['Ishita Rao','Approved','Worth It',5,'Saturday'],
        ['Dev Sharma','Waitlist','IBP',0,'Flexible'],
        ['Naina Gupta','Approved','YHTTB',6,'Sunday']
    ], columns=['Name','Status','Tier','Sessions','Availability'])

if 'events' not in st.session_state:
    st.session_state.events = pd.DataFrame([
        ['Canvas Night','2026-04-30','MP Nagar',8,499,'Live'],
        ['Rooftop Chai','2026-05-03','Arera',10,299,'Planned']
    ], columns=['Event','Date','Venue','Seats','Price','Status'])

# ---------- STYLES ----------
st.markdown('''
<style>
@import url("https://fonts.googleapis.com/css2?family=Anton&family=Inter:wght@400;600;800&display=swap");
html,body,[class*='css']{background:#020202;color:#f5f2ea;font-family:Inter,sans-serif}
section[data-testid='stSidebar']{background:#050505;border-right:2px solid #2a0000}
.block-container{max-width:1500px;padding-top:1rem}
h1,h2,h3{font-family:Anton,sans-serif;letter-spacing:.03em}
.hero{font-size:5.5rem;line-height:.9;margin:0;color:#f5f2ea}
.micro{font-size:.72rem;letter-spacing:.28em;text-transform:uppercase;color:#8d8d8d}
.card{background:linear-gradient(135deg,#5a0000,#a30000);border:1px solid rgba(255,255,255,.08);padding:1.25rem;border-radius:0;margin-bottom:1rem;box-shadow:0 0 40px rgba(180,0,0,.18)}
.metric{font-family:Anton,sans-serif;font-size:3.2rem;line-height:1;color:#fff}
.soft{color:#9d9d9d}
.orange{color:#ffb3a7}
div[data-testid='stDataFrame']{border:2px solid #222}
button[kind='primary']{background:#b30000!important;border:none!important;border-radius:0!important;color:#fff!important}
.stButton>button{border-radius:0!important;border:2px solid #222!important}
</style>
''', unsafe_allow_html=True)

# ---------- SIDEBAR ----------
st.sidebar.markdown("# NOOK")
st.sidebar.caption("CONTROL ROOM / FOUNDER")
page = st.sidebar.radio('Navigate', ['Dashboard','Waitlist','Members','Facilitators','Events','Insights','Payments','Settings'])

# ---------- DASHBOARD ----------
if page == 'Dashboard':
    st.markdown("<div class='micro'>bhopal / invite only / social architecture</div>", unsafe_allow_html=True)
    st.markdown("<div class='hero'>CONTROL ROOM</div><div class='card'><h3>FROM ROUTINE HANGOUTS TO REAL CONNECTIONS — WE'RE WITH YOU EVERY STEP</h3><p class='soft'>Private social experiences designed for people who want more than random plans.</p></div>", unsafe_allow_html=True)
    c1,c2,c3,c4 = st.columns(4)
    stats = [('128','Members'),('₹42K','Revenue'),('03','Live Events'),('87%','Retention')]
    for col,(v,l) in zip([c1,c2,c3,c4],stats):
        with col:
            st.markdown(f"<div class='card'><div class='metric'>{v}</div><div class='micro'>{l}</div></div>", unsafe_allow_html=True)
    a,b = st.columns([1.4,1])
    with a:
        st.markdown("<div class='card'><h3>ROOM SIGNAL</h3><p class='soft'>Creative leaning. Members ready to gather. Low social fatigue. High curiosity.</p></div>", unsafe_allow_html=True)
        st.markdown("<div class='card'><h3>FOUNDER NOTES</h3><p class='soft'>Canvas Night nearly sold out. Approve 2 strong applicants. Push referral wave next week.</p></div>", unsafe_allow_html=True)
    with b:
        st.markdown("<div class='card'><h3>NEXT EXPERIENCE</h3><div class='metric'>CANVAS NIGHT</div><p>Sat / MP Nagar / 8 Seats</p></div>", unsafe_allow_html=True)

# ---------- WAITLIST ----------
elif page == 'Waitlist':
    st.markdown("# WAITLIST")
    df = st.session_state.members[st.session_state.members['Status'].isin(['Pending','Waitlist'])]
    st.dataframe(df, use_container_width=True)
    st.markdown('### Review Applicant')
    names = df['Name'].tolist() if not df.empty else []
    if names:
        pick = st.selectbox('Select applicant', names)
        c1,c2,c3 = st.columns(3)
        if c1.button('Approve'):
            st.session_state.members.loc[st.session_state.members['Name']==pick,'Status']='Approved'
        if c2.button('Waitlist'):
            st.session_state.members.loc[st.session_state.members['Name']==pick,'Status']='Waitlist'
        if c3.button('Decline'):
            st.session_state.members.loc[st.session_state.members['Name']==pick,'Status']='Declined'
        st.success('Status updated')

# ---------- MEMBERS ----------
elif page == 'Members':
    st.markdown("# MEMBERS")
    search = st.text_input('Search member')
    df = st.session_state.members.copy()
    if search:
        df = df[df['Name'].str.contains(search, case=False)]
    st.dataframe(df, use_container_width=True)
    st.markdown('### Add Member')
    with st.form('add_member'):
        n1,n2,n3 = st.columns(3)
        name = n1.text_input('Name')
        tier = n2.selectbox('Tier',['First Out','IBP','Worth It','YHTTB'])
        avail = n3.text_input('Availability')
        if st.form_submit_button('Add Member'):
            st.session_state.members.loc[len(st.session_state.members)] = [name,'Approved',tier,0,avail]
            st.success('Member added')

# ---------- FACILITATORS ----------
elif page == 'Facilitators':
    st.markdown('# FACILITATORS')
    fac = pd.DataFrame([
        ['Riya Kapoor','Active','Worth It',4],
        ['Aryan Mehta','Candidate','IBP',2],
        ['Sneha Joshi','Active','YHTTB',6]
    ], columns=['Name','Status','Access','Sessions'])
    st.dataframe(fac, use_container_width=True)
    st.markdown("<div class='card'><h3>TEAM NOTE</h3><p class='soft'>Sneha should host next intimate dinner. Aryan needs one more shadow session.</p></div>", unsafe_allow_html=True)

# ---------- EVENTS ----------
elif page == 'Events':
    st.markdown('# EVENTS')
    st.dataframe(st.session_state.events, use_container_width=True)
    st.markdown('### Build Experience')
    with st.form('event_form'):
        c1,c2,c3 = st.columns(3)
        ename = c1.text_input('Event Name')
        edate = c2.date_input('Date', value=date.today())
        venue = c3.text_input('Venue')
        c4,c5,c6 = st.columns(3)
        seats = c4.number_input('Seats',4,30,8)
        price = c5.number_input('Price',100,5000,499)
        status = c6.selectbox('Status',['Planned','Live','Closed'])
        if st.form_submit_button('Create Event'):
            st.session_state.events.loc[len(st.session_state.events)] = [ename,str(edate),venue,seats,price,status]
            st.success('Experience created')

# ---------- INSIGHTS ----------
elif page == 'Insights':
    st.markdown('# INSIGHTS')
    df = pd.DataFrame({'Month':['Jan','Feb','Mar','Apr','May'],'Revenue':[12000,18000,26000,42000,51000]})
    st.line_chart(df.set_index('Month'))
    st.markdown("<div class='card'><h3>INTELLIGENCE</h3><p class='soft'>Retention strongest after small-group curated nights. Premium pricing accepted when storytelling is strong.</p></div>", unsafe_allow_html=True)

# ---------- PAYMENTS ----------
elif page == 'Payments':
    st.markdown('# PAYMENTS')
    c1,c2 = st.columns(2)
    with c1:
        st.markdown("<div class='card'><div class='metric'>₹42,000</div><div class='micro'>This Month</div></div>", unsafe_allow_html=True)
    with c2:
        st.markdown("<div class='card'><div class='metric'>12</div><div class='micro'>Transactions</div></div>", unsafe_allow_html=True)
    pay = pd.DataFrame({'Member':['Kabir','Ishita','Naina'],'Amount':[499,799,299],'Status':['Paid','Paid','Pending']})
    st.dataframe(pay,use_container_width=True)

# ---------- SETTINGS ----------
elif page == 'Settings':
    st.markdown('# SETTINGS')
    st.text_input('Google Sheet URL')
    st.text_input('Supabase URL')
    st.text_input('Admin Email')
    st.toggle('Invite Only Mode', value=True)
    st.toggle('Accept Applications', value=True)
    st.button('Save Configuration', type='primary')
    st.markdown("<div class='card'><h3>SYSTEM MODE</h3><p class='soft'>Luxury brutalist UI active. Founder access only.</p></div>", unsafe_allow_html=True)

st.markdown("<div class='micro' style='text-align:center;padding:2rem 0'>built quietly / nook</div>", unsafe_allow_html=True)
