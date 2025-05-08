import smtplib
import imghdr
from email.message import EmailMessage

PASSWORD="ynachlnxkglvoeby"
SENDER = "swarup111505@gmail.com"
RECEIVER = "swarup111505@gmail.com"

def send_email(image_path):
    print("email start")
    email_message = EmailMessage()
    email_message["Subject"] = "New customer showed up!!"
    email_message.set_content("Hey, there is new customer..")

    with open(image_path,"rb") as file:
        content = file.read()
    email_message.add_attachment(content,maintype = "image",subtype= imghdr.what(None,content))

    gmail =  smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER,PASSWORD)
    gmail.sendmail(SENDER,RECEIVER,email_message.as_string())
    gmail.quit()
    print("email ended")

