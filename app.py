import streamlit as st
import pandas as pd
from datetime import date

st.set_page_config(page_title='NOOK V5', layout='wide', initial_sidebar_state='expanded')

# data
if 'members' not in st.session_state:
    st.session_state.members = pd.DataFrame([
        ['Kabir','Approved','First Out'],['Ishita','Approved','Worth It'],['Dev','Waitlist','IBP'],['Naina','Approved','YHTTB']
    ], columns=['Name','Status','Tier'])
if 'events' not in st.session_state:
    st.session_state.events = pd.DataFrame([
        ['Canvas Night','Sat','MP Nagar'],['Rooftop Chai','Thu','Arera']
    ], columns=['Experience','Day','Location'])

st.markdown('''<style>
@import url("https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap");
html,body,[class*=css]{background:#2f312f;color:#fff;font-family:Inter,sans-serif}
section[data-testid='stSidebar']{background:#262826;border-right:1px solid rgba(255,255,255,.08)}
.block-container{max-width:1400px;padding-top:1rem;padding-bottom:3rem}
.hero,.title{font-weight:800;letter-spacing:-0.04em}.hero{font-size:5rem;line-height:.9}.title{font-size:2rem}
.shell{background:#353734;border-radius:28px;padding:1.2rem}.panel{background:#3a3c39;border:1px solid rgba(255,255,255,.08);border-radius:24px;padding:1.2rem;height:100%}
.orange{color:#ff6a00}.btn{background:#ff6a00;color:#fff;padding:.6rem 1rem;border-radius:999px}.muted{color:#c8c8c8}.metric{font-size:3rem;font-weight:800}.small{font-size:.75rem;letter-spacing:.2em;text-transform:uppercase;color:#d0d0d0}
div[data-testid='stDataFrame']{border-radius:18px;overflow:hidden}
.stButton>button{border-radius:999px;background:#ff6a00;color:#fff;border:none}
</style>''', unsafe_allow_html=True)

mode=st.sidebar.radio('Mode',['Website','Founder Portal'])
st.sidebar.caption('NOOK / PRIVATE SOCIAL CLUB')

if mode=='Website':
    st.markdown("<div class='shell'>", unsafe_allow_html=True)
    st.markdown("<div class='small'>Home · Experiences · About · Apply</div>", unsafe_allow_html=True)
    c1,c2=st.columns([1.6,1])
    with c1:
        st.markdown("<div style='padding:2rem 1rem'><div class='hero'><span class='orange'>LEVEL UP</span> YOUR SOCIAL LIFE WITH NOOK</div><br><div class='muted'>Curated experiences, ambitious people, better weekends.</div></div>", unsafe_allow_html=True)
    with c2:
        st.markdown("<div class='panel'><div class='title'>Join Us</div><p class='muted'>Invite-only community built quietly in Bhopal.</p></div>", unsafe_allow_html=True)
    c1,c2,c3=st.columns(3)
    for col,t in zip([c1,c2,c3],['Dinner Nights','Creative Gatherings','Social Walks']):
        with col: st.markdown(f"<div class='panel'><div class='title'>{t}</div><p class='muted'>Thoughtful people. Better rooms.</p></div>", unsafe_allow_html=True)
    st.markdown('<br>', unsafe_allow_html=True)
    st.markdown("<div class='panel'><div class='title'>Our Membership Tiers</div></div>", unsafe_allow_html=True)
    c1,c2,c3=st.columns(3)
    tiers=['First Out','Worth It','YHTTB']
    for col,t in zip([c1,c2,c3],tiers):
        with col: st.markdown(f"<div class='panel'><div class='title'>{t}</div><p class='muted'>Access level for different social energies.</p></div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
else:
    page=st.sidebar.radio('Navigate',['Dashboard','Members','Waitlist','Events','Insights','Settings'])
    st.markdown("<div class='shell'>", unsafe_allow_html=True)
    if page=='Dashboard':
        st.markdown("<div class='hero'>CONTROL ROOM</div>", unsafe_allow_html=True)
        c1,c2,c3,c4=st.columns(4)
        vals=[('128','Members'),('₹42K','Revenue'),('03','Events'),('87%','Retention')]
        for col,(v,l) in zip([c1,c2,c3,c4],vals):
            with col: st.markdown(f"<div class='panel'><div class='metric'>{v}</div><div class='small'>{l}</div></div>", unsafe_allow_html=True)
    elif page=='Members': st.dataframe(st.session_state.members,use_container_width=True)
    elif page=='Waitlist': st.dataframe(st.session_state.members[st.session_state.members.Status=='Waitlist'],use_container_width=True)
    elif page=='Events':
        st.dataframe(st.session_state.events,use_container_width=True)
        with st.form('ev'):
            a,b,c=st.columns(3)
            x=a.text_input('Experience'); y=b.text_input('Day'); z=c.text_input('Location')
            if st.form_submit_button('Add'): st.session_state.events.loc[len(st.session_state.events)]=[x,y,z]
    elif page=='Insights':
        st.line_chart(pd.DataFrame({'Revenue':[10,18,26,42,51]}))
    elif page=='Settings':
        st.text_input('Admin Email'); st.toggle('Invite Only',True); st.button('Save')
    st.markdown("</div>", unsafe_allow_html=True)
