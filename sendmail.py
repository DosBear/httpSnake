import time
import smtplib
import os.path as op
from email import encoders
from email.utils import formatdate
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from config import MAIL_USERNAME, MAIL_PASSWORD, SMTP_SERVER_ADDR, MAIL_FROM_ADDR


def send_mail(header, text, send_to, files=[], use_tls=True):
    subj = "{0} at {1}".format(header, time.strftime("%d/%m/%Y %H:%M:%S"))
    msg_txt = "{0} \r\n---\r\nInfo Bot".format(text)
    msg = MIMEMultipart()
    msg['From'] = MAIL_FROM_ADDR
    msg['To'] = send_to
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subj

    msg.attach(MIMEText(msg_txt))
    print("Attach start")

    for f in files or []:
        with open(f, "rb") as fil:
            part = MIMEApplication(
                fil.read(),
                Name=op.basename(f)
            )
        part['Content-Disposition'] = 'attachment; filename="%s"' % op.basename(f)
        msg.attach(part)

    print("Connect")
    smtp = smtplib.SMTP(SMTP_SERVER_ADDR, 587, timeout=30)
    smtp.ehlo()
    smtp.starttls()
    print("Login")
    smtp.login(MAIL_USERNAME, MAIL_PASSWORD)
    print("Send")
    smtp.sendmail(MAIL_FROM_ADDR, send_to, msg.as_string())
    print("Exit")
    smtp.quit()

