# Spec: Registrations

## Overview
This feature implements the user registration flow, allowing new users to create an account by providing their name, email, and password. This is a foundational step that enables personalized expense tracking and secure access to user data.

## Depends on
- 01-database-setup

## Routes
- `GET /register` — Display registration form — public
- `POST /register` — Handle registration logic and create user — public

## Database changes
No database changes. (The `users` table already exists with the required fields).

## Templates
- **Create:** `templates/register.html` (Modify existing placeholder if present)
- **Modify:** None

## Files to change
- `app.py` — Add POST handler for `/register` and import request/redirect/flash

## Files to create
- No new files.

## New dependencies
No new dependencies.

## Rules for implementation
- No SQLAlchemy or ORMs
- Parameterised queries only
- Passwords hashed with werkzeug
- Use CSS variables — never hardcode hex values
- All templates extend `base.html`

## Definition of done
- [ ] Visiting `/register` displays a form with Name, Email, and Password fields.
- [ ] Submitting the form with valid details successfully creates a user in the `users` table.
- [ ] Submitting the form with an existing email returns a user-friendly error message.
- [ ] Passwords stored in the database are hashed and not plain text.
- [ ] After successful registration, the user is redirected to the login page.
