from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import email
import smtplib
import imaplib
import os

from dotenv import load_dotenv, find_dotenv


class MailWorker:

    def __init__(self, login, my_password, header):
        self.login = login
        self.password = my_password
        self.header = header

    def send_message(self, recipients: list, message, subject, gmail_smtp):

        self.msg = MIMEMultipart()
        self.msg['From'] = self.login
        self.msg['To'] = ", ".join(recipients)
        self.msg['Subject'] = subject
        self.msg.attach(MIMEText(message))

        self.ms = smtplib.SMTP(gmail_smtp, 587)
        self.ms.ehlo()
        self.ms.starttls()
        self.ms.ehlo()

        self.ms.login(self.login, self.password)
        self.ms.sendmail(self.login, self.ms, self.msg.as_string())

        self.ms.quit()
        return recipients, message, subject, gmail_smtp

    def recieve_mail(self, gmail_imap):
        self.mail = imaplib.IMAP4_SSL(gmail_imap)
        self.mail.login(self.login, self.password)
        self.mail.list()
        self.mail.select("inbox")

        criterion = '(HEADER Subject "%s")' % self.header if self.header else 'ALL'
        result, data = self.mail.uid('search', None, criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result, data = self.mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email.message_from_string(raw_email)

        self.mail.logout()
