import os
import requests
import hashlib
import smtplib
from email.mime.text import MIMEText

# Config
URL = "https://cetcell.mahacet.org/"  # 🔁 Replace with your real URL
SENDER = os.getenv("SENDER_EMAIL")
RECEIVER = os.getenv("RECEIVER_EMAIL")
APP_PASSWORD = os.getenv("APP_PASSWORD")
HASH_FILE = "last_hash.txt"

def get_current_hash(url):
    response = requests.get(url)
    return hashlib.md5(response.text.encode('utf-8')).hexdigest()

def load_previous_hash():
    if os.path.exists(HASH_FILE):
        with open(HASH_FILE, "r") as f:
            return f.read().strip()
    return ""

def save_current_hash(hash_val):
    with open(HASH_FILE, "w") as f:
        f.write(hash_val)

def send_email_alert():
    msg = MIMEText(f"🔔 Website content has changed: {URL}")
    msg["Subject"] = "Website Change Detected"
    msg["From"] = SENDER
    msg["To"] = RECEIVER

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(SENDER, APP_PASSWORD)
        server.send_message(msg)

def main():
    current_hash = get_current_hash(URL)
    previous_hash = load_previous_hash()

    if current_hash != previous_hash:
        print("Change detected!")
        send_email_alert()
        save_current_hash(current_hash)
    else:
        print("No change.")

if __name__ == "__main__":
    main()
