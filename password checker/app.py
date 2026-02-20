from flask import Flask, render_template, request
import math
import string

app = Flask(__name__)

# Load common passwords
with open("common_passwords.txt", "r") as f:
    common_passwords = set(line.strip() for line in f)

def calculate_entropy(password):
    charset = 0

    if any(c.islower() for c in password):
        charset += 26
    if any(c.isupper() for c in password):
        charset += 26
    if any(c.isdigit() for c in password):
        charset += 10
    if any(c in string.punctuation for c in password):
        charset += len(string.punctuation)

    if charset == 0:
        return 0

    entropy = len(password) * math.log2(charset)
    return round(entropy, 2)

def estimate_crack_time(entropy):
    guesses_per_second = 1_000_000_000  # 1 billion guesses/sec
    seconds = (2 ** entropy) / guesses_per_second

    if seconds < 60:
        return f"{round(seconds,2)} seconds"
    elif seconds < 3600:
        return f"{round(seconds/60,2)} minutes"
    elif seconds < 86400:
        return f"{round(seconds/3600,2)} hours"
    elif seconds < 31536000:
        return f"{round(seconds/86400,2)} days"
    else:
        return f"{round(seconds/31536000,2)} years"

def check_strength(password):
    if password in common_passwords:
        return "Very Weak"

    entropy = calculate_entropy(password)

    if entropy < 28:
        return "Very Weak"
    elif entropy < 36:
        return "Weak"
    elif entropy < 60:
        return "Moderate"
    elif entropy < 128:
        return "Strong"
    else:
        return "Very Strong"

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        password = request.form["password"]
        entropy = calculate_entropy(password)
        crack_time = estimate_crack_time(entropy)
        strength = check_strength(password)

        result = {
            "entropy": entropy,
            "crack_time": crack_time,
            "strength": strength
        }

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
