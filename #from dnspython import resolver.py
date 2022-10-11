#from dnspython import resolver
import dns.resolver
import smtplib
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage




email_sender = 'Your_Friend@gmail.com'
email_receiver = 'oleg@10secure.com' 


#Find Domain of Sender
def resolvedns(email):
 domain = email.partition("@")
 print(domain[2])
 answersmx = dns.resolver.resolve(domain[2], 'MX')
 mxlist=[]
 iplist=[]
 for rdata in answersmx:
     mxlist.append(rdata.exchange)
 
 print(mxlist[0])
 answersip = dns.resolver.resolve(mxlist[0])
 for rdata in answersip:
     iplist.append(rdata)
 print(iplist)
    
 return(iplist)

mxrecord=resolvedns(email_receiver)
print(mxrecord[0])
ip = mxrecord[0]
print("The ip"+str(ip))
subject = 'How Are You ?'
body = 'הכל טוב אחי?'

# Create message object

message = EmailMessage()
message['From'] = email_sender
message['To'] = email_receiver
message['Subject'] = subject 
message.set_content(body)
print("\n\n\n\n\n\n\n\n\n\n\n")
print(message)

print("\n\n\n\n\n\n\n\n\n\n\n")

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



## Send email 
#with smtplib.SMTP(str(mxrecord[0]), 25) as server:
#with smtplib.SMTP("23.90.111.87", 25) as server:
#  server.send_message(message)



