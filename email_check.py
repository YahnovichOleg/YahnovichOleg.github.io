import smtplib


# Set up the email message
subject = "Test email"
body = "This is a test email sent from Python."
sender_email = "ptptemail@gmail.com"
recipient_email = "xvvirus@gmail.com"
message = f"Subject: {subject}\n\n{body}"

# Log in to the SMTP server and send the email
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login("ptptemail@gmail.com", "kwhk wnwo cfci aetk")
    smtp.sendmail("test@gmail.com", recipient_email, message)
