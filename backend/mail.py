import sendgrid
import os
from sendgrid.helpers.mail import *

def send_mail(resp,text):
    e_to = resp["entities"]["email"][0]["value"]
    e_from = resp["entities"]["email"][2]["value"]
    words = text.split('"')
    content = words[1]
    subject = words[3]
    sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
    from_email = Email(e_from)
    to_email = Email(e_to)
    content = Content("text/plain", content)
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    if response.status_code == 202:
        return "Message is queued to be delivered and will reach the recipient soon."
    elif response.status_code >= 400:
        return "Hmm... something seems to be wrong... Try again later maybe"