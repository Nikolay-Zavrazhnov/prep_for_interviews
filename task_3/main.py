from module.class_mail import MailWorker
import os
from dotenv import load_dotenv, find_dotenv

if __name__ == '__main__':
    load_dotenv(find_dotenv())

    instance = MailWorker(os.getenv('login'), os.getenv('password'), None)
    instance.send_message(['wdwd@dddd'], 'message', 'probuyu', gmail_smtp="smtp.gmail.com")
    instance.recieve_mail(gmail_imap="imap.gmail.com")