# nook v6 ecosystem

NOOK V6 splits the product into three focused apps over one Supabase backend:

- `admin_streamlit/` - founder dashboard, analytics, event ops, member management
- `frontend_next/` - member-facing Next.js app plus facilitator ops portal
- `supabase/schema.sql` - database, auth-linked profiles, RLS policies, views, functions
- `docs/` - architecture, AI layer, launch roadmap, and pitch-deck asset copy

## deploy targets

- Founder dashboard: Streamlit Cloud
- Member and facilitator frontend: Vercel
- Database and auth: Supabase
- AI features: OpenAI APIs called from server-side routes or Streamlit services

## local quick start

Admin:

```bash
cd nook_v6/admin_streamlit
pip install -r requirements.txt
streamlit run app.py
```

Frontend:

```bash
cd nook_v6/frontend_next
npm install
npm run dev
```

Environment variables:

```bash
SUPABASE_URL=
SUPABASE_SERVICE_ROLE_KEY=
NEXT_PUBLIC_SUPABASE_URL=
NEXT_PUBLIC_SUPABASE_ANON_KEY=
OPENAI_API_KEY=
```

