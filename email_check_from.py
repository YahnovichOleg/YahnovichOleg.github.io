import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

# Set up the message

class CreateMessage:
    def __init__(self, body, subject = "Subject of the email", ):
      self.msg = MIMEMultipart()
      self.msg['From'] = 'PT@gmail.com'
      self.msg['To'] = 'You@gmail.com'
      self.msg['Subject'] = subject
      self.body = body
      self.msg.attach(MIMEText(body, 'plain'))

Virus = CreateMessage("X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*", "Test Virus")
Spam = CreateMessage("XJS*C4JDBQADN1.NSBN3*2IDNEN*GTUBE-STANDARD-ANTI-UBE-TEST-EMAIL*C.34X", "Test Spam")
Phishing = CreateMessage("XJS*C4JDBQADN1.NSBN3*2IDNEN*GTPHISH-STANDARD-ANTI-PHISH-TEST-EMAIL*C.34X ", "Test  Phishing")
Inappropriate_Content = CreateMessage("", "Test Inappropriate Content")
URL_Malicious  = CreateMessage("X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*", "Test URL Malicious")
Base64  = CreateMessage("X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*", "Test Base64")
print(Virus.msg.as_string())
print("------------\n\n\n\n\n")
#print(Spam.msg)

#
#choise = input("""Enter Your Choise
#          1. Check Virus
#          2. Check Spam
#          3. Check Phishing 
#          4. Check Inappropriate_Content
#          5. Check Inappropriate URL Malicious 
#          5. Check Base64
#          6. Check All \n """)
#print(choise)



# Attach an image (optional)
#with open('image.jpg', 'rb') as f:
##    img = MIMEImage(f.read())
##    img.add_header('Content-Disposition', 'attachment', filename='image.jpg')
##    msg.attach(img)
#
## Log in to the server
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('ptptemail@gmail.com', 'kwhk wnwo cfci aetk')

# Send the message
server.sendmail('test@gmail.com', 'oleg@10secure.com', Virus.msg.as_string())
server.quit()
#
'''Register Now Phshing URL
http://track.senderbulk.com/9125644/c?p=iXEAz8_boIqKaSMD8dDE4bXXWBS2Fdm7k6U-vQTktr0w2WA2D48K1Qng7mqXb5gyFu50TCduajDqHQnlk3KV9EISxNg6p-I5HsX_EVg5uTgNE-zJv-2-o8N0TPGiT_SgNEbY2zyLqhRXtq77WH1PSOpdjwMW9_-3p_bnCvyHG28=

Register for livestream >
http://track.senderbulk.com/9125644/c?p=g9kYvFFzErrUP6yfCH0ZlKWHBwPtWqjqngqiyLzhdqGlXw4BXqtER29OSgKLqdrXEbiZFoWQB1dHhfIHP7twyS2zK7q85zUrjHSkVWWw3gT-9TzxuvQJaFyy50D2nKBgvQr6Ih5a7raZaUCxpiaeI7OBU5KGiJmZ08SFQnWlU_U='''