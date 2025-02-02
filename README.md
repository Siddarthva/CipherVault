CipherVault 🚀

A Secure Password Manager Built with Python

CipherVault is a modern password manager designed to securely store and manage your passwords. With a user-friendly interface and robust encryption, CipherVault ensures your passwords are safe and easily accessible.

Features

- User Registration & Login: Secure registration and login system with hashed passwords and unique salts. 🔒
- Password Storage: Store site-specific passwords with strong encryption. 📈
- Password Viewing: Retrieve and view encrypted passwords for saved sites. 🔍
- Modern Security Standards: Ensures password safety using SHA-256 hashing and encryption mechanisms. 🔒

Getting Started

To set up and use CipherVault locally, follow these steps:

Prerequisites
- Python 3.6 or later 🐍

Installation
1. Clone the repository:

bash
git clone https://github.com/Siddarthva/CipherVault.git
cd CipherVault

2. Install required dependencies: CipherVault does not rely on external libraries. Ensure you have Python installed. 📦
3. Run the application:

bash
python ciphervault_app.py


Usage

1. Register: Create a new account with a secure master password. 📝
2. Login: Log in to access your vault. 🔓
3. Add Passwords: Save passwords for different sites securely. 📈
4. View Passwords: View all saved passwords (encrypted). 🔍

Project Structure

- ciphervault_app.py: Main script containing all functionalities. 📄
- ciphervault.db: SQLite database to store user and vault information. 📁

Security Features

- Password Hashing: All master passwords are hashed with a unique salt before being stored in the database. 🔒
- Encryption: Site passwords are encrypted with a key derived from the user's master password. 🔒
- Validation: Ensures strong password policies during registration. 🔒

Contributing

Contributions are welcome! Feel free to fork the repository, make your changes, and submit a pull request.

1. Fork the project. 📋
2. Create your feature branch:

bash
git checkout -b feature/YourFeatureName

3. Commit your changes:

bash
git commit -m 'Add your feature description here'

4. Push to the branch:

bash
git push origin feature/YourFeatureName

5. Open a pull request. 📬

License

This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgements

- Python for its simplicity and flexibility. 🐍
- SQLite for providing a lightweight database solution. 📁
