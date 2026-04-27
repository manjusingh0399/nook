import streamlit as st
import pandas as pd
from datetime import date

st.set_page_config(page_title='NOOK Editorial V4', layout='wide', initial_sidebar_state='collapsed')

# ---------- DATA ----------
if 'members' not in st.session_state:
    st.session_state.members = pd.DataFrame([
        ['Kabir Anand','Approved','First Out'],['Ishita Rao','Approved','Worth It'],['Dev Sharma','Waitlist','IBP']
    ], columns=['Name','Status','Tier'])

if 'events' not in st.session_state:
    st.session_state.events = pd.DataFrame([
        ['Canvas Night','Saturday','MP Nagar'],['Rooftop Chai','Thursday','Arera']
    ], columns=['Experience','Day','Location'])

# ---------- STYLE ----------
st.markdown('''
<style>
@import url("https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;700&family=Inter:wght@400;600;800&display=swap");
html,body,[class*='css']{background:#0b0a09;color:#f3eee6;font-family:Inter,sans-serif}
.block-container{padding:0;max-width:100%}
section[data-testid='stSidebar']{background:#0b0a09;border-right:1px solid rgba(255,255,255,.06)}
.hero{padding:6rem 8rem;background:linear-gradient(90deg,rgba(60,10,5,.9),rgba(20,10,8,.7));min-height:88vh;display:flex;align-items:center}
.hero h1{font-family:'Cormorant Garamond',serif;font-size:5.5rem;line-height:.92;margin:0;font-weight:700}
.hero p{font-size:1.15rem;color:#d7cec3;max-width:620px;line-height:1.8}
.btn{display:inline-block;padding:.9rem 1.4rem;border-radius:999px;background:#d8c4aa;color:#111;text-decoration:none;font-weight:700}
.section{padding:5rem 8rem}
.cream{background:#ece6da;color:#231c18}.cream p{color:#4c433d}
.wine{background:#5c1f17}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:3rem;align-items:center}
.title{font-family:'Cormorant Garamond',serif;font-size:3.2rem;line-height:1}
.small{letter-spacing:.22em;text-transform:uppercase;font-size:.72rem;opacity:.7}
.card{padding:2rem;border:1px solid rgba(255,255,255,.08);border-radius:24px;background:rgba(255,255,255,.03)}
table{color:inherit}
</style>
''', unsafe_allow_html=True)

mode = st.sidebar.radio('Mode',['Public Website','Founder Portal'])

# ---------- PUBLIC WEBSITE ----------
if mode == 'Public Website':
    st.markdown("""
    <section class='hero'>
      <div>
        <div class='small'>NOOK / PRIVATE SOCIAL CLUB</div>
        <h1>BUILD THE SOCIAL LIFE YOU'VE BEEN WANTING</h1>
        <p>Curated gatherings, meaningful rooms, and elevated weekends for people who want more than random plans.</p>
        <br><a class='btn'>Apply For Access</a>
      </div>
    </section>
    <section class='section cream'>
      <div class='grid2'>
        <div>
          <div class='title'>Build a richer social life in 30 days — without burnout.</div>
          <p>Small intentional circles. Better people. Better energy. Better stories.</p>
        </div>
        <div>
          <div class='card'>Private dinners<br><br>Creative nights<br><br>Curated walks<br><br>Members only rooms</div>
        </div>
      </div>
    </section>
    <section class='section wine'>
      <div class='grid2'>
        <div class='card'>[ editorial image space ]</div>
        <div>
          <div class='title'>Meet Nook</div>
          <p>Nook exists for people tired of shallow plans, passive weekends, and low-quality social circles.</p>
          <a class='btn'>Why We Built This</a>
        </div>
      </div>
    </section>
    <section class='section cream'>
      <div class='small'>Featured In Spirit</div>
      <div class='title'>Vogue • Monocle • Forbes • Culture</div>
    </section>
    """, unsafe_allow_html=True)

    st.markdown("<div class='section'><div class='title'>Upcoming Experiences</div></div>", unsafe_allow_html=True)
    st.dataframe(st.session_state.events, use_container_width=True)

# ---------- FOUNDER PORTAL ----------
else:
    st.title('Founder Portal')
    page = st.radio('Navigate',['Members','Waitlist','Events','Settings'], horizontal=True)
    if page == 'Members':
        st.dataframe(st.session_state.members, use_container_width=True)
    elif page == 'Waitlist':
        st.dataframe(st.session_state.members[st.session_state.members['Status']=='Waitlist'], use_container_width=True)
    elif page == 'Events':
        st.dataframe(st.session_state.events, use_container_width=True)
        with st.form('new_event'):
            a,b,c = st.columns(3)
            ex = a.text_input('Experience')
            dy = b.text_input('Day')
            lo = c.text_input('Location')
            if st.form_submit_button('Add Experience'):
                st.session_state.events.loc[len(st.session_state.events)] = [ex,dy,lo]
                st.success('Added')
    else:
        st.text_input('Admin Email')
        st.toggle('Invite Only', True)
        st.button('Save')
