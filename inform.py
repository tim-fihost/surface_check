import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
my_email = os.environ['EMAIL']
my_password = os.environ['G_PW']
recipient_email = "timuleooo0212@gmail.com"
def send_email(price, link):
        with smtplib.SMTP('smtp.gmail.com', 587) as server: 
                msg = MIMEMultipart()
                msg['From'] = my_email
                msg['To'] = "timuleooo0212@gmail.com"
                msg['Subject'] = "Hello Check Toaday's Price"
                body = f"""Good day!
We have a great news check the price today for your item.
Price:{price}
Link: {link}"""
                msg.attach(MIMEText(body, 'plain'))
                server.starttls()
                server.login(my_email, my_password)
                server.sendmail(my_email, recipient_email, msg.as_string())
