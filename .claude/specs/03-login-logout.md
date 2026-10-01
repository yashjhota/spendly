# Spec: Login and Logout

## Overview
This feature implements the authentication flow for Spendly, allowing registered users to securely sign into their accounts and sign out. This is a critical step in the roadmap as it enables user-specific data access for the subsequent expense tracking and profile features.

## Depends on
- Step 02: Registration

## Routes
- `GET /login` — Renders the login page — public
- `POST /login` — Validates credentials and starts user session — public
- `GET /logout` — Clears the user session and redirects to landing — logged-in

## Database changes
No database changes.

## Templates
- **Modify:** `templates/login.html` — Update to include a proper `<form>` for POST requests.

## Files to change
- `app.py` — Implement login and logout logic.

## Files to create
No new files.

## New dependencies
No new dependencies.

## Rules for implementation
- No SQLAlchemy or ORMs
- Parameterised queries only
- Passwords hashed with werkzeug
- Use CSS variables — never hardcode hex values
- All templates extend `base.html`
- Use Flask `session` to track the logged-in user's ID.

## Definition of done
- [ ] User can successfully log in with valid email and password.
- [ ] User is redirected to a protected page (or landing) upon successful login.
- [ ] User receives a flash error message when providing an incorrect password.
- [ ] User receives a flash error message when providing an email that doesn't exist.
- [ ] User can successfully log out, clearing their session.
- [ ] Accessing a protected route after logout redirects the user to the login page.
