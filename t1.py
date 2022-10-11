import smtplib
from email.mime.text import MIMEText

# Set up the message
msg = MIMEText('Body of the email')
msg['Subject'] = 'Subject of the email'
msg['From'] = 'your_email@example.com'
msg['To'] = 'recipient_email@example.com'

# Connect to the server
server = smtplib.SMTP( "mx1.hc1240-30.eu.iphmx.com" , 25)

# Send the message
server.sendmail('your_email@example.com', 'oleg@10secure.com', msg.as_string())
#server.quit()