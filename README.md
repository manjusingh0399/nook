# nook

# Nook Control Room

Deployable static web app for managing Nook waitlist submissions, members, facilitators, availability, onboarding, experiences, and local admin data.
Deployable web app for managing Nook waitlist submissions, members, facilitators, availability, onboarding, experiences, and local admin data.

This repo supports two deploy paths:

- Streamlit Community Cloud from GitHub
- Static hosting with Netlify, Vercel, or any static host

## Deploy with GitHub and Streamlit

1. Create a GitHub repository.
2. Push this `nook-control-room` folder to the repository.
3. Go to [Streamlit Community Cloud](https://share.streamlit.io/).
4. Create a new app from your GitHub repo.
5. Set the main file path to `streamlit_app.py`.
6. Open the app settings and add this secret:

```toml
APP_PASSWORD = "choose-a-strong-password"
```

7. Deploy.

Streamlit will install `requirements.txt`, run `streamlit_app.py`, and serve the existing control room inside the Streamlit app.

## Run locally


The production build is written to `dist/`.

## Deploy
## Deploy As Static App

### Netlify


## Important security note

This is a static browser app. The current login is convenience access only because usernames and passwords are shipped in the client code. For public production use, put the app behind real authentication such as Netlify password protection, Vercel/Cloudflare access, Firebase Auth, Supabase Auth, or a small backend.
The original control room is a browser app. Its built-in usernames and passwords are convenience access only because they live in client-side code. The Streamlit wrapper adds a first password gate with `APP_PASSWORD`, but for sensitive production data you should use a private GitHub repo and keep the Streamlit app shared only with trusted admins.
