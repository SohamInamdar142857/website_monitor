import smtplib
from email.mime.text import MIMEText

def send_test_email():
    sender = "srinamdar780@gmail.com"
    receiver = "inamdar.swapna@gmail.com"
    password = "hsru dckc eshw vqtg"

    subject = "✅ Test Email from Python"
    body = "This is a test email to confirm the mailing function works."

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = receiver

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender, password)
            server.sendmail(sender, receiver, msg.as_string())
        print("✅ Test email sent successfully!")
    except Exception as e:
        print("❌ Failed to send email:", e)

send_test_email()
