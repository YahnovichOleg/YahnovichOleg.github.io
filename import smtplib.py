import smtplib
from email.message import EmailMessage

email_sender = 'Your_Friend@gmail.com'
email_receiver = 'oleg@10secure.com' 

subject = 'How Are You ?'
body = 'הכל טוב אחי?'

# Create message object
message = EmailMessage()
message['From'] = email_sender
message['To'] = email_receiver
message['Subject'] = subject 
message.set_content(body)

# Send email 
with smtplib.SMTP('23.90.111.87', 25) as server:
  server.send_message(message)