
import telnetlib

# Connect to the server
tn = telnetlib.Telnet('23.90.111.87', 25)

# Send EHLO command
tn.write(b'EHLO oferdor.com\r\n')
print(tn.read_until(b'\r\n'))

tn.close()