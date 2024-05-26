import smtplib, sys
from email.mime.text import MIMEText

# SETTINGS: PotMail.MailRuService or custom settings
# If you have filled in the SETTINGS field, then you don't need to fill in other fields!

class PotMail:
    def __init__(self, setting=None, address="smtp.gmail.com", port=587, sec_type="tls"):
        if setting == "MailServices":
            self.host = smtplib.SMTP_SSL("smtp.mail.ru", 465)

        else:
            if sec_type == "tls":
                self.host = smtplib.SMTP(address, port)
                self.host.starttls()
            elif sec_type == "ssl":
                self.host = smtplib.SMTP_SSL(address, port)

    def login(self, email, password):
        self.host.login(email, password)

    def send(self, from_mail, to_mail, subject_text, message_text):
        msg = MIMEText(message_text)
        msg["Subject"] = subject_text
        self.host.sendmail(from_mail, to_mail, msg.as_string())
