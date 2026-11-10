# Running the imported project

- Use the **Start application** workflow (or run `python3 server.py`).
- The server listens on `0.0.0.0:5000` and serves the existing `login.html` at `/` and `/login.html`.
- Python's standard library is sufficient; no third-party dependencies or secrets are required.
- Only the login page is served; other workspace files are not public.

## Current scope

This is a standalone HTML/CSS/JavaScript login demo, not a working authentication system.
Email/password submission validates input and shows a simulated success message.
Google sign-in, account creation, password reset, and persistent sessions are not implemented.
Do not enter real credentials. No authentication provider or backend was added during import setup.
