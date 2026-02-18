# Cyber Password Strength Checker

A Flask-based web application that analyzes password strength using entropy calculation and estimates crack time based on brute-force attack simulation.

## Features

- Entropy calculation using character set analysis
- Estimated crack time calculation
- Strength classification (Weak / Moderate / Strong / Very Strong)
- Detection of common passwords
- Cyber-themed animated Matrix-style UI

## Technologies Used

- Python
- Flask
- HTML
- CSS
- JavaScript

## How It Works

The application calculates password entropy using:

Entropy = Length × log2(Character Set Size)

Based on entropy, it estimates crack time assuming 1 billion guesses per second and classifies the strength accordingly.

## Installation

1. Clone the repository
2. Install dependencies:

pip install flask

3. Run the application:

python app.py

4. Open browser and go to:

http://127.0.0.1:5000

## Project Structure

password-checker/
│
├── app.py
├── common_passwords.txt
├── templates/
│   └── index.html
├── static/
│   └── style.css
└── README.md

## Author

Sudhansu Kumar Sahoo
