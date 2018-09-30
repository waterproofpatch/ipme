#!/usr/bin/env python3
import requests
import os
import sys
import smtplib

def send_email(email_sender, password, email_recipient, message):
    """
    Send the email
    
    :param email_sender: the address of the sender (used for login)
    :param password: the senders password
    :param email_recipient: the recipients email
    :param message: the message to send
    """
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    email_sender = os.environ.get('EMAIL', email_sender)
    password = os.environ.get('PASSWORD', password)
    if email_sender is None or password is None:
        print("missing email/password")
        server.quit()
        return False
    server.login(email_sender, password)
    server.sendmail(email_sender, email_recipient, message)
    server.quit()
    return True

def get_ip():
    """
    Get the IP of this host as the internet sees it...

    :return: the IP address as a string, or None
    """
    response = requests.get('https://api.ipify.org?format=json')
    if response.status_code != 200 or 'ip' not in response.json():
        return None
    return response.json()['ip']


def main():
    """
    Main function
    """
    email_sender = None
    password = None
    email_recipient = 'waterproofpatch@gmail.com'
    if len(sys.argv) == 4:
        email_sender = sys.argv[1]
        password = sys.argv[2]
        email_recipient = sys.argv[3]

    ip = get_ip()

    send_email(email_sender=email_sender, 
            password=password,
            email_recipient=email_recipient,
            message="IP is {}".format(ip))

if __name__ == "__main__":
    main()

