import smtplib
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

otp = random.randint(1111,9999)
body = f"OTP for verification is {otp}"

msg = MIMEMultipart()
msg["From"] = "hemanth.d735@gmail.com"
msg["To"] = input("Enter Email Id: ")
msg["Subject"] = "OTP For Validation"
msg.attach(MIMEText(body,'plain'))

server =smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login("hemanth.d735@gmail.com","jnqg ewls gpqt mtfh")
server.send_message(msg)
server.quit()
sai = int(input("enter OTP RECEIVED BY {receiver} : "))

if sai==otp:
    print("OTP Verfication Success")
else:
    print("OTP invalid")

