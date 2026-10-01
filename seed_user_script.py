import random
from datetime import datetime
from werkzeug.security import generate_password_hash
from database.db import get_db

def generate_indian_user():
    first_names = ["Rahul", "Priya", "Amit", "Anjali", "Siddharth", "Sneha", "Vikram", "Ishita", "Arjun", "Kavita", "Rohan", "Meera", "Aditya", "Diya", "Sameer", "Tanvi"]
    last_names = ["Sharma", "Verma", "Gupta", "Malhotra", "Iyer", "Reddy", "Patel", "Singh", "Chatterjee", "Nair", "Kulkarni", "Joshi", "Deshmukh", "Pandey"]

    first = random.choice(first_names)
    last = random.choice(last_names)
    full_name = f"{first} {last}"

    # Email: rahul.sharma91@gmail.com
    email_name = f"{first.lower()}.{last.lower()}"
    suffix = random.randint(10, 999)
    email = f"{email_name}{suffix}@gmail.com"

    return {
        "name": full_name,
        "email": email,
        "password_hash": generate_password_hash("password123"),
        "created_at": datetime.now().isoformat()
    }

def seed_user():
    with get_db() as conn:
        while True:
            user_data = generate_indian_user()
            # Check if email exists
            existing = conn.execute("SELECT id FROM users WHERE email = ?", (user_data["email"],)).fetchone()
            if not existing:
                break

        cursor = conn.execute(
            "INSERT INTO users (name, email, password_hash, created_at) VALUES (?, ?, ?, ?)",
            (user_data["name"], user_data["email"], user_data["password_hash"], user_data["created_at"])
        )
        conn.commit()

        print(f"User seeded successfully:")
        print(f"id: {cursor.lastrowid}")
        print(f"name: {user_data['name']}")
        print(f"email: {user_data['email']}")

if __name__ == "__main__":
    seed_user()
