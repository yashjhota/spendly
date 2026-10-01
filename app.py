from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from database.db import init_db, seed_db, get_db

app = Flask(__name__)
app.secret_key = "dev-secret-key-for-spendly"


# ------------------------------------------------------------------ #
# Routes                                                              #
# ------------------------------------------------------------------ #

@app.route("/")
def landing():
    return render_template("landing.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")

        if not name or not email or not password:
            flash("All fields are required.")
            return redirect(url_for("register"))

        if len(password) < 8:
            flash("Password must be at least 8 characters long.")
            return redirect(url_for("register"))

        with get_db() as conn:
            # Check if email already exists
            existing_user = conn.execute("SELECT 1 FROM users WHERE email = ?", (email,)).fetchone()
            if existing_user:
                flash("An account with this email already exists.")
                return redirect(url_for("register"))

            # Hash password and insert user
            hashed_password = generate_password_hash(password)
            conn.execute(
                "INSERT INTO users (name, email, password_hash) VALUES (?, ?, ?)",
                (name, email, hashed_password)
            )
            conn.commit()

        flash("Account created successfully! Please sign in.")
        return redirect(url_for("login"))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        if not email or not password:
            flash("All fields are required.")
            return redirect(url_for("login"))

        with get_db() as conn:
            user = conn.execute(
                "SELECT id, password_hash FROM users WHERE email = ?",
                (email,)
            ).fetchone()

            if user and check_password_hash(user["password_hash"], password):
                session["user_id"] = user["id"]
                flash("Successfully signed in!")
                return redirect(url_for("landing"))

            flash("Invalid email or password.")
            return redirect(url_for("login"))

    return render_template("login.html")


# ------------------------------------------------------------------ #
# Placeholder routes — students will implement these                  #
# ------------------------------------------------------------------ #

@app.route("/logout")
def logout():
    session.clear()
    flash("You have been logged out successfully.")
    return redirect(url_for("landing"))


@app.route("/profile")
def profile():
    return "Profile page — coming in Step 4"


@app.route("/expenses/add")
def add_expense():
    return "Add expense — coming in Step 7"


@app.route("/expenses/<int:id>/edit")
def edit_expense(id):
    return "Edit expense — coming in Step 8"


@app.route("/expenses/<int:id>/delete")
def delete_expense(id):
    return "Delete expense — coming in Step 9"


if __name__ == "__main__":
    with app.app_context():
        init_db()
        seed_db()
    app.run(debug=True, port=5001)
