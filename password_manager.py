import hashlib
import os
import sqlite3
from getpass import getpass
import re

# Database setup
db_name = "ciphervault.db"
conn = sqlite3.connect(db_name)
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY,
    password_hash TEXT NOT NULL,
    salt TEXT NOT NULL
)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS vault (
    username TEXT,
    site TEXT,
    encrypted_password TEXT,
    FOREIGN KEY (username) REFERENCES users(username)
)''')
conn.commit()

# Helper functions
def hash_password(password, salt):
    return hashlib.sha256((password + salt).encode()).hexdigest()

def generate_salt():
    return os.urandom(16).hex()

def encrypt_password(master_key, password):
    key = hashlib.sha256(master_key.encode()).digest()
    return hashlib.sha256((key.hex() + password).encode()).hexdigest()

def is_valid_password(password):
    if len(password) < 8 or not re.search(r"[A-Za-z]", password) or not re.search(r"[0-9]", password):
        return False
    return True

def register_user():
    username = input("Enter a username: ").strip()
    if not username:
        print("Username cannot be empty.")
        return

    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    if cursor.fetchone():
        print("Username already exists.")
        return

    salt = generate_salt()
    while True:
        password = getpass("Create a master password (at least 8 characters, include letters and numbers): ")
        if is_valid_password(password):
            break
        print("Invalid password. Please try again.")

    password_hash = hash_password(password, salt)
    cursor.execute("INSERT INTO users (username, password_hash, salt) VALUES (?, ?, ?)", (username, password_hash, salt))
    conn.commit()
    print("Registration successful! Please log in.")

def login_user():
    username = input("Enter your username: ").strip()
    password = getpass("Enter your master password: ")

    cursor.execute("SELECT password_hash, salt FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()

    if not result:
        print("Invalid username or password.")
        return None

    password_hash, salt = result
    if hash_password(password, salt) != password_hash:
        print("Invalid username or password.")
        return None

    print("Login successful!")
    return username

def add_password(username):
    site = input("Enter the site name: ").strip()
    if not site:
        print("Site name cannot be empty.")
        return

    password = getpass("Enter the site password: ")
    encrypted_password = encrypt_password(username, password)
    cursor.execute("INSERT INTO vault (username, site, encrypted_password) VALUES (?, ?, ?)", (username, site, encrypted_password))
    conn.commit()
    print(f"Password for {site} saved successfully.")

def view_passwords(username):
    cursor.execute("SELECT site, encrypted_password FROM vault WHERE username = ?", (username,))
    records = cursor.fetchall()

    if not records:
        print("No passwords saved yet.")
        return

    print("Saved passwords:")
    for site, enc_pass in records:
        print(f"Site: {site}, Password (Encrypted): {enc_pass}")

def main():
    print("Welcome to CipherVault!")

    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            register_user()
        elif choice == "2":
            username = login_user()
            if username:
                while True:
                    print("\n1. Add a password\n2. View passwords\n3. Logout")
                    user_choice = input("Choose an option: ").strip()

                    if user_choice == "1":
                        add_password(username)
                    elif user_choice == "2":
                        view_passwords(username)
                    elif user_choice == "3":
                        print("Logged out successfully.")
                        break
                    else:
                        print("Invalid option. Please try again.")
        elif choice == "3":
            print("Thank you for using CipherVault. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
